from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
from airflow.decorators import dag, task
import json
import requests
from kafka import KafkaProducer, KafkaConsumer
default_args = {
    'owner': 'sagar',
    'start_date': datetime(2023, 1, 3, 0, 0),
    'catchup': False
}

@task(task_id='get-data-from-api')
def get_data():
    data = requests.get('https://randomuser.me/api/')
    data = data.json()
    data = data['results'][0]
    return data

@task(task_id='format-data')
def format_data(response):
    data = {}
    data['gender'] = response['gender']
    data['full_name'] = str(response['name']['first'] + ' ' + response['name']['last'])
    # data['last_name'] = response['name']['last']
    location = response['location']
    data['address'] = str(location['street']['number']) + ' ' + location['street']['name'] + ' ' + location['city'] + ',' + location['state'] + ',' + location['country'] + '-' + str(location['postcode'])
    data['email'] = response['email']
    data['dob'] = response['dob']['date'][:10]
    data['age'] = response['dob']['age']
    data['registered'] = response['registered']['date'][:10]
    data['phone'] = response['phone']
    return data

@task(task_id='stream-data-to-kafka')
def stream_data(data):
    producer = KafkaProducer(bootstrap_servers=['broker:29092'], max_block_ms=5000)
    producer.send('user_created',json.dumps(data).encode('utf-8'))
    print("########## data sent to the kafka server ##########")
  

@dag(dag_id='StreamDataToKafka_Dag',default_args=default_args,schedule_interval='* * * * *', catchup=False,start_date=datetime(2023, 1, 1))
def Main_dag(**kwargs):
    res = stream_data(format_data(get_data()))
a = Main_dag()

