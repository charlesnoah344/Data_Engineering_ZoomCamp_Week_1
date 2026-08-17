# On part d'une image Python légère
FROM python:3.13-slim

# On installe les librairies nécessaires (pandas, sqlalchemy, connecteur postgres, outil pour lire le parquet)
RUN pip install pandas sqlalchemy psycopg2-binary pyarrow

# On définit le dossier de travail dans le conteneur
WORKDIR /app

# On copie notre script de notre ordinateur vers le conteneur
COPY ingest_data.py ingest_data.py

# Commande exécutée au démarrage du conteneur
ENTRYPOINT ["python", "ingest_data.py"]