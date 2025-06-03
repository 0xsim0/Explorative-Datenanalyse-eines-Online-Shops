# Explorative Datenanalyse eines Online Shops

Dieses Repository enthält Daten und Notebooks zur Analyse eines Online-Retail-Datensatzes.

Zum schnellen Einstieg steht im Ordner `ecommerce-eda/scripts` das Python-Skript `summary.py` bereit.
Es lädt die Daten, bereinigt sie und berechnet Kennzahlen wie den Gesamtumsatz und den durchschnittlichen Warenkorbwert.

Das Skript kann direkt ausgeführt werden:

```bash
python ecommerce-eda/scripts/summary.py
```

Dabei wird auch die Kunden-ID korrekt als Ganzzahl behandelt. Dadurch erscheinen in Auswertungen keine Werte wie `17850.0`, sondern `17850`.
