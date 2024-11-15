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

from django.http import JsonResponse
from pyspark.sql import SparkSession

def test_spark(request):
    try:
        # Initialize SparkSession
        spark = SparkSession.builder \
            .appName("TestApp") \
            .master("local[*]") \
            .getOrCreate()

        # Test Spark functionality
        data = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
        df = spark.createDataFrame(data)
        count = df.count()

        return JsonResponse({"status": "success", "spark_data_count": count})
    except Exception as e:
        return JsonResponse({"status": "error", "error": str(e)})
