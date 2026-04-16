# 01 — Diagnóstico de Lacunas Documentais

**Empreendimento:** INCILIX Incineradora Ltda.
**Endereço:** Rua João Paulo I, nº 315, Parque Industrial Araucária, Caieiras/SP
**Data de geração:** 2026-04-15
**Gerado por:** validador-cetesb (modo auditoria CETESB)

---

## 1. Tabela de Lacunas por Item Regulatório CETESB

| # | Item Regulatório | Status | Tipo de Dado | Ação Necessária |
|---|---|---|---|---|
| 1 | Parâmetros da fonte/chaminé | **DISPONÍVEL** | Real informado | Nenhuma. Altura 17 m, vazão 12.000 Nm³/h, T 200 °C, v 11 m/s, Ø 0,82 m documentados no estudo. |
| 2 | Coordenada da chaminé (UTM) | **DISPONÍVEL** | Real informado | Nenhuma. E 324209.85 / N 7412260.54, SIRGAS 2000, Zona 23S. |
| 3 | Taxa de emissão — dioxinas/furanos | **DISPONÍVEL** | Declarado no estudo | Nenhuma. 1,68 µg/h e 4,67×10⁻¹⁰ g/s declarados. Requer confirmação analítica em operação. |
| 4 | Limite de concentração — dioxinas/furanos | **DISPONÍVEL** | Declarado no estudo | Nenhuma. 0,14 ng/Nm³ adotado; validar referência normativa CETESB/CONAMA. |
| 5 | Mapa AID 5 km | **CALCULÁVEL** | Calculado a partir de dado real | Gerar com coordenada da chaminé. Arquivo de saída: `outputs/maps/mapa_aid_receptores.html`. |
| 6 | Receptores sensíveis — tabela real | **PENDENTE** | Arquivo ausente | Fornecer `data/input/receptores/receptores_sensiveis.csv` com levantamento de campo real. O arquivo `.example.csv` existente contém R001 (declarado no estudo) e R002 explicitamente marcado como exemplo fictício — **não utilizável**. |
| 7 | Saída AERMOD — concentração por receptor | **BLOQUEANTE** | Arquivo ausente | Fornecer `data/input/aermod-output/concentracoes_receptores.csv` com saída real da modelagem para toda a malha 100 m × 100 m. O arquivo `.example.csv` contém apenas 1 receptor (R001, 41 pg TEQ/m³, anual) — insuficiente para isoconcentração e RII. |
| 8 | Mapa de isoconcentração definitivo | **BLOQUEANTE** | Dependente de item 7 | Somente gerável após fornecimento da saída AERMOD completa. Gerar mapa preliminar/template enquanto ausente. |
| 9 | Verificação do critério RII CETESB (≤ 1×10⁻⁵) | **BLOQUEANTE** | Dependente de item 7 | RII não pode ser calculado sem concentração real por receptor. O valor de 41 pg TEQ/m³ de R001 é dado de exemplo — **não pode ser usado para protocolo**. |
| 10 | Meteorologia (AERMET) | **PENDENTE** | Arquivo ausente | Fornecer série meteorológica processada em `data/input/meteorologia/`. Pasta existe e está vazia. |
| 11 | Topografia (AERMAP) | **PENDENTE** | Arquivo ausente | Fornecer arquivo DEM/topografia processada em `data/input/topografia/`. Pasta existe e está vazia. |
| 12 | Saída resumida da modelagem atmosférica | **PENDENTE** | Dependente de itens 10 e 11 | Estrutura gerável; conteúdo real depende dos arquivos AERMOD (`.inp`, `.out`), AERMET e AERMAP. |
| 13 | Limites regulatórios — MP | **BLOQUEANTE** | Arquivo incompleto | Preencher valor em `data/input/limites-emissao/limites.csv`. Campo em branco no `.example.csv`. Fonte: Parecer Técnico 010/25/IAA/IARS. |
| 14 | Limites regulatórios — SOx | **BLOQUEANTE** | Arquivo incompleto | Idem item 13. |
| 15 | Limites regulatórios — NOx | **BLOQUEANTE** | Arquivo incompleto | Idem item 13. |
| 16 | Limites regulatórios — HCTNM | **BLOQUEANTE** | Arquivo incompleto | Idem item 13. |
| 17 | Memória de cálculo — MP, SOx, NOx, HCTNM (kg/h e t/ano) | **BLOQUEANTE** | Dependente de itens 13–16 | Cálculos do Plano de Emissões não podem ser realizados sem os limites regulatórios preenchidos. |
| 18 | Receptor crítico declarado (R001, ~1.300 m) | **DISPONÍVEL** | Declarado no estudo | UTM E 324800 / N 7412900 documentado. Concentração de referência apenas de exemplo — confirmar com saída AERMOD real. |

---

## 2. Risco Técnico de Protocolar sem Dado Real

| Risco | Severidade | Descrição |
|---|---|---|
| Isoconcentração sem saída AERMOD real | **CRÍTICO** | Protocolar mapa de isoconcentração baseado em único receptor de exemplo configura inconsistência documental grave perante CETESB. |
| RII calculado com dado de exemplo | **CRÍTICO** | Resultado de RII baseado em R001 (41 pg TEQ/m³ de exemplo) não representa a malha completa e pode ser contestado na análise técnica. |
| Plano de Emissões sem limites preenchidos | **ALTO** | MP, SOx, NOx e HCTNM não podem ser calculados em kg/h e t/ano sem os valores do Parecer Técnico 010/25/IAA/IARS. |
| Receptores sensíveis fictícios | **ALTO** | R002 do arquivo exemplo é explicitamente fictício. Protocolar sem levantamento de campo real é inaceitável para CETESB. |
| Meteorologia e topografia ausentes | **MÉDIO** | Sem AERMET e AERMAP não é possível reproduzir nem validar a modelagem atmosférica. |

---

## 3. Lista de Arquivos que o Usuário Deve Fornecer

Os arquivos abaixo são **obrigatórios** para fechar o protocolo tecnicamente. Nenhum dado será inventado na ausência deles.

| Prioridade | Arquivo Esperado | Conteúdo Mínimo Exigido |
|---|---|---|
| 🔴 P1 | `data/input/aermod-output/concentracoes_receptores.csv` | Saída real do AERMOD: receptor_id, utm_e, utm_n, concentration (pg TEQ/m³), period=annual, pollutant=dioxinas_furanos — **malha completa 100 m** |
| 🔴 P1 | `data/input/limites-emissao/limites.csv` | Valores preenchidos de MP, SOx, NOx e HCTNM em mg/Nm³ conforme Parecer Técnico 010/25/IAA/IARS |
| 🔴 P1 | `data/input/receptores/receptores_sensiveis.csv` | Levantamento real de receptores sensíveis com id, nome, tipo, utm_e, utm_n, fonte_dado — **sem dados fictícios** |
| 🟡 P2 | `data/input/meteorologia/` | Arquivos AERMET processados (série horária) para o município de Caieiras/SP ou estação representativa |
| 🟡 P2 | `data/input/topografia/` | Arquivo DEM/AERMAP processado para a AID de 5 km centrada na chaminé |
| 🟡 P2 | Arquivos AERMOD originais (`.inp`, `.out`) | Para reprodutibilidade e saída resumida da modelagem |

> **Nota:** Os arquivos `.example.csv` existentes são modelos de estrutura. Não devem ser renomeados diretamente — os dados reais devem ser inseridos em novos arquivos sem o sufixo `.example`.

---

## 4. Separação: Dado Real × Pendente

| Categoria | Itens |
|---|---|
| **Dados reais informados** | Parâmetros da chaminé, coordenada UTM, taxa dioxinas/furanos declarada, limite 0,14 ng/Nm³, receptor crítico R001 (coordenada declarada). |
| **Dados calculáveis** | Mapa AID 5 km, validação de unidades (ng/Nm³ → g/s), memória de cálculo de dioxinas/furanos. |
| **Dados pendentes** | Receptores sensíveis reais (R002 é fictício), meteorologia AERMET, topografia AERMAP, saída AERMOD completa. |
| **Dados bloqueantes** | Limites MP/SOx/NOx/HCTNM (em branco), concentração AERMOD real (malha completa), RII definitivo. |
| **Resultados declarados (não verificados)** | Concentração no receptor crítico (apenas 1 ponto, arquivo example), RII implícito no estudo. |
| **Resultados reais de modelo** | **Ausentes.** Nenhum arquivo AERMOD oficial foi fornecido até esta data. |
