# Project 04 — AWS Serverless Data Lake Pipeline

An educational serverless ingestion pattern: an object lands in S3, an S3 event invokes Lambda for basic CSV validation, Glue transforms the dataset, and Athena queries the curated output.

## Architecture
`S3 raw/ -> Lambda validation -> Glue job -> S3 curated/ -> Glue Catalog/Athena`

## Included
- `lambda/validator.py` — lightweight S3 event handler and CSV header validation
- `glue/transform_orders.py` — Glue Spark job to normalize and enrich order data
- `athena/` — sample analytical SQL
- `infra/template.yaml` — starter SAM template for the Lambda function and IAM permissions
- `data/orders.csv` — synthetic sample

## Setup
1. Install AWS CLI and AWS SAM CLI; configure a sandbox AWS account.
2. Review `infra/template.yaml` and replace the bucket placeholder with a globally unique bucket name.
3. Build/deploy with SAM after reviewing IAM permissions and region.
4. Create the Glue database/catalog and Glue job role; upload the Glue script to S3 and configure job arguments.
5. Upload the sample CSV to the raw prefix and query the curated output with Athena.

This repository is a deployment starter, not a one-command complete AWS environment. Glue database/job setup and Athena workgroup/output location must be configured in your account. AWS charges may apply. Never commit access keys or secrets.
