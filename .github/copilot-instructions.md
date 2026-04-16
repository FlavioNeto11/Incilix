# Instruções Copilot — INCILIX Complementação CETESB

Esta workspace deve ser operada de forma direta: um agente orquestrador conduz o fluxo e delega somente o necessário.

## Princípios

- Não inventar dados de modelagem.
- Não transformar mapa preliminar em definitivo.
- Separar dado informado, calculado, estimado, pendente e resultado real.
- Toda saída deve ser rastreável.
- Toda pendência deve virar log objetivo em `outputs/logs/`.
- Linguagem: português técnico, clara, compatível com documentação ambiental.

## Fluxo padrão

Sempre priorize:

1. diagnóstico;
2. validação de unidades;
3. cálculo de emissões;
4. mapa AID;
5. receptores sensíveis;
6. isoconcentração somente com dados reais;
7. saída resumida da modelagem;
8. relatório final;
9. quality gate.

## Comando principal

```bash
python src/pipeline.py
```
