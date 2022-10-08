from app.logic.categorization import Categorizer


def preprocess_post(post):
    kw = Categorizer.categorize(word=post.tags)
    if not kw:
        print(f"Not categorized tag: {post.tags}")
    post.tags = [post.tags, kw]
    return post
