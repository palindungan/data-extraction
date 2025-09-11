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
        googlenews.get_news(query)

        page_current = 1

        while True:
            print("")
            print("################################################################################")
            print(f"page_current {page_current}")
            print("")

            results = googlenews.page_at(page_current)
            pprint.pp(results)
            print("--------------------------------------------------------------------------------")

            if results:
                page_current += 1
            else:
                break
