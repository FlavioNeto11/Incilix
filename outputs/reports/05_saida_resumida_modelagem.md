# 05 — Saída Resumida da Modelagem Atmosférica

**Empreendimento:** INCILIX Incineradora Ltda. — Caieiras/SP  
**Data de geração:** 2026-04-15  
**Status:** **PRELIMINAR** — ausência de arquivos reais de entrada e saída do AERMOD

---

## 1. Modelo e pré-processadores

| Componente | Nome | Status |
|---|---|---|
| Modelo de dispersão | AERMOD | citado no estudo — arquivos ausentes |
| Pré-processador meteorológico | AERMET | citado no estudo — arquivos ausentes |
| Tratamento topográfico | AERMAP | citado no estudo — arquivos ausentes |

---

## 2. Parâmetros da fonte modelada

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
| Taxa de emissão declarada | 1,68 | µg/h | resultado declarado no estudo |
| Taxa de emissão declarada | 4,67×10⁻¹⁰ | g/s | resultado declarado no estudo |

---

## 3. Malha receptora

| Parâmetro | Valor | Status |
|---|---|---|
| Raio AID | 5.000 m | dado real informado |
| Espaçamento da malha | 100 m | dado real informado |
| Altura dos receptores | 1,5 m | dado real informado |
| Receptor crítico declarado | UTM E 324.800 / N 7.412.900 (~1.300 m) | resultado declarado no estudo |
| Tipo do receptor crítico | Unidade de saúde / área institucional | dado real informado |
| Critério CETESB (RII) | ≤ 1×10⁻⁵ | dado real informado |

---

## 4. Meteorologia

| Item | Caminho esperado | Status |
|---|---|---|
| Arquivos AERMET (.SFC, .PFL ou equivalente) | `data/input/meteorologia/` | **PENDENTE — diretório vazio** |

> Não foram encontrados arquivos meteorológicos em `data/input/meteorologia/`.  
> A modelagem definitiva requer séries horárias de superfície e perfil vertical de temperatura.

---

## 5. Topografia

| Item | Caminho esperado | Status |
|---|---|---|
| Arquivo AERMAP / DEM (.TER ou equivalente) | `data/input/topografia/` | **PENDENTE — diretório vazio** |

> Não foram encontrados arquivos topográficos em `data/input/topografia/`.  
> O AERMAP necessita de dados de elevação digital do terreno para cálculo de terreno complexo.

---

## 6. Receptores sensíveis

| Arquivo | Status |
|---|---|
| `data/input/receptores/receptores_sensiveis.example.csv` | Presente — arquivo de EXEMPLO (template) |
| `data/input/receptores/receptores_sensiveis.csv` | **AUSENTE — arquivo real necessário** |

> O arquivo `receptores_sensiveis.example.csv` é apenas um modelo de estrutura.  
> O arquivo real `receptores_sensiveis.csv` com coordenadas verificadas em campo ainda não foi fornecido.

---

## 7. Arquivos AERMOD — inventário

### 7.1 Arquivos encontrados em `data/input/aermod-output/`

| Arquivo | Tipo | Observação |
|---|---|---|
| `concentracoes_receptores.example.csv` | CSV de exemplo | **Arquivo de EXEMPLO** — não é saída real do AERMOD; contém valor 41 pg TEQ/m³ para R001 como placeholder |

### 7.2 Arquivos ausentes (necessários para resultado definitivo)

| Arquivo esperado | Formato | Finalidade |
|---|---|---|
| `concentracoes_receptores.csv` | CSV | Tabela real de concentração por receptor |
| `*.out` ou `*.plt` | AERMOD output | Arquivo de saída principal do modelo |
| `*.txt` (AERMOD result) | AERMOD output | Resultados de máximas e anuais por receptor |
| Arquivos AERMET processados | `.SFC`, `.PFL` | Meteorologia pré-processada |
| Arquivos AERMAP processados | `.TER` | Topografia pré-processada |

---

## 8. Status final

**PRELIMINAR**

Justificativa:
- Nenhum arquivo real de saída do AERMOD foi encontrado em `data/input/aermod-output/`
- Os diretórios de meteorologia e topografia estão vazios
- Os arquivos de receptores e concentrações presentes são únicamente exemplos (templates)
- Os limites de emissão de MP, SOx, NOx e HCTNM não foram fornecidos

Para que a saída seja classificada como **DEFINITIVA**, o usuário deve fornecer:

1. Arquivos de saída do AERMOD (`.out`, `.plt` ou `.txt`) com concentrações por receptor
2. `data/input/aermod-output/concentracoes_receptores.csv` (tabela real)
3. Arquivos meteorológicos processados pelo AERMET em `data/input/meteorologia/`
4. Arquivo de topografia processado pelo AERMAP em `data/input/topografia/`
5. `data/input/receptores/receptores_sensiveis.csv` com coordenadas reais verificadas
6. `data/input/limites-emissao/limites.csv` com limites preenchidos para MP, SOx, NOx e HCTNM
