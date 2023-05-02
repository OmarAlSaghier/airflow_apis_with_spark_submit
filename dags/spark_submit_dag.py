import airflow
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

dag_spark_submit = DAG(
    dag_id='spark_submit_dag',
    default_args={"retries": 2},
    schedule_interval='0 0 * * *',
    start_date=days_ago(1),
    description='executing spark submit command'
)

SPARK_SUBMIT_FILE = "/Users/oalsaghier/Documents/Training/Big_data_tools/hadoop_spark_installation/spark_code_test.py"

print("submitting the job")

spark_submit_task = SparkSubmitOperator(
		task_id='spark_submit_task',
		application =SPARK_SUBMIT_FILE,
		conn_id= 'spark_default',
		dag=dag_spark_submit
	)

spark_submit_task

if __name__ == "__main__":
    dag_spark_submit.cli()
