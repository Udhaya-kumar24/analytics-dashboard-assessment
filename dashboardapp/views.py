from pyspark.sql import SparkSession
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

spark = SparkSession \
    .builder \
    .appName("Python PySpark Example") \
    .getOrCreate()

df = spark.read.option("header",True) \
    .option("delimiter",",") \
    .option("inferSchema",True) \
    .csv("C:/React/Django/analytics-dashboard-assessment/dashboardapp/data-to-visualize/Electric_Vehicle_Population_Data.csv")

def home(request):
    return JsonResponse({'message': 'Welcome to the Dashboard API!'})

@csrf_exempt
def test(request):
    length = df.filter(df.County == 'King').count()
    print('test', length,'::::::::::::::::::::::::::::::::::::::::::::::::::::')
    return JsonResponse({'res':length})

import os
# Run 'java -version' command and capture the output
java_version = os.popen('java -version').read()
# Print the output (you can also log it to Render logs)
print("Java Version:", java_version,":::::::::::")