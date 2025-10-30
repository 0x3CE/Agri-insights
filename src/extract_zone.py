# src/extract_zone.py
import os
import geopandas as gpd

def extract_zone_pilote(
    rpg_path: str,
    output_path: str = "../data/zone_pilote.geojson",
    culture_filter: str | None = None,
    min_surface: float = 0.2,
    epsg_output: int = 4326
) -> gpd.GeoDataFrame:
    """
    Extrait une zone pilote à partir du RPG, filtrée selon la culture et la surface.

    Paramètres
    ----------
    rpg_path : str
        Chemin vers le fichier shapefile RPG (.shp).
    output_path : str, optionnel
        Chemin du fichier GeoJSON de sortie (défaut: ../data/zone_pilote.geojson).
    culture_filter : str, optionnel
        Code ou mot-clé de la culture à filtrer (ex: 'DCZ' pour colza).
        Si None, garde toutes les cultures.
    min_surface : float, optionnel
        Surface minimale de parcelle à conserver (en hectares).
    epsg_output : int, optionnel
        Code EPSG du système de coordonnées de sortie (défaut: 4326, WGS84).

    Retour
    ------
    gpd.GeoDataFrame
        GeoDataFrame des parcelles filtrées et reprojetées.
    """

    # S'assurer que GDAL peut restaurer l'index .shx manquant
    os.environ["SHAPE_RESTORE_SHX"] = "YES"

    # Charger le shapefile RPG
    rpg = gpd.read_file(rpg_path)
    print(f"✅ Fichier RPG chargé : {len(rpg)} parcelles")

    # Filtrer sur la culture si précisé
    if culture_filter:
        zone = rpg[rpg["CULTURE_D1"].str.contains(culture_filter, case=False, na=False)]
        print(f"🔍 Filtrage culture = {culture_filter} → {len(zone)} parcelles")
    else:
        zone = rpg

    # Sélectionner les colonnes utiles
    zone_pilote = zone[["ID_PARCEL", "CULTURE_D1", "SURF_PARC", "geometry"]]

    # Filtrer par surface minimale
    zone_pilote = zone_pilote[zone_pilote["SURF_PARC"] > min_surface]

    # Reprojeter en WGS84
    zone_pilote = zone_pilote.to_crs(epsg=epsg_output)

    # Exporter en GeoJSON
    zone_pilote.to_file(output_path, driver="GeoJSON")

    print(f"💾 Export terminé : {output_path} ({len(zone_pilote)} parcelles)")

    return zone_pilote
