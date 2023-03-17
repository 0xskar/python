import glob
from frontmatter import Frontmatter
from poster import PostInfo

folder_path = "E:\Documents\GitHub\\0xskar.github.io\_posts\\"


# Extract information from the file
def extract_info(file_path):
    post = Frontmatter.read_file(file_path)
    title = post['attributes']['title']
    try:
        categories = post['attributes']['categories']
    except KeyError:
        categories = post.get('categories')
    try:
        tags = post['attributes']['tags']
    except KeyError:
        tags = post.get('tags')
    content = post.get('body')
    return title, categories, tags, content


# Read all the markdown files in directory
for file_path in glob.glob(folder_path + '/*.md'):
    title, categories, tags, content = extract_info(file_path)
    PostInfo(title, categories, tags, content)
