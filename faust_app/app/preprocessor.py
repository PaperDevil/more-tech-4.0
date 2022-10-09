import pymorphy2 as pymorphy2
from app.logic.categorization import Categorizer
from rutermextract import TermExtractor

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def get_text_in_normal_form(text):
    analyzer = pymorphy2.MorphAnalyzer()
    normalized_text_list = []
    tokens = word_tokenize(text)
    for token in tokens:
        normalized_text_list.append(analyzer.parse(token)[0].normal_form)
    return normalized_text_list


def filter_text(text):
    word_list = get_text_in_normal_form(text)
    russian_stopwords = stopwords.words('russian')
    filtered_words = [word for word in word_list if word not in russian_stopwords]
    return ' '.join(filtered_words)


def preprocess_post(post):
    kw = Categorizer.categorize(word=post.tags)
    if not kw:
        print(f"Not categorized tag: {post.tags}")
    post.tags = [post.tags, *kw]
    term_extractor = TermExtractor()
    filtered_text = filter_text(post.text)
    post.keywords = [i for i in term_extractor(filtered_text)]
    return post
