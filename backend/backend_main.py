"""Routes for parent Flask app."""
import sys
from flask import request, jsonify
from backend_utils import extract_audio
from backend_utils import get_uuid
from pprint import pprint
from json import loads, dumps
from kafka import KafkaProducer, KafkaConsumer
from kafka.errors import NoBrokersAvailable

TEXT_TOPIC = "g5-untranscribed-text"
TEXT_AUDIO_PAIR_TOPIC = "text.audio.pair"
BROKER_ADDRESS = 'localhost:39092'

def init_routes(app):
    """A factory function that takes in the server 
    object and initializes the routes.
    """
    try:
        producer = KafkaProducer(bootstrap_servers=BROKER_ADDRESS,
                                 value_serializer=lambda x: dumps(x).encode('utf-8'))
        consumer = KafkaConsumer(TEXT_TOPIC,
                                 bootstrap_servers=BROKER_ADDRESS,
                                 auto_offset_reset='earliest',
                                 enable_auto_commit=False,
                                 value_deserializer=lambda x: loads(x.decode('utf-8')))
    except NoBrokersAvailable:
        print("NoBrokersAvailable")

    @app.route("/")
    def hello_world():
        return "<p>Hello, World!</p>"
    
    @app.route("/test")
    def test():
        return "Hello, world"

    @app.route('/get_text', methods=["GET"])
    def get_text():
        print("sending text")
        try:
            for s in consumer:
                print(s.value)
            # sentence = next(consumer)
            # print(sentence)
                sentence = s.value
            # sentence = "አገራችን ከአፍሪካም ሆነ ከሌሎች የአለም አገራት ጋር ያላትን አለም አቀፋዊ ግንኙነት ወደ ላቀ ደረጃ ያሸጋገረ ሆኗል በአገር ውስጥ አራት አለም"
                return jsonify(text=sentence)
        except NameError:
            print("Consumer not init")
            return 404
        
    @app.route('/getit',methods=['GET'])
    def getit():
        sentence = "አገራችን ከአፍሪካም ሆነ ከሌሎች የአለም አገራት ጋር ያላትን አለም አቀፋዊ ግንኙነት ወደ ላቀ ደረጃ ያሸጋገረ ሆኗል በአገር ውስጥ አራት አለም"
        return sentence
    
    @app.route('/submit', methods=["POST"])
    def publish_text_audio_pair():
        audio = request.files['audio']
        sentence = audio.filename
        audio = extract_audio(audio)
        print(audio.shape)
        audio = audio.tolist()
        id = get_uuid()
        data = {
            "id": id,
            "sentence": sentence,
            "audio": audio
        }
        try:
            res = producer.send(TEXT_AUDIO_PAIR_TOPIC, value=data)
            print(res)
        except NameError:
            print("Producer not created")

        # pprint(data)

        return "200"

    return app