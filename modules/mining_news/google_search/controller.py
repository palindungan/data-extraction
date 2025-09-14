import time
import pprint
import urllib.parse

from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from modules.mining_news.helpers import Helpers

from scripts.repositories.mining_news_history import MiningNewsHistory as MiningNewsHistoryRepository


class Controller:
    @staticmethod
    def mining_data(
            keyword=None,
            driver=None,
    ):
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        items = soup.find_all('div', {'class': 'N54PNb BToiNc'})
        for idx, item in enumerate(items):
            row_1 = item.find('div', {'class': 'kb0PBd A9Y9g jGGQ5e', 'data-snhf': '0'})

            publisher_title = None
            try:
                publisher_title = row_1.find('span', {'class': 'VuuXrf'}).text.strip()
            except Exception as e:
                print(f"Exception: {e}")

            publisher_href = None
            try:
                if row_1.find('cite', {'class': 'qLRx3b tjvcx GvPZzd cHaqb'}):
                    publisher_href = row_1.find('cite', {'class': 'qLRx3b tjvcx GvPZzd cHaqb'}).contents[0].text.strip()
            except Exception as e:
                print(f"Exception: {e}")

            title = None
            try:
                title = row_1.find('h3', {'class': 'LC20lb MBeuO DKV0Md'}).text.strip()
            except Exception as e:
                print(f"Exception: {e}")

            url = None
            try:
                url = row_1.find('a', {'class': 'zReHs'})['href']
            except Exception as e:
                print(f"Exception: {e}")

            row_2 = item.find('div', {'class': 'kb0PBd A9Y9g', 'data-sncf': '1'})

            published_date = None
            description = None
            try:
                published_date = None
                description = row_2.find('div', {'class': 'VwiC3b yXK7lf p4wth r025kc Hdw6tb'}).text.strip()
                if " — " in description:
                    published_date = description.split(" — ")[0]
                    description = description.split(" — ")[1]
            except Exception as e:
                print(f"Exception: {e}")

            title = Helpers.normalization_text(title)
            description = Helpers.normalization_text(description)
            published_date = Helpers.normalization_text(published_date)
            url = Helpers.normalization_text(url)
            publisher_href = Helpers.normalization_text(publisher_href)
            publisher_title = Helpers.normalization_text(publisher_title)

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
                mining_source_id=2,
                code=metadata['url'],
                data=metadata,
            )

            print("--------------------------------------------------------------------------------")

    @staticmethod
    def mining(
            keyword=None,
            query=None,
            driver=None,
    ):
        try:
            page_current = 1

            query_encoded = urllib.parse.quote_plus(query)
            url = f"https://www.google.com/search?q={query_encoded}"
            print(f"url: {url}")
            print("")

            driver.get(url)
            time.sleep(2)

            while True:
                print("")
                print("################################################################################")
                print(f"page_current {page_current}")
                print("")

                Controller.mining_data(
                    keyword=keyword,
                    driver=driver,
                )

                if page_current >= 5:
                    break

                page_current += 1

                next_button = None

                try:
                    next_button = driver.find_element(By.CSS_SELECTOR, f'a[aria-label="Page {page_current}"]')
                except Exception as e:
                    if e:
                        print(f"next_button: False")

                if next_button:
                    WebDriverWait(driver, 10).until(ec.element_to_be_clickable(next_button))
                    driver.execute_script("arguments[0].scrollIntoView();", next_button)
                    driver.execute_script("arguments[0].click();", next_button)
                else:
                    break

        except Exception as e:
            print(f"Exception: {e}")
