class Book:
    """
    Класс описывающий книгу
    """
    _id_counter: int = 1

    def __init__(self, title: str, author: str, year: str) -> None:
        """
        Инициализация класса, id задается автоматически, по умолчанию статус 'в наличии'
        :param title: Название книги
        :param author: Автор
        :param year: Год издания
        """
        self.id: int = Book._id_counter
        Book._id_counter += 1
        self.title: str = title
        self.author: str = author
        self.year: str = year
        self.status: str = 'в наличии'

    def __repr__(self) -> str:
        """ Возвращает строку 'как будет выглядеть объект при обращении к нему'"""
        return f"{self.id} {self.title} {self.author} {self.year} {self.status}"

    def __str__(self) -> str:
        """ Возвращает строку 'как будет выглядеть объект при трансформации в str'"""
        return f"{self.id} {self.title} {self.author} {self.year} {self.status}"


class Biblioteka:
    """Класс библиотеки"""

    def __init__(self) -> None:
        """При инициализации создается пустой список остатков"""
        self.reserve: list = []

    def add_book(self, book: Book) -> None:
        """Функция для добавления книги в библиотеку"""
        self.reserve.append(book)

    def pop_book(self, book_id: str) -> None:
        """Функция для удаления книги из библиотеки, если книги нет то пишет что книги нет"""
        pop_item: int = -1
        for i in range(len(self.reserve)):
            if self.reserve[i].id == int(book_id):
                pop_item = i
        if pop_item != -1:
            print(f'Была удалена книга {self.reserve.pop(pop_item)}')
        else:
            print(f'книги с id {book_id} нет в библиотеке')

    def set_new_status_book(self, book_id: str) -> None:
        """Функция изменения статуса книги на 'выдана'"""
        set_status_item: int = -1
        for index in range(len(self.reserve)):
            if self.reserve[index].id == int(book_id):
                set_status_item = index
        if set_status_item != -1:
            if self.reserve[set_status_item].status == 'выдана':
                print('Книга уже выдана')
            else:
                self.reserve[set_status_item].status = 'выдана'
                print(f'Книга {self.reserve[set_status_item]} выдана')
        else:
            print(f'книги с id {book_id} нет в библиотеке')

    def find_book(self, search: str) -> bool:
        """Функция поиска книг по библиотеке"""
        flag: bool = False
        for book in self.reserve:
            if book.title == search or book.author == search or book.year == search:
                print(f'Найдена книга {book}')
                flag = True
        if not flag:
            print('К сожалению по Вашему запросу книг не найдено')
        return flag

    def all_books(self) -> None:
        """Функция выводит список всех книг в библиотеке"""
        flag: bool = False
        for book in self.reserve:
            print(book)
            flag = True
        if not flag:
            print('Книг в библиотеке нет')

    def update_biblio(self) -> None:
        """Функция записывает состояние библиотеки в файл"""
        with open('database.txt', 'w') as file:
            for elem in self.reserve:
                file.write(str(elem))
                file.write('\n')

    def load_biblio(self) -> None:
        """Функция загружает последнее состояние библиотеки"""
        with open('database.txt', 'r') as file:
            for elem in file.readlines():
                title, author, year = elem.split()[1:4]
                self.reserve.append(Book(title, author, year))
                if elem.split()[4] != 'в':
                    self.reserve[-1].status = 'выдана'
