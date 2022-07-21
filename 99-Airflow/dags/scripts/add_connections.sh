airflow connections delete 'http_api'
airflow connections delete 'pg_conn'


airflow connections add 'http_api' --conn-type 'http' --conn-host 'raw.githubusercontent.com/pavanmg/EKG-Foundations/master/04A-postgress/'


airflow connections add pg_conn \
  --conn-type 'postgres' \
  --conn-host 'my-postgres' \
  --conn-login 'postgres' \
  --conn-schema 'northwind' \
  --conn-password 'postgres' 

exit 0