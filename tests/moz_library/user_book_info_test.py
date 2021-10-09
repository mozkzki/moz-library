from moz_library.user import User
from moz_library.reserved_book import ReservedBook
from moz_library.reserved_books import ReservedBooks
from moz_library.user_book_info import UserBookInfo


class TestUserBookInfo:
    def test_to_string(self):
        reserved_books = ReservedBooks()

        book = ReservedBook(
            "ご用意できました", "", "title", "kind", "yoyaku_date", "torioki_date", "receive"
        )
        reserved_books.append(book)

        info = UserBookInfo(User('{"disp_name":"hoge"}'), reserved_books=reserved_books)
        print(info)
