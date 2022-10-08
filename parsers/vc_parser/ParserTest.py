from parsers.vc_parser.VcParser import VcParser

if __name__ == '__main__':
    vc_parser = VcParser()
    articles = vc_parser.get_data()
    for article in articles:
        print(article)
        print("---" * 30)
