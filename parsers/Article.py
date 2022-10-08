class Article:
    """
    Общая модель всех статей
    """

    def __init__(self, title: str, text: str, tag: str):
        self.title = title
        self.text = text
        self.tag = tag

    def __str__(self) -> str:
        return f'tag\n {self.tag} \n' \
               f'title\n {self.title} \n' \
               f'text \n {self.text} \n'
