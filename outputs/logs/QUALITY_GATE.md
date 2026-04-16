# QUALITY GATE — Auditoria Final CETESB

Data: 2026-04-15  
Projeto: INCILIX Complementação CETESB  
Modo: validador-cetesb

## Classificação Final

**REPROVADO**

## Síntese de auditoria

- Mapa AID 5 km: **ATENDIDO** (`outputs/maps/mapa_aid_receptores.html`).
- Receptores sensíveis: **PARCIAL** (há tabela em `outputs/tables/receptores_sensiveis.csv`, porém sem base completa de campo e com inconsistência de distância do RC-01).
- Isoconcentração: **PARCIAL** (`outputs/maps/mapa_isoconcentracao.html` existe e está funcional, porém explicitamente **preliminar**).
- Saída resumida da modelagem: **ATENDIDO COMO PRELIMINAR** (`outputs/reports/05_saida_resumida_modelagem.md`).
- Memória de cálculo: **PARCIAL** (dioxinas/furanos calculado; MP, SOx, NOx e HCTNM pendentes).
- Plano de emissões (MP, SOx, NOx, HCTNM): **NÃO ATENDIDO** (limites não preenchidos).
- Separação entre dado real e pendente: **ATENDIDO** nos relatórios.

## Pendências impeditivas (bloqueiam protocolo definitivo)

1. **Ausência de dado real AERMOD por receptor (malha completa 100 m x 100 m).**
	- Bloqueia validação definitiva de isoconcentração e cálculo auditável do RII.
	- Evidência: relatórios 01, 04 e 05 classificam saída como ausente/preliminar.

2. **Mapa de isoconcentração não definitivo.**
	- O arquivo existe, mas está identificado como preliminar e não substitui resultado numérico real.
	- Evidência: `outputs/reports/04_anexo_isoconcentracao.md`.

3. **RII CETESB (<= 1x10^-5) sem comprovação com base real de modelagem.**
	- Sem concentração real por receptor, o critério não pode ser concluído tecnicamente.

4. **Plano de emissões incompleto para MP, SOx, NOx e HCTNM.**
	- Limites regulatórios não preenchidos impedem cálculo em kg/h e t/ano.
	- Evidência: `outputs/tables/emissoes_calculadas.csv` (status pendente para esses poluentes).

## Pendências não impeditivas (ajustes recomendados)

1. **Inconsistência do receptor crítico RC-01.**
	- Distância declarada (~1300 m) diverge da distância calculada por UTM (~870 m).
	- Requer validação de coordenadas e atualização documental.

2. **Aprimorar base de receptores sensíveis com levantamento de campo completo.**
	- Arquivo de saída existe, mas recomenda-se completar/confirmar inventário de receptores na AID.

3. **Consolidar pacote de reprodutibilidade da modelagem.**
	- Disponibilizar conjunto final AERMET/AERMAP/AERMOD para rastreio integral em eventual diligência.

## Evidências auditadas

- `outputs/reports/01_diagnostico_lacunas.md`
- `outputs/reports/02_memoria_calculo_emissoes.md`
- `outputs/reports/03_anexo_mapa_aid.md`
- `outputs/reports/04_anexo_isoconcentracao.md`
- `outputs/reports/05_saida_resumida_modelagem.md`
- `outputs/reports/RELATORIO_FINAL_COMPLEMENTACAO.md`
- `outputs/maps/mapa_aid_receptores.html`
- `outputs/maps/mapa_isoconcentracao.html`
- `outputs/tables/emissoes_calculadas.csv`
- `outputs/tables/receptores_sensiveis.csv`

## Decisão do quality gate

**Resultado: REPROVADO** para protocolo definitivo CETESB nesta data.

Condição de mudança para APROVADO COM RESSALVAS ou APROVADO:

- Entregar saída real do AERMOD por receptor e regenerar isoconcentração definitiva.
- Demonstrar verificação do RII com base real.
- Preencher limites de MP, SOx, NOx e HCTNM e recalcular plano de emissões.
