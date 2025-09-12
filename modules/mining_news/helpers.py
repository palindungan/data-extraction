class Helpers:
    @staticmethod
    def chrome_driver_undetected_v1():
        import undetected_chromedriver as uc

        chrome_options = uc.ChromeOptions()
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_argument("--disable-popup-blocking")
        # chrome_options.add_argument("--incognito")

        user_agent = Helpers.get_user_agent_random()
        print(f"user_agent: {user_agent}")
        chrome_options.add_argument(user_agent)

        driver = uc.Chrome(options=chrome_options, use_subprocess=True)

        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
                    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
                    Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3, 4, 5] });
                    Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] });
                """
        })

        return driver

    @staticmethod
    def get_user_agent_random():
        import random

        os_list = [
            "Windows NT 10.0; Win64; x64",
            "Windows NT 6.3; Win64; x64",
            "Macintosh; Intel Mac OS X 10_15_7",
            "Macintosh; Intel Mac OS X 13_4",
            "X11; Linux x86_64",
            "X11; Ubuntu; Linux x86_64",
            "Android 12; Mobile",
            "Android 13; Mobile",
            "iPhone; CPU iPhone OS 16_0 like Mac OS X",
            "iPad; CPU OS 15_6 like Mac OS X",
        ]

        browsers = [
            lambda: f"Chrome/{random.randint(130, 139)}.0.{random.randint(0, 9999)}.{random.randint(0, 999)} Safari/537.36",
            lambda: f"Firefox/{random.randint(115, 120)}.0",
            lambda: f"Edg/{random.randint(130, 139)}.0.{random.randint(0, 9999)}.{random.randint(0, 999)}",
            lambda: f"Version/{random.randint(16, 17)}.0 Safari/{random.randint(600, 605)}.{random.randint(1, 50)}.{random.randint(1, 50)}",
        ]

        base = f"Mozilla/5.0 ({random.choice(os_list)}) AppleWebKit/537.36 (KHTML, like Gecko) {random.choice(browsers)()}"
        return base

    @staticmethod
    def get_proxy_ip():
        import requests
        from bs4 import BeautifulSoup

        url = "https://free-proxy-list.net/en/"
        print(f"get_proxy_ip url: {url}")

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Akan melempar error jika gagal request

        soup = BeautifulSoup(response.text, "html.parser")

        table = soup.find("table", class_="table table-striped table-bordered")
        if not table:
            raise ValueError("Tabel tidak ditemukan di halaman.")

        proxies = []
        rows = table.tbody.find_all("tr")
        for row in rows:
            cols = row.find_all("td")
            if len(cols) < 8:
                continue  # Skip jika kolom tidak lengkap

            proxy = {
                "proxy_ip": f"{cols[0].text.strip()}:{cols[1].text.strip()}",
                "ip": cols[0].text.strip(),
                "port": cols[1].text.strip(),
                # "code": cols[2].text.strip(),
                "country": cols[3].text.strip(),
                # "anonymity": cols[4].text.strip(),
                # "google": cols[5].text.strip(),
                # "https": cols[6].text.strip(),
                # "last_checked": cols[7].text.strip(),
            }
            proxies.append(proxy)

            # validation = ['indonesia']
            # if proxy['country'].lower() in validation:
            #     proxies.append(proxy)

        return proxies

    @staticmethod
    def get_proxy_ip_random(proxies=None):
        import random

        if proxies is None:
            proxies = Helpers.get_proxy_ip()
        print(f"proxies: {proxies}")

        result = random.choice(proxies)
        print(f"get_proxy_ip_random: {result}")

        return result

    @staticmethod
    def normalization_unusual_char(text):
        import re

        if text is not None:
            text = text.replace('\n', ' ')

            text = re.sub(r'[\u2028\u2029\u00a0]', '', text)
            text = re.sub(r'\s+', ' ', text)

        return text

    @staticmethod
    def normalization_text(text):
        text = Helpers.normalization_unusual_char(text)
        return text
