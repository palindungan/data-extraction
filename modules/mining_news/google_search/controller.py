import time
import pprint
from bs4 import BeautifulSoup

from modules.mining_news.helpers import Helpers

from scripts.repositories.mining_news import MiningNews as MiningNewsRepository
from scripts.repositories.mining_news_history import MiningNewsHistory as MiningNewsHistoryRepository


class Controller:
    @staticmethod
    def mining_data(
            driver=None,
            url=None,
    ):
        print(f"url: {url}")
        print("")

        driver.get(url)
        time.sleep(5)

        soup = BeautifulSoup(driver.page_source, 'html.parser')

        items = soup.find_all('div', {'class': 'N54PNb BToiNc'})
        for idx, item in enumerate(items):
            row_1 = item.find('div', {'class': 'kb0PBd A9Y9g jGGQ5e', 'data-snhf': '0'})
            site_name = row_1.find('span', {'class': 'VuuXrf'}).text.strip()
            site_base_url = row_1.find('cite', {'class': 'qLRx3b tjvcx GvPZzd cHaqb'}).contents[0].text.strip()

            title = row_1.find('h3', {'class': 'LC20lb MBeuO DKV0Md'}).text.strip()
            url = row_1.find('a', {'class': 'zReHs'})['href']

            row_2 = item.find('div', {'class': 'kb0PBd A9Y9g', 'data-sncf': '1'})
            date = None
            description = row_2.find('div', {'class': 'VwiC3b yXK7lf p4wth r025kc Hdw6tb'}).text.strip()
            if " — " in description:
                date = description.split(" — ")[0]
                description = description.split(" — ")[1]

            metadata = {
                'site_name': Helpers.normalization_text(text=site_name),
                'site_base_url': Helpers.normalization_text(text=site_base_url),

                'title': Helpers.normalization_text(text=title),
                'url': Helpers.normalization_text(text=url),

                'date': Helpers.normalization_text(text=date),
                'description': Helpers.normalization_text(text=description),
            }
            pprint.pp(metadata)
            print("")

    @staticmethod
    def mining(
            query=None,
    ):
        driver = Helpers.chrome_driver_undetected_v1()

        try:
            url = "https://www.google.com/search?q=kasus+presiden+prabowo+subianto&sca_esv=efb3ab264f9589fa&ei=evO9aMPrIrPH4-EPw5-LoQg&ved=0ahUKEwjDkMTjxsePAxWz4zgGHcPPIoQQ4dUDCBE&uact=5&oq=kasus+presiden+prabowo+subianto&gs_lp=Egxnd3Mtd2l6LXNlcnAiH2thc3VzIHByZXNpZGVuIHByYWJvd28gc3ViaWFudG8yBBAAGEcyBBAAGEcyBBAAGEcyBBAAGEcyBBAAGEcyBBAAGEcyBBAAGEcyBBAAGEdI0h5QtxRYshxwAHgDkAECmAEAoAEAqgEAuAEDyAEA-AEBmAICoAILmAMAiAYBkAYIkgcBMqAHALIHALgHAMIHAzItMsgHCA&sclient=gws-wiz-serp"

            Controller.mining_data(
                driver=driver,
                url=url,
            )
        except Exception as e:
            print(f"Exception: {e}")

        driver.quit()
