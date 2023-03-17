import os
import requests


class Posts:
    def __init__(self, post_id, title, tags, categories, content):
        self.id = post_id
        self.title = title
        self.tags = tags
        self.categories = categories
        self.content = content
