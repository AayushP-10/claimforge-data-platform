
# ClaimForge Data Engineering Platform

An end-to-end AWS data engineering project that simulates a multi-partner e-commerce data processing platform.

## Tech Stack

- Python and PySpark
- AWS DMS and CDC
- Amazon S3
- AWS Glue
- Apache Parquet
- AWS Glue Data Catalog
- Amazon Athena
- AWS Step Functions
- Amazon EventBridge
- Amazon Quick Sight
- AWS CloudFormation
- AWS IAM and CloudWatch
- GitHub Actions

## Architecture

Operational PostgreSQL + SFTP Partner Feeds + REST API
→ Raw S3 Data Lake
→ AWS Glue PySpark Transformations
→ Data Quality and Reconciliation
→ Curated S3 Parquet
→ Glue Data Catalog
→ Athena
→ Quick Sight

## Goal

Build reusable, incremental, production-style data pipelines
with automated orchestration, infrastructure deployment,
data validation, and historical reporting.
