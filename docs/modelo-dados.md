# Modelo de Dados (MVP)

## Entidades principais

## 1) veiculos

Armazena dados cadastrais da frota.

| Campo | Tipo | Regra |
|---|---|---|
| id | UUID | PK |
| identificacao | VARCHAR(50) | Único, obrigatório |
| modelo | VARCHAR(120) | Obrigatório |
| placa | VARCHAR(10) | Único, obrigatório |
| tipo_veiculo | VARCHAR(50) | Obrigatório |
| km_atual | INTEGER | >= 0 |
| status | VARCHAR(20) | `ativo`/`em_manutencao` |
| created_at | TIMESTAMP | Obrigatório |
| updated_at | TIMESTAMP | Obrigatório |

## 2) planos_manutencao

Define regras preventivas e periódicas por veículo.

| Campo | Tipo | Regra |
|---|---|---|
| id | UUID | PK |
| veiculo_id | UUID | FK -> veiculos.id |
| nome | VARCHAR(120) | Obrigatório |
| tipo | VARCHAR(30) | `preventiva`/`periodica` |
| periodicidade_km | INTEGER | Opcional |
| periodicidade_dias | INTEGER | Opcional |
| ativo | BOOLEAN | Default true |
| created_at | TIMESTAMP | Obrigatório |
| updated_at | TIMESTAMP | Obrigatório |

## 3) ordens_manutencao

Representa execuções de manutenção (preventiva, periódica ou corretiva).

| Campo | Tipo | Regra |
|---|---|---|
| id | UUID | PK |
| veiculo_id | UUID | FK -> veiculos.id |
| plano_id | UUID | FK opcional -> planos_manutencao.id |
| tipo | VARCHAR(30) | `preventiva`/`periodica`/`corretiva` |
| status | VARCHAR(30) | `aberta`/`em_andamento`/`finalizada` |
| prioridade | VARCHAR(20) | `baixa`/`media`/`alta`/`urgente` |
| descricao | TEXT | Obrigatório |
| data_abertura | TIMESTAMP | Obrigatório |
| data_conclusao | TIMESTAMP | Opcional |
| responsavel | VARCHAR(120) | Opcional |
| observacoes | TEXT | Opcional |
| custo_total | NUMERIC(12,2) | Default 0 |
| created_at | TIMESTAMP | Obrigatório |
| updated_at | TIMESTAMP | Obrigatório |

## 4) itens_ordem

Registra peças/serviços aplicados na ordem.

| Campo | Tipo | Regra |
|---|---|---|
| id | UUID | PK |
| ordem_id | UUID | FK -> ordens_manutencao.id |
| tipo_item | VARCHAR(20) | `peca`/`servico` |
| descricao | VARCHAR(180) | Obrigatório |
| quantidade | NUMERIC(10,2) | > 0 |
| valor_unitario | NUMERIC(12,2) | >= 0 |
| created_at | TIMESTAMP | Obrigatório |

## 5) comentarios_ordem

Comunicação entre operação e manutenção dentro da solicitação.

| Campo | Tipo | Regra |
|---|---|---|
| id | UUID | PK |
| ordem_id | UUID | FK -> ordens_manutencao.id |
| autor_nome | VARCHAR(120) | Obrigatório |
| autor_perfil | VARCHAR(30) | `operacao`/`manutencao`/`gestao` |
| mensagem | TEXT | Obrigatório |
| created_at | TIMESTAMP | Obrigatório |

## 6) alertas

Eventos disparados por prazo, km ou prioridade.

| Campo | Tipo | Regra |
|---|---|---|
| id | UUID | PK |
| veiculo_id | UUID | FK -> veiculos.id |
| ordem_id | UUID | FK opcional -> ordens_manutencao.id |
| tipo_alerta | VARCHAR(40) | `prazo_proximo`/`km_limite`/`urgente_aberta`/`atrasada` |
| mensagem | TEXT | Obrigatório |
| nivel | VARCHAR(20) | `info`/`atencao`/`critico` |
| resolvido | BOOLEAN | Default false |
| created_at | TIMESTAMP | Obrigatório |

## Regras de negócio essenciais

1. ordem corretiva urgente deve nascer com prioridade `urgente` e status `aberta`.
2. ordem finalizada exige ao menos uma observação de conclusão.
3. alerta de km é disparado quando `km_atual` >= `periodicidade_km` acumulada do plano.
4. alerta de atraso é disparado quando prazo planejado for ultrapassado sem finalização.
5. custo total da ordem é a soma dos itens (peças + serviços).
