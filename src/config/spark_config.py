from pyspark.sql import SparkSession

def get_spark_session(app_name: str = "Agronomic Data Extraction - MG") -> SparkSession:
    return SparkSession.builder.appName(app_name).getOrCreate()
