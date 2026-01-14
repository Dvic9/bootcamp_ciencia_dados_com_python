import pandas as pd
import json
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional

# --- Configuração da Documentação ---
app = FastAPI(
    title="PSN Stats & Marketing API - ETL Challenge",
    description="""
    API criada para o desafio de ETL adaptado para o ecossistema PlayStation. 
    Esta API simula um banco de dados de jogadores, suas assinaturas e consoles.
    
    **Fluxo de Dados:**
    * **Extract:** O Pipeline lê o PSN ID e consulta o perfil do jogador.
    * **Transform:** O Gemini analisa os jogos favoritos e envia uma recomendação personalizada.
    * **Load:** O Pipeline atualiza o campo 'notifications' com a sugestão da IA.
    """,
    version="1.0.0",
    contact={
        "name": "Dvic",
        "url": "https://github.com/Dvic9",
    },
)

DB_FILE = 'playstation_db.csv'

# --- Modelos de Dados Adaptados para Games ---
class Subscription(BaseModel):
    plan: str = Field(..., example="Plus Deluxe")
    status: str = Field(..., example="Active")
    expiry_date: str = Field(..., example="2025-12-31")
    level: int = Field(..., example=350, description="Nível do Troféu")

class Console(BaseModel):
    model: str = Field(..., example="PlayStation 5 Slim")
    serial_number: str = Field(..., example="ABC-123456")
    storage_used_gb: float = Field(..., example=650.5)

class Notification(BaseModel):
    type: str = Field(..., example="Recommendation")
    message: str = Field(..., example="Vimos que você platinou Elden Ring! Que tal testar Demon's Souls?")

class Player(BaseModel):
    id: int = Field(..., example=101)
    psn_id: str = Field(..., example="Dvic_Gamer")
    name: str = Field(..., example="Dvic")
    favorite_genre: str = Field(..., example="RPG / Soulslike")
    subscription: Subscription
    console: Console
    notifications: List[Notification] = Field(default=[], example=[])

# --- Helper Functions ---

def load_db():
    if not os.path.exists(DB_FILE):
        columns = ['id', 'psn_id', 'name', 'favorite_genre', 'subscription', 'console', 'notifications']
        df = pd.DataFrame(columns=columns)
        save_db(df)
        return df
    
    df = pd.read_csv(DB_FILE)
    if df.empty:
        return pd.DataFrame(columns=['id', 'psn_id', 'name', 'favorite_genre', 'subscription', 'console', 'notifications'])

    cols_to_json = ['subscription', 'console', 'notifications']
    for col in cols_to_json:
        df[col] = df[col].apply(lambda x: json.loads(x.replace("'", '"')) if isinstance(x, str) else x)
    return df

def save_db(df):
    df_to_save = df.copy()
    cols_to_json = ['subscription', 'console', 'notifications']
    for col in cols_to_json:
        df_to_save[col] = df_to_save[col].apply(json.dumps)
    df_to_save.to_csv(DB_FILE, index=False)

# --- Endpoints ---

@app.get("/players", response_model=List[Player], tags=["Jogadores"], summary="Listar todos os jogadores")
def list_players():
    """Retorna a lista completa de perfis de jogadores na base PSN."""
    df = load_db()
    return df.to_dict(orient='records')

@app.get("/players/{player_id}", response_model=Player, tags=["Jogadores"], summary="Obter jogador por ID")
def get_player(player_id: int):
    """Busca os detalhes de um jogador específico pelo ID interno."""
    df = load_db()
    player_row = df[df['id'] == player_id]
    if player_row.empty:
        raise HTTPException(status_code=404, detail="Jogador não encontrado")
    return player_row.iloc[0].to_dict()

@app.post("/players", response_model=Player, status_code=201, tags=["Jogadores"], summary="Cadastrar novo jogador")
def create_player(player: Player):
    """Registra um novo perfil de jogador no banco de dados CSV."""
    df = load_db()
    if not df.empty and player.id in df['id'].values:
        raise HTTPException(status_code=400, detail="ID de jogador já existe")
    
    new_player_df = pd.DataFrame([player.dict()])
    df = pd.concat([df, new_player_df], ignore_index=True)
    save_db(df)
    return player

@app.put("/players/{player_id}", response_model=Player, tags=["Jogadores"], summary="Atualizar perfil do jogador")
def update_player(player_id: int, updated_player: Player):
    """
    Atualiza dados do jogador. 
    Usado pelo Pipeline para inserir recomendações da IA no campo 'notifications'.
    """
    df = load_db()
    if df.empty or player_id not in df['id'].values:
        raise HTTPException(status_code=404, detail="Jogador não encontrado")
    
    df = df[df['id'] != player_id]
    new_player_df = pd.DataFrame([updated_player.dict()])
    df = pd.concat([df, new_player_df], ignore_index=True)
    
    save_db(df)
    return updated_player

@app.delete("/players/{player_id}", status_code=204, tags=["Jogadores"], summary="Remover perfil")
def delete_player(player_id: int):
    """Exclui permanentemente o perfil do jogador."""
    df = load_db()
    if df.empty or player_id not in df['id'].values:
        raise HTTPException(status_code=404, detail="Jogador não encontrado")
    
    df = df[df['id'] != player_id]
    save_db(df)
    return