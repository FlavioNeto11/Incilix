# 04 — Anexo: Mapa de isoconcentração

**Empreendimento:** INCILIX Incineradora Ltda. — Caieiras/SP  
**Elaboração:** geoprocessamento-mapas  
**Data:** 2026-04-15

---

## 1. Status

> **PRELIMINAR COM ELEMENTOS CARTOGRÁFICOS COMPLETOS**

Não foi localizado arquivo real de saída do modelo AERMOD nem tabela de concentração por receptor em `data/input/aermod-output/concentracoes_receptores.csv`.

Foi gerado mapa preliminar em `outputs/maps/mapa_isoconcentracao.html` para atender aos elementos gráficos exigidos, sem declarar resultado definitivo de modelagem.

Elementos presentes no mapa preliminar:

- localização da fonte emissora;
- pluma de dispersão atmosférica;
- curvas de isoconcentração;
- identificação do receptor crítico;
- área de influência direta (AID);
- base cartográfica com referência espacial.

---

## 2. Justificativa técnica

O mapa de isoconcentração representa a distribuição espacial das concentrações do poluente (dioxinas/furanos em TEQ) calculadas pelo modelo AERMOD para cada ponto receptor da malha. Para gerar mapa definitivo:

- é necessária a saída numérica AERMOD por receptor (arquivo `.OUT` ou equivalente tabular);
- ou a tabela `concentracoes_receptores.csv` com concentração já calculada por ponto;
- os dados devem ser reais, auditáveis e rastreáveis.

Gerar mapa definitivo sem esses dados criaria resultado sem base numérica, violando a regra central do projeto e a rastreabilidade exigida pela CETESB.

---

## 3. Estrutura esperada do arquivo de entrada

Arquivo: `data/input/aermod-output/concentracoes_receptores.csv`

```txt
receptor_id,utm_e,utm_n,concentration,unit,period,pollutant
```

| Coluna | Tipo | Descrição |
|---|---|---|
| `receptor_id` | string | Identificador único do receptor (ex.: `RC-01`, `R001`) |
| `utm_e` | float | Coordenada UTM Este (SIRGAS 2000 / Zona 23S) |
| `utm_n` | float | Coordenada UTM Norte (SIRGAS 2000 / Zona 23S) |
| `concentration` | float | Concentração modelada pelo AERMOD |
| `unit` | string | Unidade: `pg TEQ/m3` ou `ng/Nm3` |
| `period` | string | Período de média: `annual`, `24h`, `1h` |
| `pollutant` | string | Poluente modelado (ex.: `dioxinas_furanos`) |

---

## 4. Critério de avaliação — quando os dados reais forem fornecidos

| Critério | Valor | Base |
|---|---|---|
| Limite de concentração CETESB | 0,14 ng/Nm³ (= 140 pg TEQ/m³) | Resolução SMA / ERSH |
| Critério de risco incremental individual (RII) | ≤ 1 × 10⁻⁵ | CETESB — Protocolo de avaliação de risco |
| Poluente | Dioxinas e furanos (TEQ) | Declarado no ERSH |
| Período de média | Anual | Conforme modelo AERMOD |

**Avaliação:** concentração máxima no receptor crítico (RC-01 ou outro de maior concentração) ÷ limite ≤ 1. Se RII > 1×10⁻⁵, exige análise de risco completa.

---

## 5. Referências e rastreabilidade

- `ESTUDO_DE_RISCO_A_SAUDE_RM_2025.09.11_R00_corrigido_assinado EM ANDAMENTO.pdf`
- `Pt 035 Incilix .pdf`
- `PROMPT_PRINCIPAL_EXECUCAO.md`
- `data/input/aermod-output/concentracoes_receptores.example.csv`

No mapa preliminar, o valor de exemplo (`41 pg TEQ/m3`) foi utilizado apenas para composição visual de classes indicativas, com aviso explícito de que não representa saída oficial do AERMOD.

---

## 6. Entregável cartográfico

- Arquivo: `outputs/maps/mapa_isoconcentracao.html`
- Classificação: **PRELIMINAR / NÃO DEFINITIVO**

---

## 7. Próximos passos

1. Executar o AERMOD com os arquivos AERMET e AERMAP do empreendimento.
2. Exportar saída por receptor para `data/input/aermod-output/concentracoes_receptores.csv`.
3. Reexecutar `python src/pipeline.py` para gerar mapa definitivo com base numérica real.
