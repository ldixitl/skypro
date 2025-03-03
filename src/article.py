# Ссылка на пост на сайте содержит id этого поста, по которому надо быстро найти данные, относящиеся к нему.
# Необходимо создать класс, который реализует структуру хранения записей постов и позволит быстро получать нужную запись по id.
# При появлении нового поста данные по этому посту добавляются в эту структуру.


class Article:
    """Класс для хранения статьи."""

    article_id: int

    articles = dict()  # Атрибут на уровне класса для хранения всех статей

    def __init__(self, title: str, content: str) -> None:
        """Конструктор для статьи."""
        self.article_id = self.get_new_id()
        self.title = title
        self.content = content

    def get_new_id(self) -> int:
        """Метод для получения ID следующей статьи."""
        if len(self.articles) > 0:
            return max(self.articles.keys()) + 1
        return 1

    @classmethod
    def insert(cls, title: str, content: str):
        """Метод для создания и добавления статьи."""
        new_article = cls(title, content)
        cls.articles[new_article.article_id] = new_article
        return new_article

    @classmethod
    def search(cls, article_id: int):
        """Метод для поиска статьи по ID."""
        # return cls("test3", "test3")
        return cls.articles[article_id]


if __name__ == "__main__":
    new_article_1 = Article.insert("test1", "test1text")
    print(new_article_1.article_id)

    new_article_2 = Article.insert("test2", "test2text")
    print(new_article_2.article_id)
