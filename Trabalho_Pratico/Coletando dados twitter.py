# Importando os módulos Tweepy, Datetime e Json

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from datetime import datetime
from pymongo import MongoClient
import json


# Definições de acesso ao API Twitter

# Consumer Key
consumer_key = "mUZEhiqD4n2OwtWmEPDgpENwr"

# Consumer Secret
consumer_secret = "j9NcQ8bM5yPQC9tX9ALaTRHfufqDcjrvDVW28IKuJQ09OHIjci"

# Access Token
access_token = "809188036667965441-S9M5AzTINYLpJtZ3HTEOqSND4C4v0UX"

# Access Token Secret
access_token_secret = "bbY22BM8Lcd6ld0X84f2sGzMOh87Iq792xxtJP5zho83q"

# Criando as chaves de autenticação
auth = OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

# Criando uma classe para capturar os stream de dados do Twitter e armazenar no MongoDB
class MyListener(StreamListener):

    def on_data(self, dados):
        tweet = json.loads(dados)
        created_at = tweet["created_at"]
        id_str = tweet["id_str"]
        text = tweet["text"]
        obj = {"created_at":created_at,"id_str":id_str,"text":text,}
        tweetind = col.insert_one(obj).inserted_id
        print (obj)
        return True

# Criando o objeto pythonlistener
mylistener = MyListener()


# Criando o objeto stream
mystream = Stream(auth, listener = mylistener)

# Criando a conexão ao MongoDB
client = MongoClient('localhost', 27017)

# Criando o banco de dados Trabalho_Pratico
db = client.twitterdb

# Criando a collection "twitter"
col = db.tweets

# Criando uma lista de palavras chave para filtrar os Tweets
keywords = ['Donald Trump', 'Scott Pruitt', 'administrator of the Environmental', 'climate', 'fuel industry','air pollution','pollution', 'EPA', 'Barack Obama']

mystream.filter(track=keywords)

# Encerrando o stream de dados do Twitter
mystream.disconnect()
