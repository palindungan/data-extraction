import pprint

from gnews import GNews

from modules.mining_news.helpers import Helpers

from scripts.repositories.mining_news_history import MiningNewsHistory as MiningNewsHistoryRepository


class Controller:
    @staticmethod
    def mining(
            keyword=None,
            query=None,
    ):
        print(f"query: {query}")
        print("")

        google_news = GNews(
            max_results=50,
        )
        results = google_news.get_news(query)

        for idx, item in enumerate(results):
            pprint.pp(item)

            title = Helpers.normalization_text(item['title'])
            description = Helpers.normalization_text(item['description'])
            published_date = Helpers.normalization_text(item['published date'])
            url = Helpers.normalization_text(item['url'])
            publisher_href = Helpers.normalization_text(item['publisher']['href'])
            publisher_title = Helpers.normalization_text(item['publisher']['title'])

            metadata = {
                'title': title,
                'description': description,
                'published_date': published_date,
                'url': url,
                'publisher_href': publisher_href,
                'publisher_title': publisher_title,
            }
            pprint.pp(metadata)

            MiningNewsHistoryRepository.store(
                mining_source_id=1,
                code=metadata['url'],
                data=metadata,
            )

            print("--------------------------------------------------------------------------------")
