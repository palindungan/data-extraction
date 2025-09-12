import pprint

from gnews import GNews

from modules.mining_news.helpers import Helpers

from scripts.repositories.mining_news import MiningNews as MiningNewsRepository
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

            site_name = None
            site_base_url = None
            title = None
            url = None
            date = None
            description = None

            metadata = {
                'site_name': Helpers.normalization_text(text=site_name),
                'site_base_url': Helpers.normalization_text(text=site_base_url),

                'title': Helpers.normalization_text(text=title),
                'url': Helpers.normalization_text(text=url),

                'date': Helpers.normalization_text(text=date),
                'description': Helpers.normalization_text(text=description),
            }
            pprint.pp(metadata)
            print("--------------------------------------------------------------------------------")

            MiningNewsHistoryRepository.store(
                mining_source_id=2,
                code=metadata['url'],
                data=metadata,
            )

            MiningNewsRepository.auto_update(
                mining_source_id=2,
                code=metadata['url'],
                data=metadata,
            )
