import requests


class Movies:
    def __init__(self, movie_id, title, year, description, rating, ranking, review, img_url):
        self.id = movie_id
        self.title = title
        self.year = year
        self.description = description
        self.rating = rating
        self.ranking = ranking
        self.review = review
        self.img_url = img_url

    def edit(self, movie_id):
        pass
