import sys
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.context import SparkContext
from pyspark.sql import functions as F

args = getResolvedOptions(sys.argv, ["JOB_NAME", "SOURCE_PATH", "TARGET_PATH"])
sc = SparkContext()
glue_context = GlueContext(sc)
spark = glue_context.spark_session
job = Job(glue_context)
job.init(args["JOB_NAME"], args)

source = spark.read.option("header", True).csv(args["SOURCE_PATH"])
clean = (source
    .withColumn("order_id", F.trim("order_id"))
    .withColumn("customer_id", F.trim("customer_id"))
    .withColumn("amount", F.col("amount").cast("decimal(12,2)"))
    .withColumn("order_date", F.to_date("order_date"))
    .filter(F.col("order_id").isNotNull() & (F.col("amount") >= 0))
    .withColumn("ingested_at", F.current_timestamp()))
clean.write.mode("overwrite").parquet(args["TARGET_PATH"])
job.commit()
