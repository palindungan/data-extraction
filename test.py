from modules.mining_news.google_news.controller import Controller as GoogleNewsController
from modules.mining_news.google_search.controller import Controller as GoogleSearchController

keyword = "yuri mansury"

queries = [
    keyword,

    f"berita {keyword}",
    f"{keyword} news",

    # f"seminar {keyword}",
    # f"{keyword} seminar",

    # f"pertemuan {keyword}",
    # f"{keyword} meeting",
]

for idx, item in enumerate(queries):
    print("GoogleNewsController.mining")
    GoogleNewsController.mining(keyword=keyword, query=item)
    print("")

    print("GoogleSearchController.mining")
    GoogleSearchController.mining(keyword=keyword, query=item,)
    print("")
