from modules.mining_news.google_news.controller import Controller as GoogleNewsController
from modules.mining_news.google_search.controller import Controller as GoogleSearchController

query = "kasus presiden prabowo subianto"

print("GoogleNewsController.mining")
GoogleNewsController.mining(query=query)
print("")

# print("GoogleSearchController.mining")
# GoogleSearchController.mining(query=query)
# print("")
