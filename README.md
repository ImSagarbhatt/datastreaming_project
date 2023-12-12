## Introduction
This project serves as a comprehensive guide to building an end-to-end data engineering pipeline. It covers each stage from data ingestion to processing and finally to storage, utilizing a robust tech stack that includes Apache Airflow, Python, Apache Kafka, Apache Zookeeper, AWS S3, AWS Crawler and AWS Athena. Everything is containerized using Docker for ease of deployment and scalability.


The project is designed with the following components:
- Data Source: We use randomuser.me API to generate random user data for our pipeline.
- Apache Airflow: Open-source platform to programmatically author, schedule, and monitor workflows, orchestrating complex data tasks with ease and reliability..
- Apache Kafka and Zookeeper: Used for streaming data, High-throughput distributed streaming platform, seamlessly connecting data producers and consumers, ensuring real-time data flow with durability.
- Control Center and Schema Registry: Helps in monitoring and schema management of our Kafka streams.
- AWS S3:- used for save the json file.
- AWS Crawler:- AWS Glue Crawler automates data cataloging, scanning various sources to create metadata, enhancing data discoverability and accessibility effortlessly.
- AWS Athena:- Serverless query service enabling SQL queries on S3 data, making data analysis seamless and efficient in the cloud.
