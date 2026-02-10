# Data Cleaning & Standardization Pipeline (Excel + Python)

## 🇬🇧 English

### Overview
This project demonstrates a real-world data quality workflow: cleaning and standardizing inconsistent text values across two data sources (Excel columns) to produce reliable “adjusted” names for analytics and reporting.

### Problem
Operational datasets often contain:
- typos and inconsistent casing (e.g., `AG Tower` vs `ag tower`)
- extra spaces or different separators (e.g., `G-8` vs `G 8`)
- missing keywords (e.g., one source contains `tower` while the other does not)

These issues lead to failed joins, duplicate entities, and inaccurate dashboards.

### Solution
A Python pipeline that:
1. Reads an Excel file
2. Cleans text (lowercase, trim, replace dashes, normalize whitespace)
3. Applies a rule-based adjustment to harmonize the presence of the keyword **“tower”**
4. Creates two new standardized columns:
   - `PM Building Adjusted`
   - `PF Building Adjusted`
5. Exports the result to a new Excel file (output)

### Tech Stack
- Python (pandas)
- Excel

### Repository Structure
- `src/` → Python script
- `sample_data/` → synthetic/anonymized sample input Excel
- `outputs/` → generated standardized output Excel
- `images/` → optional screenshots (before/after)

### How to Run
1) Install dependencies:
```bash
pip install pandas openpyxl

2) Run the script:
python src/standardize_buildings.py
-----------------------------------------------------------------------------------------------------
### 🇬🇧 Français
# Data Cleaning & Standardization Pipeline (Excel + Python)

## Aperçu
Ce projet illustre un cas réel de **qualité des données** : nettoyer et standardiser des champs texte incohérents entre deux sources (colonnes Excel) afin de produire des noms “ajustés” fiables pour l’analyse et le reporting.

## Contexte / Problématique
Dans les données opérationnelles, on rencontre souvent :
- des fautes de frappe et des différences de casse (ex. `AG Tower` vs `ag tower`)
- des espaces en trop ou des séparateurs différents (ex. `G-8` vs `G 8`)
- des mots-clés manquants (ex. une source contient `tower` et l’autre non)

Ces écarts peuvent entraîner des jointures incorrectes, des doublons et des tableaux de bord peu fiables.

## Solution
Un pipeline Python qui :
1. Lit un fichier Excel
2. Nettoie le texte (minuscule, suppression des espaces inutiles, remplacement des tirets, normalisation des espaces)
3. Applique une règle de standardisation pour harmoniser la présence du mot-clé **« tower »**
4. Crée deux nouvelles colonnes standardisées :
   - `PM Building Adjusted`
   - `PF Building Adjusted`
5. Exporte le résultat vers un nouveau fichier Excel (sortie)

## Outils
- Python (pandas)
- Excel

## Structure du dépôt
- `src/` → script Python
- `sample_data/` → fichier d’entrée d’exemple (données synthétiques/anonymisées)
- `outputs/` → fichier de sortie généré
- `images/` → captures optionnelles (avant/après)

## Exécution
1) Installer les dépendances :
```bash
pip install pandas openpyxl

Lancer le script :
python src/standardize_buildings.py
