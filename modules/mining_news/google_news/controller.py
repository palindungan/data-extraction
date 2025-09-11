import pprint

from GoogleNews import GoogleNews


class Controller:
    @staticmethod
    def mining(
            query=None,
    ):
        print(f"query: {query}")
        print("")

        googlenews = GoogleNews()
        items = googlenews.get_news(query)

        for idx, item in enumerate(items):
            pprint.pp(item)
            print("--------------------------------------------------------------------------------")
