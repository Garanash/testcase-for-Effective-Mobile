import unittest

from classes import Biblioteka, Book


class TestBiblio(unittest.TestCase):

    def test_add(self):
        my_bibl = Biblioteka()
        new_book = Book('Название', 'Автор', '2024')
        my_bibl.add_book(new_book)
        self.assertEqual(my_bibl.reserve[-1], new_book)

    def test_del(self):
        my_bibl = Biblioteka()
        new_book = Book('Название', 'Автор', '2024')
        my_bibl.pop_book(1)
        self.assertNotIn(new_book, my_bibl.reserve)

    def test_search(self):
        my_bibl = Biblioteka()
        new_book = Book('Название', 'Автор', '2024')
        flag = my_bibl.find_book('2024')
        self.assertEqual(flag, False)
        my_bibl.add_book(new_book)
        flag = my_bibl.find_book('2024')
        self.assertEqual(flag, True)

    def test_status(self):
        my_bibl = Biblioteka()
        new_book = Book('Название', 'Автор', '2024')
        my_bibl.add_book(new_book)
        print(my_bibl.reserve)
        my_bibl.set_new_status_book(4)
        print(my_bibl.reserve)
        self.assertEqual(my_bibl.reserve[-1].status, 'выдана')


if __name__ == '__main__':
    unittest.main()
