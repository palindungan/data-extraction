from modules.mining_news.google_news.controller import Controller as GoogleNewsController
from modules.mining_news.google_search.controller import Controller as GoogleSearchController

query = "kasus presiden prabowo subianto"
GoogleNewsController.mining(query=query)
GoogleSearchController.mining(query=query)
