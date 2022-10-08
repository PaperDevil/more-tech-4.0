class Article:
    def __init__(self, title: str, text: str, tag: str, date: str):
        self.title = title
        self.text = text
        self.tag = tag
        self.date = date

    def __str__(self) -> str:
        return f'tag \n {self.tag} \n' \
               f'title \n {self.title} \n' \
               f'text \n {self.text} \n' \
               f'date \n {self.date} \n'
