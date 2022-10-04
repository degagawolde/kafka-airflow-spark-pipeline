# kafka-airflow-spark-pipeline
Text-to-speech data collection with Kafka, Airflow, and Spark.

## Project overview

In this project design and build a robust, large scale, fault tolerant, highly available Kafka cluster that can be used to post a sentence and receive an audio file and produce a tool that can be deployed to process posting and receiving text and audio files from and into a data lake, apply transformation in a distributed manner, and load it into a warehouse in a suitable format to train a speech-t0-text model.  

## Data 

There are a number of large text corpora we will use, but for the purpose of testing the backend development, you can use the recently released Amharic news text classification dataset with baseline performance dataset:   

[IsraelAbebe/An-Amharic-News-Text-classification-Dataset: An Amharic News Text classification Dataset (github.com)](https://github.com/IsraelAbebe/An-Amharic-News-Text-classification-Dataset)

Alternative data Ready-made Amharic data collected from different sources  [here](https://drive.google.com/file/d/1_YLX27TdACjIF1iu8e3t-kkTb1qBlLkO/view)
