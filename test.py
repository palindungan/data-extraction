from modules.mining_news.google_news.controller import Controller as GoogleNewsController
from modules.mining_news.google_search.controller import Controller as GoogleSearchController

name = "yuri mansury"

queries = [
    name,

    f"berita {name}",
    f"{name} news",

    f"seminar {name}",
    f"{name} seminar",

    f"pertemuan {name}",
    f"{name} meeting",
]

for idx, item in enumerate(queries):
    print("GoogleNewsController.mining")
    GoogleNewsController.mining(query=item)
    print("")

    print("GoogleSearchController.mining")
    GoogleSearchController.mining(query=item)
    print("")
