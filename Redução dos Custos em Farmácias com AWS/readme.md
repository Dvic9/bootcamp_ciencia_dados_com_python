RELATÓRIO DE IMPLEMENTAÇÃO DE SERVIÇOS AWS

Data: 13/01/2026

Empresa: Abstergo Industries 

Responsável: Jonas Vitor

Introdução

Este relatório apresenta o processo de modernização da infraestrutura de TI da Abstergo Industries . O objetivo central é migrar nosso ambiente físico (que gera altos custos de manutenção e energia) para a nuvem da AWS.

Esta mudança estratégica visa transformar nossos custos fixos de hardware em custos variáveis, permitindo pagar apenas pelo que a empresa realmente consome, eliminando o desperdício financeiro com máquinas ociosas e garantindo a segurança dos dados regulatórios.

Descrição do Projeto

O projeto de implementação foi dividido em 3 etapas sequenciais e complementares. Cada etapa resolve um problema financeiro e operacional imediato:

Etapa 1: Amazon EC2 (Elastic Compute Cloud)

O que é: Servidores Virtuais.

Foco da ferramenta: Substituição de Hardware Físico e Redução de Manutenção.

Descrição de caso de uso: Atualmente, compramos servidores caros que desvalorizam com o tempo e exigem refrigeração/energia 24h. Com o EC2, vamos criar "máquinas virtuais" na nuvem para rodar nosso sistema de ERP e logística.

Como funciona a implantação: "Alugamos" a capacidade de processamento da AWS. Se a distribuidora tem pico de vendas no fim do mês, aumentamos a potência; nos dias calmos, diminuímos.

Ganho Financeiro: Fim da compra de servidores físicos (CAPEX) e redução drástica na conta de energia elétrica da sede.

Etapa 2: Amazon S3 (Simple Storage Service)

O que é: Armazenamento em Nuvem Altamente Seguro.

Foco da ferramenta: Backup, Arquivo Morto e Compliance Regulatório.

Descrição de caso de uso: Como distribuidora farmacêutica, precisamos guardar notas fiscais e laudos por anos (Anvisa). Hoje, isso ocupa discos rígidos caros e suscetíveis a falhas. O S3 funciona como um "arquivo infinito".

Como funciona a implantação: Configuramos nossos sistemas para enviar cópias de segurança (backups) e arquivos antigos automaticamente para o S3.

Ganho Financeiro: Custo de armazenamento extremamente baixo (centavos por GB). Elimina a necessidade de comprar HDs externos ou fitas de backup, além de garantir que nunca perderemos dados fiscais (evitando multas).

Etapa 3: Amazon RDS (Relational Database Service)

O que é: Banco de Dados Gerenciado.

Foco da ferramenta: Gestão de Estoque e Redução de Custo com Pessoal de TI.

Descrição de caso de uso: O coração da distribuidora é o banco de dados que controla o estoque e os pedidos. Manter isso funcionando hoje exige muitas horas extras da equipe de TI para atualizações e correções. O RDS automatiza tudo isso.

Como funciona a implantação: Migramos os dados brutos do estoque para o RDS. A AWS assume a responsabilidade pelas tarefas repetitivas (backups diários, atualizações de segurança).

Ganho Financeiro: Redução de horas-homem gastas em manutenção de rotina, permitindo que a equipe foque em melhorias de negócio, além de garantir que o sistema de vendas não saia do ar (alta disponibilidade).

Conclusão

A implementação destas ferramentas na Abstergo Industries  trará como resultado imediato a conversão de custos de investimento em custos operacionais controláveis.

Esperamos:

Eliminar a necessidade de renovação do parque de servidores físicos pelos próximos 5 anos.

Garantir segurança dos dados contra perdas físicas (incêndio, roubo ou falha de hardware).

Aumentar a agilidade da operação logística.

Recomenda-se a aprovação deste plano para início imediato da Etapa 1 (Migração dos Servidores).

Anexos

Planilha comparativa: Custo Servidor Físico vs. Custo Mensal AWS EC2.

Cronograma de migração (estimado em 3 meses).


Assinatura do Responsável pelo Projeto:

Jonas Vitor 
