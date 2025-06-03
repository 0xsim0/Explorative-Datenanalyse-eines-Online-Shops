# Explorative Datenanalyse eines Online Shops

Dieses Repository enthält Daten und Notebooks zur Analyse eines Online-Retail-Datensatzes.

Zum schnellen Einstieg steht im Ordner `ecommerce-eda/scripts` das Python-Skript `summary.py` bereit.
Es lädt die Daten, bereinigt sie und berechnet Kennzahlen wie den Gesamtumsatz und den durchschnittlichen Warenkorbwert.

Das Skript kann direkt ausgeführt werden:

```bash
python ecommerce-eda/scripts/summary.py
```

Dabei wird auch die Kunden-ID korrekt als Ganzzahl behandelt. Dadurch erscheinen in Auswertungen keine Werte wie `17850.0`, sondern `17850`.

## Requirements

- Python 3.8 or higher
- pandas
- numpy
- matplotlib
- seaborn
- jupyter

## Installation

1. Optional: Create and activate a virtual environment.
2. Install all dependencies:

```bash
pip install -r requirements.txt
```

The file `data.csv` in `ecommerce-eda/data` contains the **Online Retail** dataset from the UCI Machine Learning Repository. It is made available for research and educational uses under the terms described at the [UCI website](https://archive.ics.uci.edu/ml/datasets/Online+Retail).

