from app.logic.categorization import Categorizer
from rutermextract import TermExtractor


def preprocess_post(post):
    kw = Categorizer.categorize(word=post.tags)
    if not kw:
        print(f"Not categorized tag: {post.tags}")
    post.tags = [post.tags, *kw]
    term_extractor = TermExtractor()
    post.keywords = [i for i in term_extractor(post.text)]
    return post
