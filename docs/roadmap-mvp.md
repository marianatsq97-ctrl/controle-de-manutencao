# Roadmap de Implementação (MVP)

## Fase 0 — Fundação (1 semana)

- Definição de requisitos funcionais e não funcionais.
- Modelagem do banco de dados.
- Setup do repositório, convenções e pipeline inicial.
- Definição da política de autenticação por perfil (`admin` e `usuario`).

## Fase 1 — Backend essencial (2 semanas)

- CRUD de veículos.
- CRUD de planos de manutenção.
- Abertura e atualização de ordens de manutenção.
- Registro de itens de ordem e comentários.
- Endpoint de listagem de histórico por veículo.

## Fase 2 — Autenticação e controle de acesso (1 semana)

- Login por pessoa (email/senha).
- Perfis `admin` e `usuario` com autorização por rota/tela.
- Gestão de usuários pelo perfil `admin`.

## Fase 3 — Alertas automáticos (1 semana)

- Job agendado para validação de manutenção por km/prazo.
- Geração de alertas para:
  - prazo próximo;
  - atraso;
  - km limite atingida;
  - corretiva urgente aberta.

## Fase 4 — Front-end operacional (2 semanas)

- Tela de cadastro de veículos.
- Tela de ordens de manutenção (kanban por status).
- Calendário de seleção de manutenções com filtros por veículo/tipo.
- Formulário de solicitação urgente.
- Timeline de histórico por veículo.
- Painel de alertas.

## Fase 5 — Indicadores de gestão (1 semana)

- Custo acumulado por frota.
- Ranking de veículos com mais ocorrências.
- Relatório de frequência de manutenção por tipo.

## Critérios de pronto do MVP

- Cadastro e atualização de veículos funcionando.
- Chamado urgente criado, atendido e finalizado com histórico.
- Login individual funcionando com segregação de acesso entre `admin` e `usuario`.
- Calendário de seleção exibindo manutenções por data/status.
- Alertas de prazo/km gerados automaticamente.
- Consulta de histórico e custo por veículo disponível.

## Arquitetura sugerida (profissional e escalável)

- Backend: Node.js + TypeScript + Fastify/NestJS.
- Banco de dados: PostgreSQL.
- Frontend: React + Vite.
- Jobs: BullMQ ou agenda com worker dedicado.
- Deploy: Docker + CI/CD (GitHub Actions).
