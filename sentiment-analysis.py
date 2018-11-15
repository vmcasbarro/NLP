import Algorithmia

# import Algorithmia api key
from config import *

input = {
  "document": """Does not fit my husbands steering wheel. He drives a truck and does a fair amount of work in his truck. Disappointed"""
}
client = Algorithmia.client(client_key)
algo = client.algo('nlp/SentimentAnalysis/1.0.5')
print(' ')
print(algo.pipe(input).result)
print(' ')
