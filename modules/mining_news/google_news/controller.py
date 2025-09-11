import pprint

from gnews import GNews


class Controller:
    @staticmethod
    def mining(
            query=None,
    ):
        print(f"query: {query}")
        print("")

        google_news = GNews()
        results = google_news.get_news(query)

        for idx, item in enumerate(results):
            print(item)
            print("--------------------------------------------------------------------------------")
