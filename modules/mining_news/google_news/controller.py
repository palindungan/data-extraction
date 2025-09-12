import pprint

from gnews import GNews

from modules.mining_news.helpers import Helpers

from scripts.repositories.mining_news_history import MiningNewsHistory as MiningNewsHistoryRepository


class Controller:
    @staticmethod
    def mining(
            query=None,
    ):
        print(f"query: {query}")
        print("")

        google_news = GNews(
            max_results=10,
        )
        results = google_news.get_news(query)

        for idx, item in enumerate(results):
            pprint.pp(item)

            title = item['title']
            description = item['description']
            published_date = item['published date']
            url = item['url']
            publisher_href = item['publisher']['href']
            publisher_title = item['publisher']['title']

            metadata = {
                'title': Helpers.normalization_text(text=title),
                'description': Helpers.normalization_text(text=description),
                'published_date': Helpers.normalization_text(text=published_date),
                'url': Helpers.normalization_text(text=url),
                'publisher_href': Helpers.normalization_text(text=publisher_href),
                'publisher_title': Helpers.normalization_text(text=publisher_title),
            }
            pprint.pp(metadata)
            print("--------------------------------------------------------------------------------")

            MiningNewsHistoryRepository.store(
                mining_source_id=2,
                code=metadata['url'],
                data=metadata,
            )
