# INCILIX — Complementação CETESB Direta

Workspace direta para VS Code Insiders + GitHub Copilot Agent Mode.

A estrutura usa um **prompt principal** e um **agente orquestrador** que delega para poucos agentes especializados.

## Como usar

1. Abra esta pasta no VS Code Insiders.
2. Instale dependências:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

3. Abra o arquivo:

```txt
PROMPT_PRINCIPAL_EXECUCAO.md
```

4. Cole o conteúdo no Copilot Chat em Agent Mode.
5. Peça para executar o fluxo completo.

Também é possível rodar direto:

```bash
python src/pipeline.py
```

## Entradas opcionais

Coloque arquivos reais nestas pastas:

```txt
data/input/receptores/receptores_sensiveis.csv
data/input/limites-emissao/limites.csv
data/input/aermod-output/concentracoes_receptores.csv
data/input/aermod-output/*.out
data/input/meteorologia/
data/input/topografia/
```

## Saídas esperadas

```txt
outputs/maps/
outputs/tables/
outputs/reports/
outputs/html/
outputs/logs/
```

## Regra de segurança técnica

O projeto **não inventa resultado AERMOD**. Sem dados reais de concentração, o mapa de isoconcentração fica marcado como pendente/preliminar.
