# IndustrIA — Manutenção Preditiva Industrial

Prevê se uma máquina está em risco de falhar a partir das leituras dos seus
sensores, para que a manutenção aja **antes da quebra** — sem trocar peças
saudáveis à toa.

> 🚧 **Em construção** — projeto de portfólio feito em etapas versionadas (veja o
> histórico de commits). Dados, EDA e estatística concluídos; modelagem em andamento.

## Problema de negócio

Numa operação industrial, uma falha não planejada para a produção e sai caro.
Mas fazer manutenção cedo demais desperdiça peças e mão de obra. O objetivo é o
equilíbrio: **pegar as falhas reais cedo, evitando alarmes falsos.**

**Pergunta:** dadas as leituras atuais dos sensores de uma máquina (temperatura
do ar/processo, rotação, torque, desgaste da ferramenta), ela está em risco de
falhar? (sim / não)

Como falha é rara (~3,4% dos casos), o foco de avaliação é **precision/recall**
(não acurácia), com **threshold calibrado por custo**.

## Dados

Duas fontes integradas via **SQL** (modelagem fato + dimensão):

1. **Leituras de sensores** — AI4I 2020 Predictive Maintenance Dataset (UCI),
   público e de benchmark (~10.000 linhas). *Sintético por construção — não são
   dados reais de fábrica.*
2. **Cadastro de máquinas** — dimensão que traduz o tipo (L/M/H → Low/Medium/High),
   unida às leituras por `JOIN`.

## Abordagem

Ingestão → qualidade dos dados → carga e `JOIN` em SQL → EDA + estatística →
engenharia de atributos → **(próximo)** modelo + avaliação (precision/recall,
threshold por custo).

## Principais achados (até aqui)

- Máquinas de **qualidade baixa** falham quase o **dobro** das de alta
  (3,92% vs 2,09%).
- **Torque** e **desgaste da ferramenta** são significativamente maiores nas
  falhas (teste t de Welch, **p < 0,001**) — os sinais preditivos mais fortes.
- Nenhuma variável isolada separa falha/não-falha (boxplots com sobreposição)
  → justifica um **modelo multivariado**.
- Features físicas criadas alinhadas aos modos de falha do dataset:
  `power` (torque×rotação), `temp_diff` e `strain` (desgaste×torque).

## Stack

Python · pandas · NumPy · SQL (SQLite) · SciPy · Matplotlib · Seaborn ·
scikit-learn · pytest · Git.

## Como rodar

    git clone https://github.com/IsantoDev/industria-preditiva.git
    cd industria-preditiva
    python -m venv .venv
    .\.venv\Scripts\Activate.ps1
    pip install -e .
    python src/industria/download_data.py   # baixa o dataset
    python src/industria/database.py        # monta o banco SQLite
    # EDA em: notebooks/01_eda.ipynb

## Roadmap

- [x] Ingestão + qualidade + SQL
- [x] EDA + estatística
- [x] Engenharia de atributos
- [ ] Modelo + avaliação (precision/recall, threshold por custo)
- [ ] Dados não estruturados (ordens de serviço) + documentação final

## Autor

**Igor Ribeiro dos Santos**
[github.com/IsantoDev](https://github.com/IsantoDev) ·
[linkedin.com/in/isantosdev](https://linkedin.com/in/isantosdev)