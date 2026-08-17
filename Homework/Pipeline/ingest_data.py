import urllib.request
import pandas as pd
from sqlalchemy import create_engine
import time
import os

def main():
    print("Démarrage du processus d'ingestion...")
    
    # Paramètres de connexion (qui correspondent au docker-compose)
    user = os.getenv('POSTGRES_USER')
    password = os.getenv('POSTGRES_PASSWORD')
    host = 'db' # C'est le nom du conteneur de la base de données !
    port = '5432'
    db_name = os.getenv('POSTGRES_DB')
    
    # URLs et noms de fichiers
    url_trips = "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2025-11.parquet"
    url_zones = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv"
    
    file_trips = "green_tripdata_2025-11.parquet"
    file_zones = "taxi_zone_lookup.csv"
    
    # Téléchargement
    print(f"Téléchargement de {file_trips}...")
    urllib.request.urlretrieve(url_trips, file_trips)
    
    print(f"Téléchargement de {file_zones}...")
    urllib.request.urlretrieve(url_zones, file_zones)
    
    # Connexion à PostgreSQL
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db_name}')
    
    # Ingestion des trajets
    print("Lecture et insertion du fichier Parquet (Trajets)...")
    df_trips = pd.read_parquet(file_trips)
    df_trips.to_sql(name='green_tripdata_2025_11', con=engine, if_exists='replace', index=False)
    
    # Ingestion des zones
    print("Lecture et insertion du fichier CSV (Zones)...")
    df_zones = pd.read_csv(file_zones)
    df_zones.to_sql(name='taxi_zone_lookup', con=engine, if_exists='replace', index=False)
    
    print("Ingestion terminée avec succès !")

if __name__ == '__main__':
    main()