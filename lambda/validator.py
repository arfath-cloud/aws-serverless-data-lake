import csv
import io
import os
import urllib.parse
import boto3

s3 = boto3.client("s3")
REQUIRED = {"order_id", "customer_id", "order_date", "amount"}

def lambda_handler(event, context):
    results = []
    for record in event.get("Records", []):
        bucket = record["s3"]["bucket"]["name"]
        key = urllib.parse.unquote_plus(record["s3"]["object"]["key"])
        response = s3.get_object(Bucket=bucket, Key=key)
        text = response["Body"].read().decode("utf-8-sig")
        reader = csv.DictReader(io.StringIO(text))
        missing = REQUIRED - set(reader.fieldnames or [])
        if missing:
            raise ValueError(f"{key}: missing columns {sorted(missing)}")
        count = sum(1 for _ in reader)
        results.append({"bucket": bucket, "key": key, "records": count, "status": "VALID"})
    return {"validated_files": results}
