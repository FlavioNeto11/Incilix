from __future__ import annotations

import csv
import math
from pathlib import Path
from typing import Any, Dict, List, Optional

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "input"
OUT = ROOT / "outputs"

PROJECT = {
    "empresa": "INCILIX Incineradora Ltda",
    "municipio": "Caieiras/SP",
    "fonte_utm_e": 324209.85,
    "fonte_utm_n": 7412260.54,
    "sistema": "SIRGAS 2000 / UTM Zona 23S",
    "altura_chamine_m": 17,
    "vazao_nm3_h": 12000,
    "temperatura_c": 200,
    "velocidade_m_s": 11,
    "diametro_m": 0.82,
    "operacao_h_dia": 20,
    "operacao_d_ano": 300,
    "aid_m": 5000,
    "receptor_altura_m": 1.5,
    "malha_m": 100,
    "limite_dioxinas_ng_nm3": 0.14,
    "taxa_declarada_ug_h": 1.68,
    "taxa_declarada_g_s": 4.67e-10,
}


def ensure_dirs() -> None:
    for p in [OUT / "maps", OUT / "tables", OUT / "reports", OUT / "html", OUT / "logs"]:
        p.mkdir(parents=True, exist_ok=True)


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def read_csv(path: Path) -> List[Dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: List[Dict[str, Any]], fieldnames: List[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def utm_to_latlon(e: float, n: float) -> Optional[tuple[float, float]]:
    try:
        from pyproj import Transformer
        transformer = Transformer.from_crs("EPSG:31983", "EPSG:4326", always_xy=True)
        lon, lat = transformer.transform(e, n)
        return lat, lon
    except Exception:
        return None


def distance_m(e1: float, n1: float, e2: float, n2: float) -> float:
    return math.sqrt((e2 - e1) ** 2 + (n2 - n1) ** 2)


def diagnose() -> None:
    content = f"""# 01 — Diagnóstico de lacunas

## Contexto

Complementação documental do ERSH e Plano de Gestão de Emissões da {PROJECT['empresa']} em {PROJECT['municipio']}.

## Lacunas principais

| Item | Status | Observação |
|---|---:|---|
| Mapa AID 5 km | Gerável | Pode ser gerado com coordenada da chaminé. |
| Receptores sensíveis reais | Pendente se não houver CSV | Inserir `data/input/receptores/receptores_sensiveis.csv`. |
| Mapa de isoconcentração definitivo | Pendente se não houver saída AERMOD | Exige dados reais de concentração por receptor. |
| Saída resumida da modelagem | Parcial | Pode ser estruturada; fica pendente se arquivos AERMOD não forem enviados. |
| MP, SOx, NOx, HCTNM | Pendente | Exige limites regulatórios no arquivo `limites.csv`. |
| Validação de unidades | Gerável | Será calculada com dados conhecidos. |

## Risco técnico

O maior risco é protocolar mapa de isoconcentração sem base numérica real da modelagem. Isso deve ser evitado.
"""
    write(OUT / "reports" / "01_diagnostico_lacunas.md", content)


def calculate_emissions() -> None:
    vazao = PROJECT["vazao_nm3_h"]
    limite = PROJECT["limite_dioxinas_ng_nm3"]
    taxa_ng_h = limite * vazao
    taxa_ug_h = taxa_ng_h / 1000
    taxa_g_s = taxa_ng_h * 1e-9 / 3600
    diff = abs(taxa_g_s - PROJECT["taxa_declarada_g_s"]) / PROJECT["taxa_declarada_g_s"] * 100

    rows: List[Dict[str, Any]] = [
        {
            "poluente": "Dioxinas e Furanos",
            "limite": limite,
            "unidade_limite": "ng/Nm3",
            "vazao_nm3_h": vazao,
            "taxa_ug_h": f"{taxa_ug_h:.6g}",
            "taxa_g_s": f"{taxa_g_s:.6e}",
            "taxa_kg_h": "N/A",
            "taxa_t_ano": "N/A",
            "status": "calculado",
            "fonte": "dados conhecidos do estudo",
        }
    ]

    limits_path = DATA / "limites-emissao" / "limites.csv"
    limits = read_csv(limits_path)
    for r in limits:
        pol = (r.get("poluente") or "").strip()
        raw_lim = (r.get("limite") or "").strip().replace(",", ".")
        unit = (r.get("unidade") or "mg/Nm3").strip()
        fonte = (r.get("fonte") or "informado pelo usuário").strip()
        if not pol:
            continue
        if not raw_lim:
            rows.append({
                "poluente": pol,
                "limite": "PENDENTE",
                "unidade_limite": unit,
                "vazao_nm3_h": vazao,
                "taxa_ug_h": "N/A",
                "taxa_g_s": "N/A",
                "taxa_kg_h": "PENDENTE",
                "taxa_t_ano": "PENDENTE",
                "status": "pendente_limite",
                "fonte": fonte,
            })
            continue
        try:
            lim = float(raw_lim)
            if unit.lower().replace("³", "3") in ["mg/nm3", "mg/nm³"]:
                kg_h = lim * vazao / 1_000_000
                t_ano = kg_h * PROJECT["operacao_h_dia"] * PROJECT["operacao_d_ano"] / 1000
                rows.append({
                    "poluente": pol,
                    "limite": lim,
                    "unidade_limite": unit,
                    "vazao_nm3_h": vazao,
                    "taxa_ug_h": "N/A",
                    "taxa_g_s": "N/A",
                    "taxa_kg_h": f"{kg_h:.6g}",
                    "taxa_t_ano": f"{t_ano:.6g}",
                    "status": "calculado",
                    "fonte": fonte,
                })
            else:
                rows.append({
                    "poluente": pol,
                    "limite": lim,
                    "unidade_limite": unit,
                    "vazao_nm3_h": vazao,
                    "taxa_ug_h": "N/A",
                    "taxa_g_s": "N/A",
                    "taxa_kg_h": "unidade_nao_suportada",
                    "taxa_t_ano": "unidade_nao_suportada",
                    "status": "verificar_unidade",
                    "fonte": fonte,
                })
        except ValueError:
            pass

    fields = ["poluente", "limite", "unidade_limite", "vazao_nm3_h", "taxa_ug_h", "taxa_g_s", "taxa_kg_h", "taxa_t_ano", "status", "fonte"]
    write_csv(OUT / "tables" / "emissoes_calculadas.csv", rows, fields)

    md_rows = "\n".join(
        f"| {r['poluente']} | {r['limite']} | {r['unidade_limite']} | {r['taxa_ug_h']} | {r['taxa_g_s']} | {r['taxa_kg_h']} | {r['taxa_t_ano']} | {r['status']} |"
        for r in rows
    )
    content = f"""# 02 — Memória de cálculo de emissões

## Dioxinas e furanos

Fórmula aplicada:

```txt
taxa_g_s = limite_ng_nm3 * vazao_nm3_h * 1e-9 / 3600
```

Resultado calculado:

- limite: {limite} ng/Nm³
- vazão: {vazao} Nm³/h
- taxa: {taxa_ug_h:.6g} µg/h
- taxa: {taxa_g_s:.6e} g/s
- divergência contra taxa declarada: {diff:.2f}%

## Tabela consolidada

| Poluente | Limite | Unidade | µg/h | g/s | kg/h | t/ano | Status |
|---|---:|---|---:|---:|---:|---:|---|
{md_rows}

## Observação

MP, SOx, NOx e HCTNM só serão calculados quando os limites forem preenchidos em `data/input/limites-emissao/limites.csv`.
"""
    write(OUT / "reports" / "02_memoria_calculo_emissoes.md", content)


def process_receptors() -> List[Dict[str, Any]]:
    path = DATA / "receptores" / "receptores_sensiveis.csv"
    rows = read_csv(path)
    processed: List[Dict[str, Any]] = []
    if not rows:
        write(OUT / "logs" / "RECEPTORES_SENSIVEIS_AUSENTES.md", "# Receptores sensíveis ausentes\n\nNão foi encontrado `data/input/receptores/receptores_sensiveis.csv`. O mapa AID será gerado sem receptores reais.\n")
        write_csv(OUT / "tables" / "receptores_sensiveis.csv", [], ["id", "nome", "tipo", "utm_e", "utm_n", "distancia_fonte_m", "fonte_dado", "observacao"])
        return processed

    for r in rows:
        try:
            e = float(str(r.get("utm_e", "")).replace(",", "."))
            n = float(str(r.get("utm_n", "")).replace(",", "."))
            d = distance_m(PROJECT["fonte_utm_e"], PROJECT["fonte_utm_n"], e, n)
            processed.append({
                "id": r.get("id", ""),
                "nome": r.get("nome", ""),
                "tipo": r.get("tipo", ""),
                "utm_e": e,
                "utm_n": n,
                "distancia_fonte_m": round(d, 2),
                "fonte_dado": r.get("fonte_dado", ""),
                "observacao": r.get("observacao", ""),
            })
        except Exception:
            continue

    fields = ["id", "nome", "tipo", "utm_e", "utm_n", "distancia_fonte_m", "fonte_dado", "observacao"]
    write_csv(OUT / "tables" / "receptores_sensiveis.csv", processed, fields)
    return processed


def generate_aid_map(receptors: List[Dict[str, Any]]) -> None:
    latlon = utm_to_latlon(PROJECT["fonte_utm_e"], PROJECT["fonte_utm_n"])
    if not latlon:
        write(OUT / "logs" / "MAPA_AID_NAO_GERADO.md", "# Mapa AID não gerado\n\nBiblioteca pyproj/folium indisponível ou falha na transformação de coordenadas.\n")
        return
    lat, lon = latlon
    try:
        import folium
        m = folium.Map(location=[lat, lon], zoom_start=12)
        folium.Marker([lat, lon], tooltip="Chaminé INCILIX", popup="Fonte/chaminé").add_to(m)
        for radius in [100, 200, 1000, 3000, 5000]:
            folium.Circle([lat, lon], radius=radius, fill=False, tooltip=f"Raio {radius} m").add_to(m)
        for r in receptors:
            rp = utm_to_latlon(float(r["utm_e"]), float(r["utm_n"]))
            if rp:
                folium.Marker(rp, tooltip=str(r.get("nome", "Receptor")), popup=f"{r.get('tipo','')} - {r.get('distancia_fonte_m','')} m").add_to(m)
        m.save(str(OUT / "maps" / "mapa_aid_receptores.html"))
        write(OUT / "maps" / "mapa_aid_receptores.txt", "Mapa HTML gerado em mapa_aid_receptores.html. Para PNG, abrir no navegador e exportar/capturar tela.\n")
    except Exception as exc:
        write(OUT / "logs" / "MAPA_AID_ERRO.md", f"# Erro ao gerar mapa AID\n\n{exc}\n")

    content = f"""# 03 — Anexo: Mapa da AID com receptores sensíveis

## Produto gerado

- `outputs/maps/mapa_aid_receptores.html`

## Critério adotado

A Área de Influência Direta foi representada por raio de {PROJECT['aid_m']} m a partir da chaminé, com raios auxiliares de 100 m, 200 m, 1 km e 3 km.

## Fonte

- Coordenada da chaminé: UTM E {PROJECT['fonte_utm_e']} / N {PROJECT['fonte_utm_n']} — {PROJECT['sistema']}.

## Receptores sensíveis

Total importado: {len(receptors)}.

Se o total for zero, a base de receptores deve ser fornecida em `data/input/receptores/receptores_sensiveis.csv`.
"""
    write(OUT / "reports" / "03_anexo_mapa_aid.md", content)


def process_isoconcentration() -> None:
    path = DATA / "aermod-output" / "concentracoes_receptores.csv"
    rows = read_csv(path)
    aermod_files = list((DATA / "aermod-output").glob("*"))
    real_files = [p for p in aermod_files if not p.name.endswith(".example.csv")]

    if not rows:
        write(OUT / "logs" / "AERMOD_OUTPUT_AUSENTE.md", "# Saída AERMOD ausente\n\nNão foi encontrado `data/input/aermod-output/concentracoes_receptores.csv`. Não é adequado gerar mapa de isoconcentração definitivo sem a saída numérica da modelagem.\n")
        content = """# 04 — Anexo: Mapa de isoconcentração

## Status

PENDENTE / PRELIMINAR.

Não foi encontrada tabela real de concentração por receptor nem saída AERMOD suficiente para gerar mapa definitivo.

## Dado necessário

Fornecer `data/input/aermod-output/concentracoes_receptores.csv` com colunas:

```txt
receptor_id,utm_e,utm_n,concentration,unit,period,pollutant
```

## Observação técnica

Não foi gerado mapa definitivo para evitar criação de resultado sem base numérica auditável.
"""
        write(OUT / "reports" / "04_anexo_isoconcentracao.md", content)
        return

    # Save top concentrations table
    parsed = []
    for r in rows:
        try:
            parsed.append({
                "receptor_id": r.get("receptor_id", ""),
                "utm_e": float(str(r.get("utm_e", "")).replace(",", ".")),
                "utm_n": float(str(r.get("utm_n", "")).replace(",", ".")),
                "concentration": float(str(r.get("concentration", "")).replace(",", ".")),
                "unit": r.get("unit", ""),
                "period": r.get("period", ""),
                "pollutant": r.get("pollutant", ""),
            })
        except Exception:
            continue
    parsed.sort(key=lambda x: x["concentration"], reverse=True)
    fields = ["receptor_id", "utm_e", "utm_n", "concentration", "unit", "period", "pollutant"]
    write_csv(OUT / "tables" / "top_concentracoes.csv", parsed[:10], fields)

    # Make simple folium map
    try:
        import folium
        latlon = utm_to_latlon(PROJECT["fonte_utm_e"], PROJECT["fonte_utm_n"])
        m = folium.Map(location=latlon, zoom_start=12)
        folium.Marker(latlon, tooltip="Chaminé INCILIX").add_to(m)
        for r in parsed:
            rp = utm_to_latlon(r["utm_e"], r["utm_n"])
            if rp:
                folium.CircleMarker(rp, radius=5, popup=f"{r['receptor_id']}: {r['concentration']} {r['unit']}").add_to(m)
        m.save(str(OUT / "maps" / "mapa_isoconcentracao.html"))
    except Exception as exc:
        write(OUT / "logs" / "ISOCONCENTRACAO_MAPA_ERRO.md", f"# Erro ao gerar mapa de isoconcentração\n\n{exc}\n")

    top = parsed[0] if parsed else None
    content = f"""# 04 — Anexo: Mapa de isoconcentração

## Status

GERADO COM DADOS FORNECIDOS.

## Arquivos

- `outputs/maps/mapa_isoconcentracao.html`
- `outputs/tables/top_concentracoes.csv`

## Receptor crítico calculado a partir da tabela

- Receptor: {top['receptor_id'] if top else 'N/A'}
- Concentração: {top['concentration'] if top else 'N/A'} {top['unit'] if top else ''}
- Período: {top['period'] if top else 'N/A'}
- Poluente: {top['pollutant'] if top else 'N/A'}

## Arquivos AERMOD encontrados

{chr(10).join('- ' + p.name for p in real_files) if real_files else '- Nenhum arquivo adicional encontrado.'}
"""
    write(OUT / "reports" / "04_anexo_isoconcentracao.md", content)


def model_summary() -> None:
    files = [p.name for p in (DATA / "aermod-output").glob("*") if not p.name.endswith(".example.csv")]
    content = f"""# 05 — Saída resumida da modelagem atmosférica

## Modelo

- Modelo citado: AERMOD.
- Pré-processador meteorológico citado: AERMET.
- Tratamento topográfico citado: AERMAP.

## Fonte modelada

| Parâmetro | Valor |
|---|---:|
| Tipo | Fonte pontual/chaminé |
| Coordenada E | {PROJECT['fonte_utm_e']} |
| Coordenada N | {PROJECT['fonte_utm_n']} |
| Sistema | {PROJECT['sistema']} |
| Altura | {PROJECT['altura_chamine_m']} m |
| Vazão | {PROJECT['vazao_nm3_h']} Nm³/h |
| Temperatura | {PROJECT['temperatura_c']} °C |
| Velocidade | {PROJECT['velocidade_m_s']} m/s |
| Diâmetro equivalente | {PROJECT['diametro_m']} m |
| Operação | {PROJECT['operacao_h_dia']} h/dia, {PROJECT['operacao_d_ano']} dias/ano |

## Malha receptora

- Raio AID: {PROJECT['aid_m']} m.
- Espaçamento previsto: {PROJECT['malha_m']} m.
- Altura de receptor: {PROJECT['receptor_altura_m']} m.

## Arquivos AERMOD encontrados

{chr(10).join('- ' + f for f in files) if files else '- Nenhum arquivo real encontrado em `data/input/aermod-output/`.'}

## Status

A saída resumida está estruturalmente pronta. Para ser definitiva, anexar arquivos reais de entrada/saída do AERMOD, AERMET e AERMAP ou tabela consolidada de concentração por receptor.
"""
    write(OUT / "reports" / "05_saida_resumida_modelagem.md", content)


def final_report() -> None:
    report_files = [
        "01_diagnostico_lacunas.md",
        "02_memoria_calculo_emissoes.md",
        "03_anexo_mapa_aid.md",
        "04_anexo_isoconcentracao.md",
        "05_saida_resumida_modelagem.md",
    ]
    parts = ["# Relatório Final — Complementação ERSH / CETESB\n"]
    for name in report_files:
        p = OUT / "reports" / name
        if p.exists():
            parts.append(p.read_text(encoding="utf-8"))
            parts.append("\n---\n")
    md = "\n".join(parts)
    write(OUT / "reports" / "RELATORIO_FINAL_COMPLEMENTACAO.md", md)
    html = "<html><head><meta charset='utf-8'><title>Relatório Final</title></head><body>" + md.replace("\n", "<br>\n") + "</body></html>"
    write(OUT / "html" / "RELATORIO_FINAL_COMPLEMENTACAO.html", html)


def quality_gate() -> None:
    required = {
        "diagnostico": OUT / "reports" / "01_diagnostico_lacunas.md",
        "memoria_emissoes": OUT / "reports" / "02_memoria_calculo_emissoes.md",
        "mapa_aid": OUT / "maps" / "mapa_aid_receptores.html",
        "anexo_aid": OUT / "reports" / "03_anexo_mapa_aid.md",
        "anexo_isoconcentracao": OUT / "reports" / "04_anexo_isoconcentracao.md",
        "saida_modelagem": OUT / "reports" / "05_saida_resumida_modelagem.md",
        "relatorio_final": OUT / "reports" / "RELATORIO_FINAL_COMPLEMENTACAO.md",
    }
    missing = [k for k, p in required.items() if not p.exists()]
    blockers = []
    if (OUT / "logs" / "AERMOD_OUTPUT_AUSENTE.md").exists():
        blockers.append("Saída AERMOD / concentração por receptor ausente: isoconcentração definitiva pendente.")
    if (OUT / "logs" / "RECEPTORES_SENSIVEIS_AUSENTES.md").exists():
        blockers.append("Base real de receptores sensíveis ausente.")

    if missing:
        status = "REPROVADO"
    elif blockers:
        status = "APROVADO COM RESSALVAS"
    else:
        status = "APROVADO"

    content = f"""# Quality Gate

## Status

**{status}**

## Arquivos obrigatórios ausentes

{chr(10).join('- ' + m for m in missing) if missing else '- Nenhum.'}

## Ressalvas / bloqueios técnicos

{chr(10).join('- ' + b for b in blockers) if blockers else '- Nenhum.'}

## Próximos dados recomendados

- CSV real de receptores sensíveis.
- Arquivos reais de saída AERMOD/AERMET/AERMAP.
- Tabela de concentração por receptor.
- Limites de MP, SOx, NOx e HCTNM conforme parecer aplicável.
"""
    write(OUT / "logs" / "QUALITY_GATE.md", content)


def main() -> None:
    ensure_dirs()
    diagnose()
    calculate_emissions()
    receptors = process_receptors()
    generate_aid_map(receptors)
    process_isoconcentration()
    model_summary()
    final_report()
    quality_gate()
    print("Fluxo concluído. Verifique outputs/reports, outputs/maps, outputs/tables e outputs/logs.")


if __name__ == "__main__":
    main()
