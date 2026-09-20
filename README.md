# IndustrIA — Manutenção Preditiva Industrial

Prevê se uma máquina está em risco de falhar a partir das leituras dos seus
sensores, para que a manutenção aja **antes da quebra** — sem trocar peças
saudáveis à toa.

## Problema de negócio

Numa operação industrial, uma falha não planejada para a produção, sai caro.
Mas fazer manutenção cedo demais desperdiça peças e mão de obra. O objetivo é
achar o equilíbrio: **pegar as falhas reais cedo, evitando alarmes falsos.**

**Pergunta:** dadas as leituras atuais dos sensores de uma máquina (temperatura
do ar/processo, rotação, torque, desgaste da ferramenta), ela está em risco de
falhar? (sim / não)

**Por que importa:** cada falha não detectada custa uma parada não planejada;
cada alarme falso custa uma intervenção desnecessária. O modelo é calibrado em
torno desse trade-off.

## Dados

Três fontes combinadas:

1. **Leituras de sensores** — AI4I 2020 Predictive Maintenance Dataset (UCI).
   Um dataset **público de benchmark, sintético** (~10.000 linhas).
   *Sintético por construção — não são dados reais de fábrica.*
2. **Cadastro de máquinas** — tabela de referência (id, tipo da máquina),
   integrada via **SQL**.
3. **Ordens de serviço** — notas de texto **derivadas dos rótulos de falha do
   dataset** (transformação documentada), usadas como dado não estruturado.

## Abordagem

Ingestão → verificação de qualidade dos dados → carga e JOIN em SQL → EDA +
estatística → engenharia de atributos → treino do modelo sem vazamento →
avaliação (precision/recall, threshold por custo).

## Stack

Python · pandas · NumPy · scikit-learn · SciPy · Matplotlib · Seaborn · SQLite ·
pytest · Git.

## Como rodar

    python -m venv .venv
    .\.venv\Scripts\Activate.ps1
    pip install -r requirements.txt

## Status

 Em construção — feito em etapas. Veja o histórico de commits.

## Autor

Igor Ribeiro dos Santos — github.com/IsantoDev · linkedin.com/in/isantosdev