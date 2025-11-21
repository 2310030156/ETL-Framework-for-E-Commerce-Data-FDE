FROM apache/airflow:2.6.3-python3.11

# Install dbt and Python deps as airflow user (use --user)
USER airflow
RUN pip install --no-cache-dir --user dbt-core dbt-postgres psycopg2-binary pandas matplotlib

# make folders
RUN mkdir -p /opt/airflow/dbt /opt/airflow/dags /opt/airflow/data
WORKDIR /opt/airflow
