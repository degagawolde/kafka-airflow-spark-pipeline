# kafka-airflow-spark-pipeline
Text-to-speech data collection with Kafka, Airflow, Spark and S3 bucket.

**Table of Content**
* [Project Overview](#project-overview)
* [Data](#data)
* [Installation Guide](#installation-guide)
* [LICENCE](#licence)
* [Contributers](#contributors)


## Project overview

In this project design and build a robust, large scale, fault tolerant, highly available Kafka cluster that can be used to post a sentence and receive an audio file and produce a tool that can be deployed to process posting and receiving text and audio files from and into a data lake, apply transformation in a distributed manner, and load it into a warehouse in a suitable format to train a speech-t0-text model. 
![workflow](https://github.com/Hu-10xB6W7G5/kafka-airflow-spark-pipeline/blob/unittest/screenshots/ETL%20Pipeline%20with%20Apache%20Kafka,%20Spark%20and%20Airflow.png?raw=true) 

## Data 

There are a number of large text corpora we will use, but for the purpose of testing the backend development, you can use the recently released Amharic news text classification dataset with baseline performance dataset:   

[IsraelAbebe/An-Amharic-News-Text-classification-Dataset: An Amharic News Text classification Dataset (github.com)](https://github.com/IsraelAbebe/An-Amharic-News-Text-classification-Dataset)

Alternative data Ready-made Amharic data collected from different sources  [here](https://drive.google.com/file/d/1_YLX27TdACjIF1iu8e3t-kkTb1qBlLkO/view)

## Frontend
![image](https://user-images.githubusercontent.com/59474650/194722808-4e55ce24-7078-41b0-aa7a-2fc70d4441ab.png)


### Installation Guide

### LICENCE
 MIT
#### Contributors
* [Yohans Samuel](https://github.com/YohansSamuel)
* [Degaga Wolde](https://github.com/degagawolde)
* [Margaret Chepkirui](https://github.com/MegCheppy) 
* [Yohanes Gutema](https://github.com/Yohanes-GR)
* [Tibarek Mesfin](https://github.com/tibarekb)
* [Andenet Alexander](https://github.com/andyalex234)

