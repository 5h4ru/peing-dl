import requests
import time
import json
import csv
import logging
import pandas


class PeingAPI:
    """
    Peing の API を叩くクラス？
    """

    PEING_API_ENDPOINT = "https://peing.net/api/v2/"
    ENDPOINT = "https://peing.net/api/v2/questions/"

    def __init__(self, screen_name):
        self.screen_name = screen_name
        self.first_pasts_hash = ""
        self.total_pages = 0

    def get_item(self):
        data = []

        first_post_data = self._fetch_item_by_page(self.screen_name)[0]
        data.append(first_post_data)
        self.first_pasts_hash = first_post_data.get("uuid_hash")

        latest_data = self._fetch_posts_by_hash(self.first_pasts_hash, page=1)

        data.append(latest_data["items"])

        for first_items in latest_data["items"]:
            data.append(first_items)

        paginte = latest_data["paginate"]

        self.total_pages = paginte.get("total_pages")

        print(self.total_pages)

        for page in range(2, self.total_pages + 1):
            next_data = self._fetch_posts_by_hash(self.first_pasts_hash, page=page)

            data.append(next_data["items"][0])

            print(page)

            time.sleep(1)

        return data

    def _fetch_item_by_page(self, page: int = 1) -> list:
        get_params = {"type": "answered", "account": self.screen_name, "page": page}
        res = requests.get(PeingAPI.PEING_API_ENDPOINT + "items/", params=get_params)
        return res.json()["items"]

    def _fetch_posts_by_hash(self, uuid_hash: str, page: int = 1) -> list:
        post_hash = uuid_hash
        res = requests.get(
            f"{PeingAPI.ENDPOINT}{post_hash}/latests", params={"page": page}
        )
        return res.json()

    def save_json(self, data: list, file_name: str):
        with open(f"{file_name}.json", "w") as f:
            json.dump(data, f, indent=4)

    def save_csv(self, data: list, file_name: str):
        for column in data:
            d = pandas.json_normalize(column)

            # 改行をエスケープ
            d["body"] = d["body"].str.replace("\n", "\\n")
            d["answer_body"] = d["answer_body"].str.replace("\n", "\\n")

            d.to_csv(f"{file_name}.csv", mode="a", header=False, index=False)