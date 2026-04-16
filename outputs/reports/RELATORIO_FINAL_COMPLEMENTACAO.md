# Relatório Final de Complementação — INCILIX / CETESB

**Empreendimento:** INCILIX Incineradora Ltda.  
**Processo CETESB:** Complementação documental — ERSH e Plano de Gestão de Emissões  
**Data de geração:** 2026-04-15  
**Versão:** 1.0 — PRELIMINAR (pendências impeditivas em aberto)  
**Gerado por:** redator-tecnico-final

---

## Dados do Empreendimento

| Campo | Valor |
|---|---|
| Razão Social | INCILIX Incineradora Ltda. |
| Endereço | Rua João Paulo I, nº 315, Parque Industrial Araucária, Caieiras/SP |
| Coordenada UTM E (chaminé) | 324 209,85 m |
| Coordenada UTM N (chaminé) | 7 412 260,54 m |
| Sistema de Referência | SIRGAS 2000 / UTM Zona 23S |
| Latitude (decimal) | −23,38998° S |
| Longitude (decimal) | −46,72014° W |
| Altura da chaminé | 17 m |
| Vazão volumétrica normalizada | 12.000 Nm³/h |
| Temperatura dos gases de saída | 200 °C |
| Velocidade de saída dos gases | 11 m/s |
| Diâmetro equivalente da chaminé | 0,82 m |
| Regime de operação | 20 h/dia × 300 dias/ano = 6.000 h/ano |
| Poluente principal (ERSH) | Dioxinas e Furanos (TEQ) |
| Limite de emissão adotado | 0,14 ng/Nm³ |
| Taxa de emissão calculada | 1,68 µg/h / 4,6667×10⁻¹⁰ g/s |
| Modelo de dispersão citado | AERMOD / AERMET / AERMAP |
| Critério de risco (CETESB) | RII ≤ 1×10⁻⁵ |

---

## Resumo Executivo

O presente relatório consolida a etapa de complementação documental do Estudo de Risco para a Saúde Humana (ERSH) e do Plano de Gestão de Emissões da INCILIX Incineradora Ltda., elaborado em conformidade com as exigências da CETESB. O objetivo da complementação é suprir as lacunas documentais identificadas no processo administrativo e fornecer os anexos técnicos necessários para instrução do protocolo definitivo junto ao órgão licenciador.

No âmbito desta execução, foram gerados os seguintes produtos técnicos: diagnóstico de lacunas documentais (Anexo 1), memória de cálculo de emissões com rastreabilidade de conversão de unidades (Anexo 2), mapa cartográfico da Área de Influência Direta (AID) de 5 km com receptor crítico declarado (Anexo 3), análise do status do mapa de isoconcentração (Anexo 4) e saída resumida dos parâmetros da modelagem atmosférica (Anexo 5). Todos os produtos são rastreáveis às fontes de dado indicadas neste documento.

A memória de cálculo de emissões foi integralmente concluída para dioxinas e furanos, com verificação de consistência entre os valores declarados no estudo (1,68 µg/h; 4,67×10⁻¹⁰ g/s) e os valores recalculados independentemente (divergência de 0,07% — atribuída unicamente a arredondamento). Para os demais poluentes identificados no Plano de Emissões (MP, SOx, NOx e HCTNM), os cálculos permanecem bloqueados pela ausência dos limites regulatórios provenientes do Parecer Técnico 010/25/IAA/IARS.

O mapa de isoconcentração **preliminar** foi gerado nesta execução para fins cartográficos, com identificação de fonte emissora, pluma de dispersão, curvas indicativas, receptor crítico, AID e base cartográfica com referência espacial. Contudo, o cálculo do Risco Incremental Individual (RII) e a isoconcentração **definitiva** permanecem bloqueados, pois os arquivos de saída real do AERMOD por receptor não foram fornecidos. O arquivo de exemplo presente na workspace (`concentracoes_receptores.example.csv`) contém um único receptor com valor fictício (41 pg TEQ/m³) e **não pode ser utilizado para protocolo**. Adicionalmente, identificou-se inconsistência de distância para o receptor crítico RC-01: a distância declarada no estudo (~1.300 m) difere da distância calculada pelas coordenadas UTM (~870 m), demandando verificação prévia antes do protocolo definitivo.

O status atual do processo é **PRELIMINAR**. Existem doze pendências — oito delas com classificação BLOQUEANTE — que impedem o protocolo técnico definitivo. Enquanto esses itens não forem supridos pelo empreendedor ou pelo responsável técnico, o protocolo formal junto à CETESB não deve ser realizado, sob risco de contestação ou exigência de reapresentação.

---

## Anexo 1 — Diagnóstico de Lacunas Documentais

**Empreendimento:** INCILIX Incineradora Ltda. — Caieiras/SP  
**Data de geração:** 2026-04-15  
**Elaborado por:** validador-cetesb (modo auditoria CETESB)

### 1.1 Tabela de Lacunas por Item Regulatório CETESB

| # | Item Regulatório | Status | Tipo de Dado | Ação Necessária |
|---|---|---|---|---|
| 1 | Parâmetros da fonte/chaminé | **DISPONÍVEL** | Real informado | Nenhuma. Altura 17 m, vazão 12.000 Nm³/h, T 200 °C, v 11 m/s, Ø 0,82 m documentados no estudo. |
| 2 | Coordenada da chaminé (UTM) | **DISPONÍVEL** | Real informado | Nenhuma. E 324.209,85 / N 7.412.260,54, SIRGAS 2000, Zona 23S. |
| 3 | Taxa de emissão — dioxinas/furanos | **DISPONÍVEL** | Declarado no estudo | 1,68 µg/h e 4,67×10⁻¹⁰ g/s declarados. Requer confirmação analítica em operação. |
| 4 | Limite de concentração — dioxinas/furanos | **DISPONÍVEL** | Declarado no estudo | 0,14 ng/Nm³ adotado; validar referência normativa CETESB/CONAMA. |
| 5 | Mapa AID 5 km | **GERADO** | Calculado a partir de dado real | Arquivo: `outputs/maps/mapa_aid_receptores.html`. |
| 6 | Receptores sensíveis — tabela real | **PENDENTE** | Arquivo ausente | Fornecer `data/input/receptores/receptores_sensiveis.csv`. O arquivo `.example.csv` contém R002 explicitamente fictício — não utilizável. |
| 7 | Saída AERMOD — concentração por receptor | **BLOQUEANTE** | Arquivo ausente | Fornecer `data/input/aermod-output/concentracoes_receptores.csv` com malha real 100 m × 100 m. |
| 8 | Mapa de isoconcentração definitivo | **BLOQUEANTE** | Dependente do item 7 | Somente gerável após fornecimento da saída AERMOD completa. |
| 9 | Verificação do critério RII CETESB (≤ 1×10⁻⁵) | **BLOQUEANTE** | Dependente do item 7 | RII não calculável sem concentração real. O valor 41 pg TEQ/m³ (exemplo) não pode ser usado para protocolo. |
| 10 | Meteorologia (AERMET) | **PENDENTE** | Arquivo ausente | Fornecer série meteorológica processada em `data/input/meteorologia/`. |
| 11 | Topografia (AERMAP) | **PENDENTE** | Arquivo ausente | Fornecer DEM processado em `data/input/topografia/`. |
| 12 | Saída resumida da modelagem atmosférica | **PENDENTE** | Dependente dos itens 10 e 11 | Estrutura gerada; conteúdo real depende de AERMOD, AERMET e AERMAP. |
| 13 | Limites regulatórios — MP | **BLOQUEANTE** | Arquivo incompleto | Preencher em `data/input/limites-emissao/limites.csv`. Fonte: Parecer Técnico 010/25/IAA/IARS. |
| 14 | Limites regulatórios — SOx | **BLOQUEANTE** | Arquivo incompleto | Idem item 13. |
| 15 | Limites regulatórios — NOx | **BLOQUEANTE** | Arquivo incompleto | Idem item 13. |
| 16 | Limites regulatórios — HCTNM | **BLOQUEANTE** | Arquivo incompleto | Idem item 13. |
| 17 | Memória de cálculo — MP, SOx, NOx, HCTNM | **BLOQUEANTE** | Dependente dos itens 13–16 | Plano de Emissões bloqueado sem os limites regulatórios. |
| 18 | Receptor crítico declarado (RC-01) | **INCONSISTENTE** | Declarado no estudo | Distância calculada (~870 m) diverge da declarada (~1.300 m). Verificar coordenadas antes do protocolo. |

### 1.2 Risco Técnico de Protocolar sem Dado Real

| Risco | Severidade | Descrição |
|---|---|---|
| Isoconcentração sem saída AERMOD real | **CRÍTICO** | Inconsistência documental grave perante CETESB. |
| RII calculado com dado de exemplo | **CRÍTICO** | Resultado de RII baseado em R001 (41 pg TEQ/m³ de exemplo) pode ser contestado. |
| Plano de Emissões sem limites preenchidos | **ALTO** | MP, SOx, NOx e HCTNM bloqueados sem Parecer Técnico 010/25/IAA/IARS. |
| Receptores sensíveis fictícios | **ALTO** | R002 do arquivo exemplo é explicitamente fictício — inaceitável para CETESB. |
| Inconsistência de distância RC-01 | **MÉDIO** | Diferença de ~430 m entre distância declarada e calculada afeta avaliação de exposição. |
| Meteorologia e topografia ausentes | **MÉDIO** | Sem AERMET e AERMAP não é possível reproduzir nem validar a modelagem. |

### 1.3 Separação: Dado Real × Pendente

| Categoria | Itens |
|---|---|
| **Dados reais informados** | Parâmetros da chaminé, coordenada UTM da fonte, taxa dioxinas/furanos declarada, limite 0,14 ng/Nm³, coordenada RC-01 (declarada). |
| **Dados calculados** | Mapa AID 5 km, conversão de unidades dioxinas/furanos, taxas em µg/h, g/s, kg/h, t/ano. |
| **Dados pendentes** | Receptores sensíveis reais, meteorologia AERMET, topografia AERMAP, saída AERMOD completa. |
| **Dados bloqueantes** | Limites MP/SOx/NOx/HCTNM (em branco), concentração AERMOD por receptor (malha completa), RII definitivo. |
| **Resultados declarados (não verificados)** | Concentração no RC-01 (único ponto, arquivo exemplo), RII implícito no estudo. |
| **Resultados reais de modelo** | **Ausentes.** Nenhum arquivo AERMOD oficial foi fornecido. |

---

## Anexo 2 — Memória de Cálculo de Emissões

**Empreendimento:** INCILIX Incineradora Ltda. — Caieiras/SP  
**Data de geração:** 2026-04-15  
**Status geral:** PARCIALMENTE CALCULADO — limites de MP, SOx, NOx e HCTNM pendentes

### 2.1 Dioxinas e Furanos — Dados de entrada

| Parâmetro | Valor | Unidade | Status |
|---|---:|---|---|
| Limite de emissão adotado | 0,14 | ng/Nm³ | dado real informado |
| Vazão volumétrica normalizada | 12.000 | Nm³/h | dado real informado |
| Taxa declarada no estudo | 1,68 | µg/h | resultado declarado no estudo |
| Taxa declarada no estudo | 4,67×10⁻¹⁰ | g/s | resultado declarado no estudo |

### 2.2 Sequência de conversão (ng/Nm³ → µg/h → g/s → kg/h → t/ano)

**Etapa 1 — Concentração → Fluxo mássico em ng/h:**

```
Q_ng_h = 0,14 × 12.000 = 1.680 ng/h
```

**Etapa 2 — ng/h → µg/h** (fator: 1 µg = 1.000 ng):

```
Q_ug_h = 1.680 ÷ 1.000 = 1,68 µg/h
```

**Etapa 3 — µg/h → g/s** (fator: 1 g = 10⁶ µg; 1 h = 3.600 s):

```
Q_g_s = 1,68 × 10⁻⁶ ÷ 3.600 = 4,6667×10⁻¹⁰ g/s
```

**Etapa 4 — g/s → kg/h:**

```
Q_kg_h = 4,6667×10⁻¹⁰ × 3.600 ÷ 1.000 = 1,68×10⁻⁹ kg/h
```

**Etapa 5 — kg/h → t/ano** (6.000 h/ano):

```
Q_t_ano = 1,68×10⁻⁹ × 6.000 ÷ 1.000 = 1,008×10⁻⁸ t/ano
```

### 2.3 Verificação de consistência

| | Taxa calculada | Taxa declarada | Divergência |
|---|---|---|---|
| µg/h | **1,68 µg/h** | 1,68 µg/h | 0,00% — **consistente** |
| g/s | **4,6667×10⁻¹⁰ g/s** | 4,67×10⁻¹⁰ g/s | 0,07% — atribuído a arredondamento |

Conclusão: Sem erro de unidade ou de conversão. Os valores são fisicamente coerentes entre si.

### 2.4 Tabela consolidada de emissões

| Poluente | Limite | Unidade | µg/h | g/s | kg/h | t/ano | Status |
|---|---:|---|---:|---:|---:|---:|---|
| Dioxinas e Furanos | 0,14 | ng/Nm³ | 1,68 | 4,667×10⁻¹⁰ | 1,68×10⁻⁹ | 1,008×10⁻⁸ | **calculado** |
| MP | PENDENTE | mg/Nm³ | — | — | — | — | **pendente** |
| SOx | PENDENTE | mg/Nm³ | — | — | — | — | **pendente** |
| NOx | PENDENTE | mg/Nm³ | — | — | — | — | **pendente** |
| HCTNM | PENDENTE | mg/Nm³ | — | — | — | — | **pendente** |

> **Arquivo esperado para desbloqueio:** `data/input/limites-emissao/limites.csv` (Parecer Técnico 010/25/IAA/IARS)

### 2.5 Rastreabilidade

| Item | Origem | Status |
|---|---|---|
| Limite dioxinas/furanos (0,14 ng/Nm³) | PROMPT_PRINCIPAL_EXECUCAO.md | dado real informado |
| Vazão (12.000 Nm³/h) | PROMPT_PRINCIPAL_EXECUCAO.md | dado real informado |
| Taxa 1,68 µg/h e 4,6667×10⁻¹⁰ g/s | Calculado nesta memória | calculado |
| Taxa 4,67×10⁻¹⁰ g/s | PROMPT_PRINCIPAL_EXECUCAO.md | resultado declarado no estudo |
| Limites MP, SOx, NOx, HCTNM | limites.example.csv | **pendente** |
| Concentração R001 (41 pg TEQ/m³) | concentracoes_receptores.example.csv | arquivo de exemplo — **não é resultado real** |

---

## Anexo 3 — Mapa da AID e Receptores Sensíveis

**Empreendimento:** INCILIX Incineradora Ltda. — Caieiras/SP  
**Datum:** SIRGAS 2000 / UTM Zona 23S  
**Data:** 2026-04-15

### 3.1 Localização da fonte

| Campo | Valor |
|---|---|
| UTM E | 324 209,85 m |
| UTM N | 7 412 260,54 m |
| Zona | 23S — SIRGAS 2000 |
| Latitude (decimal) | −23,38998° S |
| Longitude (decimal) | −46,72014° W |
| Latitude (g/m/s) | 23° 23′ 24″ S |
| Longitude (g/m/s) | 46° 43′ 13″ W |

### 3.2 Produto cartográfico

| Campo | Valor |
|---|---|
| Arquivo gerado | `outputs/maps/mapa_aid_receptores.html` |
| Tecnologia | Leaflet.js (OpenStreetMap) |
| Status | **GERADO — funcional** |
| Raio da AID | 5.000 m |
| Raios auxiliares | 100 m, 200 m, 1 km, 3 km |

### 3.3 Receptor crítico declarado

| Campo | Valor |
|---|---|
| ID | RC-01 |
| Descrição | Unidade de saúde / área institucional |
| UTM E | 324 800 m |
| UTM N | 7 412 900 m |
| Distância declarada (estudo) | ~1.300 m |
| Distância calculada (UTM) | ~870 m |
| Fonte | Declarado em PROMPT_PRINCIPAL_EXECUCAO.md |

> **⚠ Inconsistência detectada:** A distância calculada (~870 m) diverge da distância declarada (~1.300 m). Verificar coordenadas antes do protocolo definitivo.

### 3.4 Tabela de receptores sensíveis

| id | nome | tipo | utm_e | utm_n | distancia_fonte_m | fonte_dado | observacao |
|---|---|---|---|---|---|---|---|
| RC-01 | Unidade de saúde/área institucional (declarado no estudo) | saude | 324.800 | 7.412.900 | 1.300 (declarado) / ~870 (calculado) | declarado_no_estudo | Verificar coordenadas antes do protocolo definitivo |

> **Arquivo de campo ausente:** `data/input/receptores/receptores_sensiveis.csv` — levantamento real obrigatório para protocolo.

---

## Anexo 4 — Isoconcentração

**Empreendimento:** INCILIX Incineradora Ltda. — Caieiras/SP  
**Data:** 2026-04-15

### 4.1 Status

> **PRELIMINAR COM ELEMENTOS CARTOGRÁFICOS COMPLETOS**

Não foi localizado arquivo real de saída do modelo AERMOD em `data/input/aermod-output/concentracoes_receptores.csv`. O mapa definitivo de isoconcentração não pode ser elaborado sem resultado numérico auditável por receptor.

Mapa preliminar disponível em `outputs/maps/mapa_isoconcentracao.html`.

### 4.2 Justificativa técnica

O mapa de isoconcentração representa a distribuição espacial das concentrações de dioxinas/furanos (TEQ) calculadas pelo AERMOD para cada ponto receptor da malha de 100 m. Sua geração exige saída numérica AERMOD por receptor real, auditável e rastreável — nunca estimada ou extrapolada de exemplo único.

### 4.3 Critérios de avaliação (a aplicar quando os dados forem fornecidos)

| Critério | Valor | Base |
|---|---|---|
| Limite de concentração CETESB | 0,14 ng/Nm³ (= 140 pg TEQ/m³) | Resolução SMA / ERSH |
| RII (Risco Incremental Individual) | ≤ 1×10⁻⁵ | CETESB — protocolo de avaliação de risco |
| Poluente | Dioxinas e furanos (TEQ) | Declarado no ERSH |
| Período de média | Anual | Conforme AERMOD |

### 4.4 Estrutura esperada do arquivo de entrada

Arquivo: `data/input/aermod-output/concentracoes_receptores.csv`

| Coluna | Tipo | Descrição |
|---|---|---|
| `receptor_id` | string | Identificador único do receptor |
| `utm_e` | float | Coordenada UTM Este (SIRGAS 2000 / Zona 23S) |
| `utm_n` | float | Coordenada UTM Norte (SIRGAS 2000 / Zona 23S) |
| `concentration` | float | Concentração modelada pelo AERMOD |
| `unit` | string | `pg TEQ/m3` ou `ng/Nm3` |
| `period` | string | `annual`, `24h` ou `1h` |
| `pollutant` | string | Poluente modelado |

### 4.5 Dado de exemplo na workspace

O arquivo `data/input/aermod-output/concentracoes_receptores.example.csv` contém dado de exemplo não auditável (41 pg TEQ/m³ em RC-01), inserido apenas para ilustrar o formato. **Não foi utilizado** e **não pode ser adotado para protocolo**.

---

## Anexo 5 — Saída Resumida da Modelagem Atmosférica

**Empreendimento:** INCILIX Incineradora Ltda. — Caieiras/SP  
**Data de geração:** 2026-04-15  
**Status:** **PRELIMINAR** — ausência de arquivos reais de entrada e saída do AERMOD

### 5.1 Modelo e pré-processadores

| Componente | Nome | Status |
|---|---|---|
| Modelo de dispersão | AERMOD | citado no estudo — arquivos ausentes |
| Pré-processador meteorológico | AERMET | citado no estudo — arquivos ausentes |
| Tratamento topográfico | AERMAP | citado no estudo — arquivos ausentes |

### 5.2 Parâmetros da fonte modelada

| Parâmetro | Valor | Unidade | Status |
|---|---:|---|---|
| Tipo de fonte | Pontual/chaminé | — | dado real informado |
| Coordenada UTM E | 324.209,85 | m | dado real informado |
| Coordenada UTM N | 7.412.260,54 | m | dado real informado |
| Sistema de referência | SIRGAS 2000 / UTM Zona 23S | — | dado real informado |
| Altura da chaminé | 17 | m | dado real informado |
| Vazão volumétrica | 12.000 | Nm³/h | dado real informado |
| Temperatura dos gases | 200 | °C | dado real informado |
| Velocidade de saída | 11 | m/s | dado real informado |
| Diâmetro equivalente | 0,82 | m | dado real informado |
| Operação diária | 20 | h/dia | dado real informado |
| Operação anual | 300 | dias/ano | dado real informado |
| Horas anuais de operação | 6.000 | h/ano | calculado |
| Poluente ERSH principal | Dioxinas e Furanos (TEQ) | — | dado real informado |
| Limite de emissão adotado | 0,14 | ng/Nm³ | dado real informado |
| Taxa declarada | 1,68 | µg/h | resultado declarado no estudo |
| Taxa declarada | 4,67×10⁻¹⁰ | g/s | resultado declarado no estudo |

### 5.3 Malha receptora

| Parâmetro | Valor | Status |
|---|---|---|
| Raio AID | 5.000 m | dado real informado |
| Espaçamento da malha | 100 m | dado real informado |
| Altura dos receptores | 1,5 m | dado real informado |
| Receptor crítico declarado | UTM E 324.800 / N 7.412.900 (~1.300 m declarados; ~870 m calculados) | resultado declarado — inconsistente |
| Tipo do receptor crítico | Unidade de saúde / área institucional | dado real informado |
| Critério CETESB (RII) | ≤ 1×10⁻⁵ | dado real informado |

### 5.4 Meteorologia e Topografia

| Item | Caminho esperado | Status |
|---|---|---|
| Arquivos AERMET (.SFC, .PFL) | `data/input/meteorologia/` | **PENDENTE — diretório vazio** |
| Arquivo AERMAP / DEM (.TER) | `data/input/topografia/` | **PENDENTE — diretório vazio** |

### 5.5 Status final da modelagem

**PRELIMINAR** — a saída será classificada como DEFINITIVA após fornecimento de:

1. Arquivos de saída do AERMOD (`.out`, `.plt` ou `.txt`) com concentrações por receptor
2. `data/input/aermod-output/concentracoes_receptores.csv` (tabela real)
3. Arquivos meteorológicos (AERMET) em `data/input/meteorologia/`
4. Arquivo topográfico (AERMAP) em `data/input/topografia/`
5. `data/input/receptores/receptores_sensiveis.csv` com coordenadas reais verificadas
6. `data/input/limites-emissao/limites.csv` com limites para MP, SOx, NOx e HCTNM

---

## Pendências Impeditivas para Protocolo

1. **Saída AERMOD — concentração por receptor (malha completa):** Ausência de `data/input/aermod-output/concentracoes_receptores.csv` com dados reais. *Responsável: responsável técnico da modelagem atmosférica.*

2. **Mapa de isoconcentração definitivo:** Bloqueado pela pendência 1. Foi gerado somente produto cartográfico preliminar, sem base numérica oficial do AERMOD. *Responsável: responsável técnico da modelagem atmosférica.*

3. **Cálculo do RII (Risco Incremental Individual):** Bloqueado pela pendência 1. Critério CETESB (RII ≤ 1×10⁻⁵) não verificável sem concentração real. *Responsável: responsável técnico da modelagem atmosférica.*

4. **Limite regulatório de MP (mg/Nm³):** Campo em branco em `data/input/limites-emissao/limites.csv`. Fonte: Parecer Técnico 010/25/IAA/IARS. *Responsável: empreendedor / assessoria jurídica.*

5. **Limite regulatório de SOx (mg/Nm³):** Idem pendência 4. *Responsável: empreendedor / assessoria jurídica.*

6. **Limite regulatório de NOx (mg/Nm³):** Idem pendência 4. *Responsável: empreendedor / assessoria jurídica.*

7. **Limite regulatório de HCTNM (mg/Nm³):** Idem pendência 4. *Responsável: empreendedor / assessoria jurídica.*

8. **Taxas de emissão de MP, SOx, NOx e HCTNM (kg/h e t/ano):** Bloqueadas pelas pendências 4–7. Plano de Emissões incompleto. *Responsável: empreendedor / responsável técnico.*

9. **Receptores sensíveis reais (levantamento de campo):** Ausência de `data/input/receptores/receptores_sensiveis.csv`. Arquivo de exemplo contém receptor fictício — não utilizável. *Responsável: empreendedor / equipe de campo.*

10. **Inconsistência de distância RC-01:** Distância declarada (~1.300 m) ≠ distância calculada pelas coordenadas UTM (~870 m). *Responsável: responsável técnico do ERSH.*

11. **Meteorologia AERMET:** Diretório `data/input/meteorologia/` vazio. *Responsável: responsável técnico da modelagem atmosférica.*

12. **Topografia AERMAP:** Diretório `data/input/topografia/` vazio. *Responsável: responsável técnico da modelagem atmosférica.*

---

## Próximos Passos

| Ação | Arquivo a fornecer | Caminho esperado | Responsável |
|---|---|---|---|
| Fornecer saída real do AERMOD | `concentracoes_receptores.csv` | `data/input/aermod-output/` | Resp. técnico da modelagem |
| Preencher limites de emissão | `limites.csv` | `data/input/limites-emissao/` | Empreendedor / assessoria (Parecer 010/25/IAA/IARS) |
| Levantar receptores sensíveis em campo | `receptores_sensiveis.csv` | `data/input/receptores/` | Equipe de campo / resp. técnico |
| Verificar coordenadas UTM do RC-01 | Correção no ERSH / PROMPT | — | Resp. técnico do ERSH |
| Fornecer arquivos AERMET | Arquivos `.SFC`, `.PFL` | `data/input/meteorologia/` | Resp. técnico da modelagem |
| Fornecer arquivo AERMAP/DEM | Arquivo `.TER` ou DEM raster | `data/input/topografia/` | Resp. técnico da modelagem |
| Re-executar pipeline após fornecimento | — | `python src/pipeline.py` | Equipe técnica INCILIX |
| Emitir relatório versão definitiva | Relatório final revisado | `outputs/reports/RELATORIO_FINAL_COMPLEMENTACAO.md` | Orquestrador / resp. técnico |

---

*Relatório gerado automaticamente pelo pipeline INCILIX — versão PRELIMINAR. Todas as seções marcadas como PENDENTE ou BLOQUEANTE requerem ação do empreendedor ou responsável técnico antes do protocolo definitivo junto à CETESB.*
