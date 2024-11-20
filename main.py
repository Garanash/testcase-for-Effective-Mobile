import os

from classes import Book, Biblioteka

my_bib: Biblioteka = Biblioteka()
my_bib.load_biblio()

while True:
    """
    Основной код программы, в бесконечном цикле считываем команды от пользователя через стандартный поток ввода
    Результаты обработки команд так же выводим с стандартный поток вывода
    """
    os.system('cls' if os.name == 'nt' else 'clear')  # необходимо для обновления консоли(что бы было красиво)
    command = input("Выберите опцию управления: \n"
                    "1: Добавить книгу в библиотеку\n"
                    "2: Удалить книгу из библиотеки\n"
                    "3: Найти книгу по title, author или year\n"
                    "4: Показать список всех книг\n"
                    "5: Изменить статус книги по id\n"
                    "6: Выйти из приложения\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    match command:
        case '1':
            try:
                print('Ввиду ограничений вводите название одним словом(без пробелов)\n'
                      'Фио автора так же одним словом(без пробелов)')
                title, author, year = input('Введите Название книги, Автора и год издания\n').split()
                my_bib.add_book(Book(title, author, year))
                print('Книга успешно добавлена')
            except ValueError:
                print('Вы ввели некорректные данные, попробуйте еще раз')
        case '2':
            try:
                book_id = input('Введите id книги которую нужно удалить\n')
                my_bib.pop_book(book_id)
            except ValueError:
                print('Вы ввели некорректные данные, попробуйте еще раз')
        case '3':
            try:
                search = input('Введите Название книги, Автора или год издания для поиска\n')
                my_bib.find_book(search)
            except ValueError:
                print('Вы ввели некорректные данные, попробуйте еще раз')
        case '4':
            my_bib.all_books()
        case '5':
            try:
                book_id = input('Введите id книги которой нужно поменять статус\n')
                my_bib.set_new_status_book(book_id)
            except ValueError:
                print('Вы ввели некорректные данные, попробуйте еще раз')
        case '6':
            print('Всего доброго')
            quit(1)
    my_bib.update_biblio()
    input('Для возврата в предыдущее меню нажмите enter')
