# 03 — Anexo: Mapa da AID com receptores sensíveis

**Empreendimento:** INCILIX Incineradora Ltda. — Caieiras/SP  
**Elaboração:** geoprocessamento-mapas  
**Datum:** SIRGAS 2000 / UTM Zona 23S  
**Data:** 2026-04-15

---

## 1. Localização da fonte

| Campo | Valor |
|---|---|
| UTM E | 324 209,85 m |
| UTM N | 7 412 260,54 m |
| Zona | 23S — SIRGAS 2000 |
| Latitude (grau decimal) | −23,38998° S |
| Longitude (grau decimal) | −46,72014° W |
| Latitude (grau/min/s) | 23° 23′ 24″ S |
| Longitude (grau/min/s) | 46° 43′ 13″ W |

> Conversão UTM → grau decimal: método TM inverso (GRS80), k₀ = 0,9996.

---

## 2. Critério da AID

- **Raio da AID:** 5 000 m (conforme PROMPT_PRINCIPAL_EXECUCAO.md e método CETESB para incineração).
- **Raios auxiliares representados no mapa:** 100 m, 200 m, 1 000 m, 3 000 m.

---

## 3. Produto cartográfico

- Arquivo: `outputs/maps/mapa_aid_receptores.html`
- Tecnologia: Leaflet.js (OpenStreetMap)
- Status: **GERADO — funcional**
- Conteúdo:
  - Marcador da chaminé (ponto vermelho)
  - Círculo AID 5 km (azul sólido)
  - Círculos auxiliares: 100 m, 200 m, 1 km, 3 km (azul tracejado)
  - Marcador do receptor crítico declarado (ponto laranja)
  - Legenda interativa

---

## 4. Receptor crítico declarado

| Campo | Valor |
|---|---|
| ID | RC-01 |
| Descrição | Unidade de saúde / área institucional |
| UTM E | 324 800 m |
| UTM N | 7 412 900 m |
| Latitude (decimal) | −23,38422° S |
| Longitude (decimal) | −46,71436° W |
| Distância declarada (estudo) | ~1 300 m |
| Distância calculada (UTM) | ~870 m |
| Fonte | Declarado em PROMPT_PRINCIPAL_EXECUCAO.md |

> **Atenção — inconsistência:** A distância calculada a partir das coordenadas UTM (E 324800 / N 7412900) resulta em **~870 m**, divergindo da distância declarada no estudo (~1 300 m). Recomenda-se verificar as coordenadas exatas do receptor antes do protocolo definitivo.

---

## 5. Status dos receptores sensíveis

| Origem | Qtd | Status |
|---|---|---|
| `receptores_sensiveis.csv` (real) | 0 | Arquivo não fornecido — **PENDENTE** |
| Receptor crítico declarado (estudo) | 1 | Incluído (RC-01) |
| **Total no mapa** | **1** | Parcial |

> **Arquivo obrigatório ausente:** `data/input/receptores/receptores_sensiveis.csv`

---

## 6. Como fornecer os receptores sensíveis

1. Criar (ou exportar do SIG) o arquivo: `data/input/receptores/receptores_sensiveis.csv`
2. Colunas obrigatórias:

```
id,nome,tipo,utm_e,utm_n,fonte_dado,observacao
```

3. Tipos aceitos: `escola`, `hospital`, `unidade_saude`, `residencia`, `parque`, `outro`
4. Datum: SIRGAS 2000 / UTM Zona 23S
5. Após fornecer o arquivo, executar novamente `python src/pipeline.py`
