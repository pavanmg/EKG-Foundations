from airflow import DAG
from airflow.operators.dummy import DummyOperator 
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.operators.bash import BashOperator
from airflow.providers.amazon.aws.transfers.s3_to_redshift import S3ToRedshiftOperator
from airflow.contrib.operators.s3_list_operator import S3ListOperator
from datetime import datetime, date 


with DAG (dag_id = "cnr_pipeline", start_date  = datetime( 2020,1,1)  ) as dag:

    start = DummyOperator(task_id = 'start')
    create_connections = BashOperator(task_id = 'create_connections' , bash_command = "./scripts/add_connections_cnr.sh")
    postgres_extract = PostgresOperator(task_id = 'postgres_extract' , sql = "", postgres_conn_id = "")

    dump_date_to_s3 = S3ListOperator(task_id = 'dump_date_to_s3' , bucket = "", prefix = "" , delimiter = "")
    s3_to_redshift_copy = S3ToRedshiftOperator(task_id = 's3_to_redshift_copy' , schema = "", table = "" , s3_bucket = "", s3_key = "")



    

