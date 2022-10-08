from app.logic.categorization import Categorizer


def preprocess_post(post):
    for tag in post.tags:
        kw = Categorizer.categorize(word=tag)
        if not kw:
            print(f"Not categorized tag: {tag}")
    return post
