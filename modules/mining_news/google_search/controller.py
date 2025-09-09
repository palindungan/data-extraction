import time
import pprint

from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from modules.mining_news.helpers import Helpers

from scripts.repositories.mining_news import MiningNews as MiningNewsRepository
from scripts.repositories.mining_news_history import MiningNewsHistory as MiningNewsHistoryRepository


class Controller:
    @staticmethod
    def mining_data(
            driver=None,
    ):
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        items = soup.find_all('div', {'class': 'N54PNb BToiNc'})
        for idx, item in enumerate(items):
            row_1 = item.find('div', {'class': 'kb0PBd A9Y9g jGGQ5e', 'data-snhf': '0'})
            site_name = row_1.find('span', {'class': 'VuuXrf'}).text.strip()

            site_base_url = None
            if row_1.find('cite', {'class': 'qLRx3b tjvcx GvPZzd cHaqb'}):
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

            MiningNewsHistoryRepository.store(
                mining_source_id=1,
                code=metadata['url'],
                data=metadata,
            )

            MiningNewsRepository.auto_update(
                mining_source_id=1,
                code=metadata['url'],
                data=metadata,
            )

    @staticmethod
    def mining(
            query=None,
    ):
        driver = Helpers.chrome_driver_undetected_v1()

        try:
            page_current = 1

            url = "https://www.google.com/search?q=kasus+presiden+prabowo+subianto"
            print(f"url: {url}")
            print("")

            driver.get(url)
            time.sleep(5)

            while True:
                Controller.mining_data(
                    driver=driver,
                )

                page_current += 1
                next_button = driver.find_element(By.CSS_SELECTOR, f'a[aria-label="Page {page_current}"]')
                if next_button is not None:
                    WebDriverWait(driver, 10).until(ec.element_to_be_clickable(next_button))
                    driver.execute_script("arguments[0].scrollIntoView();", next_button)
                    driver.execute_script("arguments[0].click();", next_button)
                else:
                    break

        except Exception as e:
            print(f"Exception: {e}")

        driver.quit()
