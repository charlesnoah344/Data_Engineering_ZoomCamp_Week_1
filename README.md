# Data Engineering ZoomCamp - Week 1

Repository for the first week of the Data Engineering ZoomCamp exercises. It contains a PostgreSQL ingestion pipeline, Docker-based local orchestration, Terraform resources for GCP, and the notebook/SQL answers used for the homework.

## What is in this repo

- A reusable ingestion script for NYC taxi data in [ingest_data.py](ingest_data.py).
- A Docker image and a separate Docker Compose setup for the homework pipeline in [Homework/Pipeline](Homework/Pipeline).
- Terraform code for a GCS data lake bucket and a BigQuery dataset in [main.tf](main.tf) and [variables.tf](variables.tf).
- Notebook and SQL homework material in [Homework/pipeline.ipynb](Homework/pipeline.ipynb) and [Homework/readme.md](Homework/readme.md).

## Repository Layout

```text
.
├── Dockerfile
├── ingest_data.py
├── main.tf
├── variables.tf
├── pyproject.toml
├── notebook.ipynb
├── README.md
└── Homework/
		├── Pipeline/
		│   ├── Dockerfile
		│   ├── docker-compose.yaml
		│   └── ingest_data.py
		├── docker-compose.yaml
		├── pipeline.ipynb
		└── readme.md
```

## Requirements

- Python 3.13+
- Docker and Docker Compose
- Terraform 1.0+
- A Google Cloud project if you want to apply the Terraform resources

## Local Python Setup

The root project uses the dependencies declared in [pyproject.toml](pyproject.toml).

Install the Python dependencies with your preferred tool, for example:

```bash
uv sync
```

If you prefer not to use `uv`, install the packages listed in [pyproject.toml](pyproject.toml): `pandas`, `sqlalchemy`, `pyarrow`, `tqdm`, and the PostgreSQL driver used by your environment.

## Running the Root Ingestion Script

The root [ingest_data.py](ingest_data.py) ingests yellow taxi data from the public DataTalksClub dataset into PostgreSQL.

Example:

```bash
python ingest_data.py \
	--pg-user root \
	--pg-pass root \
	--pg-host localhost \
	--pg-port 5432 \
	--pg-db ny_taxi \
	--year 2021 \
	--month 1 \
	--target-table yellow_taxi_data
```

Useful options:

- `--pg-user`, `--pg-pass`, `--pg-host`, `--pg-port`, `--pg-db`: PostgreSQL connection parameters.
- `--year`, `--month`: dataset partition to download.
- `--target-table`: destination table name.
- `--chunksize`: CSV chunk size for streaming ingestion.

## Homework Pipeline with Docker Compose

The homework pipeline under [Homework/Pipeline](Homework/Pipeline) loads green taxi data and the taxi zone lookup table into PostgreSQL.

1. Go to the folder:

```bash
cd Homework/Pipeline
```

2. Create or update your `.env` file with:

```env
POSTGRES_USER=root
POSTGRES_PASSWORD=root
POSTGRES_DB=ny_taxi_green
```

3. Start the stack:

```bash
docker-compose up --build
```

This starts:

- `db`: PostgreSQL on port `5432`
- `pgadmin`: pgAdmin on port `8080`
- `ingestion`: the Python container that downloads the parquet and CSV files, then writes them to PostgreSQL

### Accessing pgAdmin

- URL: `http://localhost:8080`
- Email: `admin@admin.com`
- Password: `root`

### Expected Tables

After a successful run, PostgreSQL contains at least:

- `green_tripdata_2025_11`
- `taxi_zone_lookup`

## Terraform

The Terraform files provision two resources in GCP:

- a GCS bucket for the data lake
- a BigQuery dataset

### Files

- [main.tf](main.tf): provider configuration and resources
- [variables.tf](variables.tf): project, region, bucket and dataset settings

### Typical commands

```bash
terraform init
terraform apply
terraform destroy
```

Use `-auto-approve` if you want non-interactive runs.

## Notebook and Homework Notes

- [Homework/pipeline.ipynb](Homework/pipeline.ipynb) contains the notebook work for the homework tasks.
- [Homework/readme.md](Homework/readme.md) contains the SQL answers and short command notes.

## Troubleshooting

- If PostgreSQL authentication fails, check that the environment variables used by Docker and the ingestion script match.
- If the ingestion container exits immediately, inspect the logs of `db` and `ingestion` first.
- If Terraform fails to authenticate to GCP, verify the service account JSON path in [main.tf](main.tf) or set `GOOGLE_APPLICATION_CREDENTIALS`.

## Notes

- The root ingestion script and the homework pipeline are intentionally separate examples.
- The homework pipeline currently targets the `green_tripdata_2025-11` parquet file and the NYC taxi zone lookup CSV.
