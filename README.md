# 🌾 Agri-Insight — Analyse intelligente des parcelles agricoles

## 🚀 Objectif
**Agri-Insight** est un projet de modélisation et d’analyse géospatiale visant à :
- Identifier l’état de santé des cultures à partir d’images satellites et données agronomiques.
- Déterminer les besoins en irrigation et les signes de stress hydrique.
- Estimer les rendements futurs à partir des conditions géographiques et climatiques.
- Fournir une base de données géospatiale propre et standardisée pour l’entraînement de modèles IA.

Ce dépôt se concentre sur la **Phase 0 – Mise en place et cadrage** :
- Sélection d’une zone pilote.
- Extraction des parcelles agricoles via le RPG (Registre Parcellaire Graphique).
- Préparation des données géographiques en format GeoJSON.

---

## 🗂️ Structure du projet

agri-insight/
├── data/
│ ├── raw/ # Données brutes IGN (non versionnées)
│ ├── processed/ # Données nettoyées / prêtes pour analyse
│ ├── demo/ # Petits fichiers GeoJSON d’exemple
│ └── README.md # Documentation sur les sources
├── notebooks/
│ └── 01_extract_zone_pilote.ipynb
├── src/
│ └── extract_zone.py # Fonction principale d’extraction de parcelles
├── configs/
│ └── paths.yaml # (optionnel) chemins et variables de configuration
├── .gitignore
├── README.md
└── requirements.txt / pyproject.toml



---

## ⚙️ Installation

### 1. Créer ton environnement
```bash
python -m venv .venv
source .venv/bin/activate      # sous Linux/macOS
.venv\Scripts\activate         # sous Windows
```

2. Installer les dépendances
```bash
pip install geopandas folium shapely fiona
```

🌍 Données
🔗 Source officielle
Les données proviennent du RPG 2024 fourni par l’IGN :
👉 https://geoservices.ign.fr/telechargement-api/RPG

Télécharge le ZIP correspondant à ton département, puis dépose-le décompressé dans :

```bash

data/raw/
```

Exemple :

```bash
data/raw/PARCELLES_GRAPHIQUES.shp
data/raw/PARCELLES_GRAPHIQUES.dbf
data/raw/PARCELLES_GRAPHIQUES.shx
data/raw/PARCELLES_GRAPHIQUES.prj
```

⚠️ Ces fichiers sont non versionnés pour respecter les licences IGN et éviter d’alourdir le dépôt.

🧩 Utilisation
1. Depuis un notebook

```python
from src.extract_zone import extract_zone_pilote

zone_pilote = extract_zone_pilote(
    rpg_path="../data/raw/PARCELLES_GRAPHIQUES.shp",
    culture_filter="DCZ",  # Exemple : colza
    output_path="../data/zone_pilote.geojson"
)
1. En ligne de commande (optionnel)
```

```bash
python src/extract_zone.py --rpg ../data/raw/PARCELLES_GRAPHIQUES.shp --culture DCZ
```

🗺️ Visualisation rapide
Pour vérifier visuellement la zone extraite :

```python
import folium

center = zone_pilote.geometry.iloc[0].centroid.y, zone_pilote.geometry.iloc[0].centroid.x
m = folium.Map(location=center, zoom_start=13)
folium.GeoJson(zone_pilote).add_to(m)
m
```

🧠 Prochaines étapes
Phase 1 : Automatisation du téléchargement et nettoyage des données satellite (Sentinel-2).

Phase 2 : Calculs d’indices NDVI, NDWI, EVI.

Phase 3 : Modélisation IA & prédiction de rendement.

Phase 4 : Interface utilisateur et tableaux de bord interactifs.

👨‍🌾 Crédits & Mentions
Projet initié et conçu par 0c3CE — Data Engineer et explorateur de données agricoles 🌱
Inspiré par la tradition, tourné vers l’avenir.

Sources :

IGN France – Registre Parcellaire Graphique 2024

ESA Copernicus Sentinel-2 imagery

📜 Licence
Code sous licence MIT.
Les données IGN sont sous Licence Ouverte v2.0 — toute réutilisation doit citer la source.

« La technologie au service de la terre — pas l’inverse. »
