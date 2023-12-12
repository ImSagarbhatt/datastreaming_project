from datetime import datetime
from kafka import KafkaConsumer
import datetime
import json
import boto3


aws_access_key = 'ADD_YOUR_AWS_ACCESS_KEY'
aws_secret_key = 'ADD_YOUR_AWS_SECRET_KEY'
aws_s3_bucket = 'ADD_YOUR_AWS_S3_BUCKET'

s3 = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)

def save_data():
    consumer = KafkaConsumer ('user_created',bootstrap_servers = ['localhost:9092'], value_deserializer=lambda m: json.loads(m.decode('utf-8')))
    
    for j in consumer:
        today = str(datetime.datetime.today())[:16].replace(" ", "_").replace(":","-")
        json_string = json.dumps(j.value)
        json_bytes = json_string.encode('utf-8')
        filename = f"demo_file{today}.json"
        response = s3.put_object(Bucket=aws_s3_bucket, Key=filename, Body=json_bytes)
        
        # Check if the upload was successful
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            print("File uploaded successfully!")
        else:
            print("Failed to upload file.")

if __name__ == '__main__':
    save_data()