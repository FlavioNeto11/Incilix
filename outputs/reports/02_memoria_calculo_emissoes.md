# 02 — Memória de Cálculo de Emissões

**Empreendimento:** INCILIX Incineradora Ltda. — Caieiras/SP  
**Data de geração:** 2026-04-15  
**Status geral:** PARCIALMENTE CALCULADO — MP, SOx e NOx calculados; HCTNM pendente

---

## 1. Dioxinas e Furanos — Cadeia completa de conversão

### 1.1 Dados de entrada

| Parâmetro | Valor | Unidade | Status |
|---|---:|---|---|
| Limite de emissão adotado | 0,14 | ng/Nm³ | dado real informado |
| Vazão volumétrica normalizada | 12.000 | Nm³/h | dado real informado |
| Taxa declarada no estudo | 1,68 | µg/h | resultado declarado no estudo |
| Taxa declarada no estudo | 4,67×10⁻¹⁰ | g/s | resultado declarado no estudo |

### 1.2 Sequência de conversão (ng/Nm³ → µg/h → g/s → kg/h → t/ano)

**Etapa 1 — Concentração → Fluxo mássico em ng/h:**

```
Q_ng_h = C_emissao(ng/Nm³) × Q_volumetrica(Nm³/h)
Q_ng_h = 0,14 × 12.000
Q_ng_h = 1.680 ng/h
```

**Etapa 2 — ng/h → µg/h** (fator: 1 µg = 1.000 ng):

```
Q_ug_h = Q_ng_h ÷ 1.000
Q_ug_h = 1.680 ÷ 1.000
Q_ug_h = 1,68 µg/h
```

**Etapa 3 — µg/h → g/s** (fator: 1 g = 1.000.000 µg; 1 h = 3.600 s):

```
Q_g_s = Q_ug_h × 1×10⁻⁶ (g/µg) ÷ 3.600 (s/h)
Q_g_s = 1,68 × 10⁻⁶ ÷ 3.600
Q_g_s = 4,6667×10⁻¹⁰ g/s
```

**Etapa 4 — g/s → kg/h** (fator: 1 kg = 1.000 g; 1 h = 3.600 s):

```
Q_kg_h = Q_g_s × 3.600 ÷ 1.000
Q_kg_h = 4,6667×10⁻¹⁰ × 3.600 ÷ 1.000
Q_kg_h = 1,68×10⁻⁹ kg/h
```

**Etapa 5 — kg/h → t/ano** (operação: 20 h/dia × 300 dias/ano = 6.000 h/ano; 1 t = 1.000 kg):

```
Q_t_ano = Q_kg_h × 6.000 h/ano ÷ 1.000
Q_t_ano = 1,68×10⁻⁹ × 6.000 ÷ 1.000
Q_t_ano = 1,008×10⁻⁸ t/ano
```

### 1.3 Verificação de consistência — taxa calculada vs. taxa declarada

| | Taxa calculada | Taxa declarada | Divergência |
|---|---|---|---|
| µg/h | **1,68 µg/h** | 1,68 µg/h | 0,00% — **consistente** |
| g/s | **4,6667×10⁻¹⁰ g/s** | 4,67×10⁻¹⁰ g/s | 0,07% |

**Análise da divergência em g/s:**
- Diferença absoluta: 4,67×10⁻¹⁰ − 4,6667×10⁻¹⁰ = 3,3×10⁻¹³ g/s  
- Causa identificada: arredondamento do valor declarado na 3ª casa decimal significativa  
- Conclusão: **sem erro de unidade ou de conversão** — os valores são coerentes entre si  
- A taxa de 1,68 µg/h e 4,67×10⁻¹⁰ g/s representam o mesmo valor físico

### 1.4 Notas sobre outras conversões relevantes

| Equivalência | Resultado | Observação |
|---|---|---|
| 41 pg TEQ/m³ → ng/m³ | 0,041 ng/m³ | Concentração no receptor R001 (arquivo de exemplo) |
| 41 pg TEQ/m³ → µg/m³ | 4,1×10⁻⁵ µg/m³ | Atenção: 41 pg/m³ ≠ 0,041 µg/m³ (diferem por fator 1.000) |
| 0,14 ng/Nm³ (limite emissão) | — | Padrão de emissão na chaminé — não comparável diretamente com concentração no receptor |

> **Atenção:** O valor de 41 pg TEQ/m³ provém de `concentracoes_receptores.example.csv`, que é um arquivo de EXEMPLO. Não representa saída real do AERMOD.

---

## 2. MP, SOx, NOx, HCTNM — Status atual

Foi criado o arquivo `data/input/limites-emissao/limites.csv` com limites para MP, SOx e NOx com base no plano técnico revisado.  
O parâmetro HCTNM permanece sem valor numérico por ausência de base normativa consolidada no processo.

**Arquivo preenchido:** `data/input/limites-emissao/limites.csv`  
**Pendência remanescente:** `limite` de HCTNM (unidade: mg/Nm³)

---

## 3. Tabela consolidada de emissões

| Poluente | Limite | Unidade | µg/h | g/s | kg/h | t/ano | Status |
|---|---:|---|---:|---:|---:|---:|---|
| Dioxinas e Furanos | 0,14 | ng/Nm³ | 1,68 | 4,667×10⁻¹⁰ | 1,68×10⁻⁹ | 1,008×10⁻⁸ | calculado |
| MP | 50 | mg/Nm³ | N/A | N/A | 0,6 | 3,6 | calculado |
| SOx | 250 | mg/Nm³ | N/A | N/A | 3,0 | 18,0 | calculado |
| NOx | 400 | mg/Nm³ | N/A | N/A | 4,8 | 28,8 | calculado |
| HCTNM | PENDENTE | mg/Nm³ | PENDENTE | PENDENTE | PENDENTE | PENDENTE | pendente_limite |

**Arquivo de limites esperado:** `data/input/limites-emissao/limites.csv`

---

## 4. Rastreabilidade

| Item | Origem | Status |
|---|---|---|
| Limite de dioxinas/furanos (0,14 ng/Nm³) | PROMPT_PRINCIPAL_EXECUCAO.md | dado real informado |
| Vazão (12.000 Nm³/h) | PROMPT_PRINCIPAL_EXECUCAO.md | dado real informado |
| Taxa 1,68 µg/h | Calculado nesta memória | calculado |
| Taxa 4,6667×10⁻¹⁰ g/s | Calculado nesta memória | calculado |
| Taxa 4,67×10⁻¹⁰ g/s | PROMPT_PRINCIPAL_EXECUCAO.md | resultado declarado no estudo |
| Limites MP, SOx e NOx | limites.csv | calculado |
| Limite HCTNM | limites.csv | pendente (base normativa) |
| Concentração R001 (41 pg TEQ/m³) | concentracoes_receptores.example.csv | arquivo de exemplo — não é resultado real |
