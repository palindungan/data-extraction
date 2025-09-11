from GoogleNews import GoogleNews


class Controller:
    @staticmethod
    def mining(
            query=None,
    ):
        googlenews = GoogleNews()
        googlenews.get_news(query)

        page_current = 1

        while True:
            results = googlenews.page_at(page_current)
            if results:
                page_current += 1
            else:
                break
