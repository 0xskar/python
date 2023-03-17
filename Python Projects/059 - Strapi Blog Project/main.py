import os

import requests
from flask import Flask, render_template
from strapistuff import Posts

app = Flask(__name__)

# strapi CMS
api_key = os.environ['STRAPI_API_KEY']
url_endpoint = "http://192.168.0.35:1337/api/articles"
headers = {
    "Authorization": f"Bearer {api_key}"
}

# Get the recent 25 posts from strapi
params = {
    "sort": "id:desc"
}
r = requests.get(url=url_endpoint, headers=headers, params=params)
print(r.status_code)
data = r.json()['data']
blog_posts = []
for post in data:
    p_id = post['id']
    title = post['attributes']['title']
    tags = post['attributes']['tags']
    categories = post['attributes']['categories']
    content = post['attributes']['content']
    blog_posts.append(Posts(p_id, title, tags, categories, content))


@app.route("/")
def index():
    return render_template("index.html", posts=blog_posts)


@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/post/<int:post_id>")
def post(post_id):
    print(post_id)
    for post in blog_posts:
        if post.id == post_id:
            title = post.title
            content = post.content
            tags = post.tags
            categories = post.categories

    return render_template("post.html", title=title, content=content, tags=tags, categories=categories)


@app.route("/contact.html")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=80)
