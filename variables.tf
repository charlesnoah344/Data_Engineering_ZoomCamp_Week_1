locals {
  data_lake_bucket = "dtc_data_lake"
}

variable "project" {
  description = "ID du projet GCP"
  default     = "dtc-de-504710"
  type        = string
}

variable "region" {
  description = "Region for GCP resources."
  default     = "europe-west6"
  type        = string
}

variable "storage_class" {
  description = "Storage class type for your bucket."
  default     = "STANDARD"
  type        = string
}

variable "BQ_DATASET" {
  description = "BigQuery Dataset that raw data (from GCS) will be written to"
  default     = "trips_data_all"
  type        = string
}

# J'ai commenté les clés AWS car elles ne sont pas utilisées dans main.tf 
# et bloqueraient l'exécution en demandant une saisie manuelle.
#
# variable "access_key_id" {
#   description = "AWS access key"
#   type        = string
# }
#
# variable "aws_secret_key" {
#   description = "AWS secret key"
#   type        = string
# }