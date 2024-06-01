# testing/book_test.py

from lib.book import Book

class TestBook:
    def test_has_title_and_page_count(self):
        book = Book("And Then There Were None", 272)
        assert book.title == "And Then There Were None"
        assert book.page_count == 272
