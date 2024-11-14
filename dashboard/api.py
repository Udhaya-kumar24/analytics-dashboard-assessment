from pyspark.sql import SparkSession
from django.http import JsonResponse

spark = SparkSession \
    .builder \
    .appName("Python PySpark Example") \
    .getOrCreate()

df = spark.read.option("header",True) \
    .option("delimiter",",") \
    .option("inferSchema",True) \
    .csv("C:/React/Django/analytics-dashboard-assessment/dashboard/Electric_Vehicle_Population_Data.csv")

def test():
    length = df.filter(df.County == 'King').count()
    return JsonResponse({'res':length})