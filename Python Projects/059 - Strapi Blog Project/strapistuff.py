import os
import requests


class Posts:
    def __init__(self, title, tags, categories, content):
        self.title = title
        self.tags = tags
        self.categories = categories
        self.content = content
