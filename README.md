# Sistema de Controle de Manutenção de Frotas

Base inicial do projeto para gerenciamento de manutenção preventiva, periódica e corretiva de frotas.

## Objetivo

Centralizar as informações de manutenção em um único sistema para:

- organizar o controle por veículo;
- registrar solicitações urgentes;
- gerar alertas automáticos por prazo e quilometragem;
- manter comunicação entre operação e manutenção;
- preservar histórico completo de intervenções.

## Escopo funcional (MVP)

### 1. Cadastro de frotas

Dados mínimos por veículo:

- identificação interna da frota;
- modelo;
- placa;
- tipo de veículo;
- km atual;
- status (`ativo`, `em_manutencao`).

### 2. Plano de manutenção preventiva e periódica

Permite cadastrar regras como:

- troca de óleo a cada 10.000 km;
- revisão semanal;
- revisão geral a cada X meses.

Cada execução deve registrar:

- data de realização;
- responsável;
- peças trocadas;
- observações.

### 3. Solicitações corretivas/urgentes

Fluxo básico:

1. colaborador abre solicitação;
2. manutenção recebe alerta;
3. status acompanha o ciclo (`aberta`, `em_andamento`, `finalizada`);
4. interação operação/manutenção ocorre dentro do chamado.

### 4. Calendário de seleção de manutenções

O sistema deve exibir um calendário para seleção e visualização de agendas de manutenção, com:

- visão mensal e semanal;
- filtro por veículo e tipo de manutenção;
- identificação visual por status (`programada`, `em_andamento`, `finalizada`, `atrasada`);
- ação rápida para abrir solicitação urgente em uma data selecionada.

### 5. Alertas automáticos

Tipos de alerta:

- manutenção próxima do prazo;
- km limite atingida;
- solicitação urgente aberta;
- manutenção atrasada.

### 6. Histórico e análise

Por veículo, o sistema deve manter:

- linha do tempo de manutenções;
- peças trocadas;
- custos;
- frequência de problemas.

Indicadores esperados:

- custo por frota;
- frotas com maior índice de manutenção;
- suporte à decisão de substituição de veículo.

## Estrutura inicial do projeto

```text
.
├── README.md
└── docs
    ├── modelo-dados.md
    └── roadmap-mvp.md
```

### 7. Login por pessoa e perfis de acesso

O acesso deve ser individual (um login por pessoa), com ao menos dois perfis:

- `admin`: acesso total ao sistema (configuração, gestão de usuários e visão global);
- `usuario`: acesso operacional (abertura/acompanhamento de solicitações e consulta de calendário/histórico conforme permissão).

## Próximos passos sugeridos

1. implementar API (Node.js + TypeScript + PostgreSQL);
2. construir interface web (React) para operação/manutenção;
3. implementar autenticação com login individual e perfis (`admin`, `usuario`);
4. criar módulo de calendário com filtros e atualização por status;
5. automatizar alertas via jobs agendados;
6. publicar MVP em ambiente cloud com CI/CD.


## Visualização publicada do modelo

Para visualizar uma versão publicada do modelo em HTML, abra `public/index.html` no navegador.

Se quiser publicar no GitHub Pages, configure a branch para servir a pasta `public/`.

## Como ver o sistema (passo a passo)

### Opção 1 — Abrir direto no navegador

1. Entre na pasta do projeto.
2. Abra o arquivo `public/index.html` com duplo clique.

### Opção 2 — Rodar servidor local (recomendado)

No terminal, execute:

```bash
cd /workspace/controle-de-manutencao
python -m http.server 8000 --directory public
```

Depois, abra no navegador:

- `http://localhost:8000`

Para parar o servidor: `Ctrl + C`.


> A página publicada em `public/index.html` foi estilizada no formato de portal corporativo com logo e navegação lateral (estilo Portal Areia Ana).


## Aplicativo pronto para testar

O sistema já está funcional em `public/index.html` com:

- Login por pessoa (`admin` e `usuario`);
- Cadastro de veículos;
- Cadastro de planos de manutenção;
- Abertura e atualização de ordens;
- Calendário de eventos de manutenção;
- Alertas automáticos;
- Histórico consolidado;
- Gestão de usuários (apenas admin).

### Credenciais padrão

- **Admin**: `admin@areiaana.com` / `admin123`
- **Usuário**: `usuario@areiaana.com` / `usuario123`

### Como abrir e testar agora

### Jeito mais fácil (1 clique)

- Dê duplo clique no arquivo **`ABRIR_PORTAL.html`**.
- Ele abre diretamente o portal no estilo Areia Ana.

### Jeito automático por script

```bash
cd /workspace/controle-de-manutencao
python abrir_portal.py
```

O navegador abre automaticamente em `http://localhost:8000`.

### Jeito manual (alternativo)

```bash
cd /workspace/controle-de-manutencao
python -m http.server 8000 --directory public
```

Abra no navegador: `http://localhost:8000`
