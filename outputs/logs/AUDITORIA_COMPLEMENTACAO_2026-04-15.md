# AUDITORIA CETESB — Complementacao Documental

Data: 2026-04-15
Projeto: INCILIX Complementacao CETESB
Modo: validador-cetesb

## Classificacao

REPROVADO

## Escopo auditado

- Mapa AID 5 km
- Receptores sensiveis
- Isoconcentracao
- Saida resumida da modelagem
- Memoria de calculo
- Plano de emissoes (MP, SOx, NOx, HCTNM)
- Separacao entre dado real e dado pendente

## Conclusoes por item

1. Mapa AID 5 km: ATENDIDO
2. Receptores sensiveis: PARCIAL
3. Isoconcentracao: PARCIAL (preliminar, nao definitiva)
4. Saida resumida da modelagem: PARCIAL (preliminar)
5. Memoria de calculo: PARCIAL (dioxinas/furanos, MP, SOx e NOx fechados; HCTNM pendente)
6. Plano de emissoes MP/SOx/NOx/HCTNM: PARCIAL
7. Separacao real x pendente: ATENDIDO

## Nao conformidades impeditivas

1. Ausencia de concentracao AERMOD real por receptor em malha completa.
2. Mapa de isoconcentracao sem base numerica oficial do modelo (status preliminar).
3. Criterio RII CETESB sem comprovacao com dado real.
4. Limite de HCTNM sem base normativa consolidada, bloqueando fechamento integral do plano de emissoes.

## Nao conformidades relevantes

1. Inconsistencia do RC-01: distancia declarada (~1300 m) diverge da calculada (~870 m).
2. Base de receptores sensiveis sem levantamento de campo completo.
3. Ausencia de meteorologia AERMET e topografia AERMAP para reprodutibilidade.

## Exigencias para mudanca de classificacao

1. Entregar `data/input/aermod-output/concentracoes_receptores.csv` com dados reais da malha.
2. Regenerar mapa de isoconcentracao definitivo com saida oficial do modelo.
3. Demonstrar verificacao do RII com base real e rastreavel.
4. Consolidar limite normativo de HCTNM em `data/input/limites-emissao/limites.csv`.
5. Recalcular plano de emissoes completo (kg/h e t/ano) incluindo HCTNM.
6. Validar coordenadas do RC-01 e corrigir distancia no dossie final.

## Decisao

Protocolo definitivo CETESB nao recomendado nesta data.
