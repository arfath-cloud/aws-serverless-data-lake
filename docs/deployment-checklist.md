# Deployment checklist

- [ ] Use a dedicated sandbox AWS account and region.
- [ ] Confirm S3 bucket name and block public access.
- [ ] Review Lambda IAM scope and event notification configuration.
- [ ] Configure Glue execution role, database, job, and script location.
- [ ] Configure curated S3 prefix, Glue Catalog table, and Athena output location.
- [ ] Add retries, dead-letter handling, monitoring, encryption, lifecycle policies, and idempotency before production use.
- [ ] Delete test resources after the exercise to avoid ongoing charges.
