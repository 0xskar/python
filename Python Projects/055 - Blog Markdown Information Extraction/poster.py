import os
import requests


class PostInfo:
    """ Get post information, connect to strapi, post information """
    def __init__(self, title, categories, tags, content):
        self.api_key = os.environ['STRAPI_API_KEY']
        self.endpoint = "http://192.168.0.35:1337/api/articles"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}"
        }
        self.title = title
        self.categories = categories
        self.tags = tags
        self.content = content
        self.post()

    def post(self):
        schema = {
            "data": {
                "title": self.title,
                "content": self.content,
                "categories": self.categories,
                "tags": self.tags
            }
        }
        r = requests.post(url=self.endpoint, headers=self.headers, json=schema)
        print(r.status_code)
