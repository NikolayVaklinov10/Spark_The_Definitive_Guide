from pyspark.sql import SparkSession as spark

myRange = spark.range(1000).toDF("number")