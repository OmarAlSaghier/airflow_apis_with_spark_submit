# The expresission (username:password) needs to be base64 encoded added to the string "Basic".
#   for example, if we have username and password as (airflow:airflow),
#   the value for the "Authorization" header must be as:
#   -H "Authorization: Basic YWlyZmxvdzphaXJmbG93"

# Ref: https://airflow.apache.org/docs/apache-airflow/stable/stable-rest-api-ref.html


# List airflow dags
curl -X GET \
    -H "Content-Type: application/json" \
    -H "Authorization: Basic ${base64(username:password)}" \
    http://localhost:8080/api/v1/dags

# Example:
curl -X GET \
    -H "Content-Type: application/json" \
    -H "Authorization: Basic YWlyZmxvdzphaXJmbG93" \
    http://localhost:8080/api/v1/dags


# Triggering an unpaused airflow dag called "spark_submit_dag"
curl -X POST \
    -H "Content-Type: application/json" \
    -H "Authorization: Basic ${base64(username:password)}" \
    -d '{"conf":{}}' \
    http://localhost:8080/api/v1/dags/spark_submit_dag/dagRuns
