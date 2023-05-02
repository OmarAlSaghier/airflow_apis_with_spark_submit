from pyspark.sql import SparkSession
import os

spark = SparkSession.builder \
    .master("local") \
    .appName("Trial app") \
    .config("spark.executor.memory", '4g') \
    .config('spark.executor.cores', '1') \
    .config('spark.cores.max', '1') \
    .config("spark.driver.memory",'4g') \
    .getOrCreate()

# /Users/oalsaghier/Documents/Training/airflow_apis_with_spark_submit/data_input_output/orders.csv
WORKING_DIR = str(os.getcwd())
data_input_file = f"{WORKING_DIR.split('/Training')[0]}/Training/airflow_apis_with_spark_submit/data_input_output/orders.csv"
data_output_file = f"{WORKING_DIR.split('/Training')[0]}/Training/airflow_apis_with_spark_submit/data_input_output/orders.json"

ordersDF = spark.read.csv(data_input_file, \
    header=True, \
    schema='''
        order_id INT, 
        order_date STRING, 
        order_customer_id INT, 
        order_status STRING'''
    )

ordersDF.show(10)

ordersDF.write. \
    mode('overwrite'). \
    option('compression', 'none'). \
    format('json'). \
    save(data_output_file)
