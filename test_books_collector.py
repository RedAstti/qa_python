    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

import pytest
from main import BooksCollector

class TestBooksCollector:

    @pytest.mark.parametrize("book_name", ["1984", "Война и мир", "Шерлок Холмс"])
    def test_add_new_book_success(self, collector, book_name):
        """Проверка, что книга успешно добавляется в коллекцию"""
        collector.add_new_book(book_name)
        assert book_name in collector.get_books_genre()

    def test_add_new_book_duplicate_not_added(self, collector):
        """Проверка, что дубликат книги не добавляется"""
        collector.add_new_book("Мастер и Маргарита")
        collector.add_new_book("Мастер и Маргарита")
        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_too_long_name_not_added(self, collector):
        """Проверка, что книга с названием длиннее 40 символов не добавляется"""
        long_name = "Очень длинное название книги, которое точно больше сорока символов"
        collector.add_new_book(long_name)
        assert long_name not in collector.get_books_genre()

    def test_set_book_genre_success(self, collector):
        """Проверка успешной установки жанра книги"""
        collector.add_new_book("1984")
        collector.set_book_genre("1984", "Фантастика")
        assert collector.get_book_genre("1984") == "Фантастика"

    def test_set_book_genre_invalid_genre_not_set(self, collector):
        """Проверка, что нельзя установить несуществующий жанр"""
        collector.add_new_book("Оно")
        collector.set_book_genre("Оно", "Поэзия")
        assert collector.get_book_genre("Оно") == ""

    def test_get_books_with_specific_genre_returns_correct_books(self, collector):
        """Проверка получения списка книг определённого жанра"""
        collector.add_new_book("12 стульев")
        collector.add_new_book("Ревизор")
        collector.set_book_genre("12 стульев", "Комедии")
        collector.set_book_genre("Ревизор", "Комедии")
        result = collector.get_books_with_specific_genre("Комедии")
        assert "12 стульев" in result and "Ревизор" in result

    def test_get_books_for_children_excludes_age_restricted(self, collector):
        """Проверка, что книги с возрастным рейтингом не попадают в список для детей"""
        collector.add_new_book("Оно")
        collector.add_new_book("Король Лев")
        collector.set_book_genre("Оно", "Ужасы")
        collector.set_book_genre("Король Лев", "Мультфильмы")
        result = collector.get_books_for_children()
        assert "Оно" not in result and "Король Лев" in result

    def test_add_book_in_favorites_success(self, collector):
        """Проверка добавления книги в избранное"""
        collector.add_new_book("Шерлок Холмс")
        collector.add_book_in_favorites("Шерлок Холмс")
        assert "Шерлок Холмс" in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_invalid_book_not_added(self, collector):
        """Проверка, что нельзя добавить в избранное книгу, которой нет в коллекции"""
        collector.add_book_in_favorites("Несуществующая книга")
        assert "Несуществующая книга" not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_success(self, collector):
        """Проверка удаления книги из избранного"""
        collector.add_new_book("Властелин колец")
        collector.add_book_in_favorites("Властелин колец")
        collector.delete_book_from_favorites("Властелин колец")
        assert "Властелин колец" not in collector.get_list_of_favorites_books()

