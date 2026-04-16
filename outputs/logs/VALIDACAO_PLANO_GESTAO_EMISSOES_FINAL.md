# VALIDACAO TECNICA — PLANO DE GESTAO DE EMISSOES FINAL

Data: 2026-04-15  
Documento avaliado: PLANO DE GESTAO DE EMISSOES FINAL.pdf  
Base de evidencia textual: outputs/logs/PLANO_GESTAO_EMISSOES_FINAL_EXTRAIDO.txt

## Resultado

APROVADO COM RESSALVAS (documento de plano de emissao tecnicamente estruturado, com pendencias de consistencia para protocolo definitivo sem diligencia).

## Itens conformes

1. Metodologia de conversao de limite (mg/Nm3) para emissao (kg/h) esta correta.
- Evidencia: Emissao (kg/h) = limite x vazao / 1.000.000 em outputs/logs/PLANO_GESTAO_EMISSOES_FINAL_EXTRAIDO.txt:914.

2. Regime operacional anual adotado para t/ano esta coerente com 20 h/dia e 300 dias/ano.
- Evidencia: outputs/logs/PLANO_GESTAO_EMISSOES_FINAL_EXTRAIDO.txt:915.

3. Vazao de referencia utilizada (12.000 Nm3/h) esta explicita e alinhada ao estudo-base.
- Evidencia: outputs/logs/PLANO_GESTAO_EMISSOES_FINAL_EXTRAIDO.txt:917.

4. Quadro de estimativas de emissao apresenta MP, SOx e NOx com valores fechados em kg/h e t/ano.
- Evidencia: outputs/logs/PLANO_GESTAO_EMISSOES_FINAL_EXTRAIDO.txt:925.
- Evidencia: outputs/logs/PLANO_GESTAO_EMISSOES_FINAL_EXTRAIDO.txt:926.
- Evidencia: outputs/logs/PLANO_GESTAO_EMISSOES_FINAL_EXTRAIDO.txt:927.
- Evidencia: outputs/logs/PLANO_GESTAO_EMISSOES_FINAL_EXTRAIDO.txt:928.

5. Limites regulatorios listados incluem Dioxinas/Furanos < 0,14 ng/Nm3 e classes de metais.
- Evidencia: outputs/logs/PLANO_GESTAO_EMISSOES_FINAL_EXTRAIDO.txt:1153.
- Evidencia: outputs/logs/PLANO_GESTAO_EMISSOES_FINAL_EXTRAIDO.txt:1155.
- Evidencia: outputs/logs/PLANO_GESTAO_EMISSOES_FINAL_EXTRAIDO.txt:1156.
- Evidencia: outputs/logs/PLANO_GESTAO_EMISSOES_FINAL_EXTRAIDO.txt:1157.

## Ressalvas e nao conformidades

1. ALTA — HCT/HCTNM sem limite regulatorio explicito no quadro principal.
- O quadro de estimativa apresenta HCT com limite "—" e emissao estimada (0,50 kg/h; 3,00 t/ano), sem demonstrar base normativa numerica.
- Evidencia: outputs/logs/PLANO_GESTAO_EMISSOES_FINAL_EXTRAIDO.txt:929.
- Risco: fragilidade de auditabilidade perante CETESB para parametro de hidrocarbonetos.

2. ALTA — Inconsistencia com a base de calculo do pipeline atual (arquivo oficial de trabalho ainda indica MP/SOx/NOx/HCTNM como pendente).
- Evidencia: outputs/tables/emissoes_calculadas.csv:3.
- Evidencia: outputs/tables/emissoes_calculadas.csv:4.
- Evidencia: outputs/tables/emissoes_calculadas.csv:5.
- Evidencia: outputs/tables/emissoes_calculadas.csv:6.
- Risco: protocolo com documentos divergentes no mesmo processo.

3. MEDIA — Tabela de "Composto Interesse / Taxa de Alimentacao" usa unidade kg/h para "Dioxinas e furanos" com valor 8,0, o que exige esclarecimento de escopo (alimentacao de teste x emissao de chamine).
- Evidencia: outputs/logs/PLANO_GESTAO_EMISSOES_FINAL_EXTRAIDO.txt:1216.
- Risco: interpretacao equivocada por auditor como taxa de emissao.

4. MEDIA — Documento nao apresenta modelagem de dispersao (AERMOD/AERMET/AERMAP) nem validacao de RII.
- Observacao: para Plano de Gestao de Emissoes isso pode ser escopo externo, mas para fechamento global do protocolo CETESB segue pendencia no processo.
- Evidencia indireta: ausencia de ocorrencias de AERMOD/AERMET/AERMAP/RII na extracao textual.

## Recomendacoes objetivas (antes do protocolo)

1. Inserir base normativa numerica para HCTNM (ou retirar estimativa e marcar como pendente formal), com referencia do Parecer Tecnico aplicavel.
2. Harmonizar os arquivos de trabalho do processo: atualizar limites em data/input/limites-emissao/limites.csv e recalcular outputs/tables/emissoes_calculadas.csv para eliminar divergencias.
3. Rotular explicitamente a tabela de "Taxa de Alimentacao" como ensaio de queima (nao emissao de chamine), com nota de nao comparabilidade direta com limites de emissao.
4. Manter o Plano como anexo de emissao e preservar em documento separado a validacao de dispersao/RII para fechamento regulatorio final.

## Decisao tecnica desta validacao

- Documento de Plano: APROVADO COM RESSALVAS.
- Uso para protocolo definitivo sem ajustes: NAO RECOMENDADO.
