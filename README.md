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

### 4. Alertas automáticos

Tipos de alerta:

- manutenção próxima do prazo;
- km limite atingida;
- solicitação urgente aberta;
- manutenção atrasada.

### 5. Histórico e análise

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

## Próximos passos sugeridos

1. implementar API (Node.js + TypeScript + PostgreSQL);
2. construir interface web (React) para operação/manutenção;
3. configurar autenticação por perfil (`operacao`, `manutencao`, `gestao`);
4. automatizar alertas via jobs agendados;
5. publicar MVP em ambiente cloud com CI/CD.
