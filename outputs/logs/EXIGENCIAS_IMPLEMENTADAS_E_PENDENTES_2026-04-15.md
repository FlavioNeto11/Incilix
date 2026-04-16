# EXIGENCIAS CETESB — Implementacao e pendencias

Data: 2026-04-15

## Implementado nesta execucao

1. Criado `data/input/limites-emissao/limites.csv` com:
   - MP = 50 mg/Nm3
   - SOx = 250 mg/Nm3
   - NOx = 400 mg/Nm3
   - HCTNM = pendente (sem base normativa consolidada)
2. Criado `data/input/receptores/receptores_sensiveis.csv` com RC-01 declarado no estudo.
3. Recalculada `outputs/tables/emissoes_calculadas.csv`:
   - MP, SOx e NOx calculados (kg/h e t/ano)
   - HCTNM mantido como pendente_limite
4. Atualizados os registros de auditoria e quality gate para refletir implementacao parcial real.

## Pendencias que ainda impedem status 100%

1. Ausencia de `data/input/aermod-output/concentracoes_receptores.csv` com saida real da malha completa.
2. Isoconcentracao definitiva bloqueada sem base numerica oficial.
3. RII CETESB sem comprovacao com dado real de modelagem.
4. HCTNM sem limite normativo consolidado para fechamento integral do plano de emissoes.

## Observacao tecnica

Sem os dados reais acima, o protocolo definitivo permanece tecnicamente nao recomendavel nesta data.
