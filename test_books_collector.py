import pytest

class TestBooksCollector:
    # --- add_new_book ---
    @pytest.mark.parametrize("book_name", ["1984", "Война и мир", "Шерлок Холмс"])
    def test_add_new_book_success(self, collector, book_name):
        """Проверка, что книга успешно добавляется в коллекцию"""
        collector.add_new_book(book_name)
        assert book_name in collector.books_genre

    def test_add_new_book_duplicate_not_added(self, collector):
        """Проверка, что дубликат книги не добавляется"""
        collector.books_genre["Мастер и Маргарита"] = ""
        collector.add_new_book("Мастер и Маргарита")
        assert len(collector.books_genre) == 1

    @pytest.mark.parametrize("book_name", ["K", "K" * 23, "K" * 40])
    def test_add_new_book_valid_length_success(self, collector, book_name):
        """Метод add_new_book добавляет книгу с названием длиной от 1 до 40 символов"""
        collector.add_new_book(book_name)
        assert book_name in collector.books_genre

    @pytest.mark.parametrize("book_name", ["", "K" * 41, "K" * 100])
    def test_add_new_book_invalid_length_not_added(self, collector, book_name):
        """Метод add_new_book не добавляет книгу, если длина названия < 1 или > 40"""
        collector.add_new_book(book_name)
        assert book_name not in collector.books_genre

    # --- set_book_genre ---
    def test_set_book_genre_success(self, collector):
        """Проверка успешной установки жанра книги"""
        collector.books_genre["1984"] = ""
        collector.set_book_genre("1984", "Фантастика")
        assert collector.books_genre["1984"] == "Фантастика"

    def test_set_book_genre_invalid_genre_not_set(self, collector):
        """Проверка, что нельзя установить несуществующий жанр"""
        collector.books_genre["Оно"] = ""
        collector.set_book_genre("Оно", "Поэзия")
        assert collector.books_genre["Оно"] == ""

    # --- get_book_genre ---
    def test_get_book_genre_returns_correct_genre(self, collector):
        """Метод get_book_genre возвращает жанр по названию книги"""
        collector.books_genre["Ревизор"] = "Комедии"
        assert collector.get_book_genre("Ревизор") == "Комедии"

    # --- get_books_with_specific_genre ---
    def test_get_books_with_specific_genre_returns_correct_books(self, collector):
        """Метод get_books_with_specific_genre возвращает книги с заданным жанром"""
        collector.books_genre = {
            "12 стульев": "Комедии",
            "Ревизор": "Комедии",
            "1984": "Фантастика"
        }
        result = collector.get_books_with_specific_genre("Комедии")
        assert set(result) == {"12 стульев", "Ревизор"}

    # --- get_books_for_children ---
    def test_get_books_for_children_excludes_age_restricted(self, collector):
        """Метод get_books_for_children исключает книги с возрастным рейтингом"""
        collector.books_genre = {
            "Оно": "Ужасы",
            "Король Лев": "Мультфильмы"
        }
        result = collector.get_books_for_children()
        assert "Оно" not in result and "Король Лев" in result

    # --- add_book_in_favorites ---
    def test_add_book_in_favorites_success(self, collector):
        """Метод add_book_in_favorites добавляет книгу в избранное"""
        collector.books_genre["Шерлок Холмс"] = "Детективы"
        collector.add_book_in_favorites("Шерлок Холмс")
        assert "Шерлок Холмс" in collector.favorites

    def test_add_book_in_favorites_invalid_book_not_added(self, collector):
        """Метод add_book_in_favorites не добавляет книгу, если её нет в словаре"""
        collector.add_book_in_favorites("Несуществующая книга")
        assert "Несуществующая книга" not in collector.favorites

    # --- delete_book_from_favorites ---
    def test_delete_book_from_favorites_success(self, collector):
        """Метод delete_book_from_favorites удаляет книгу из избранного"""
        collector.favorites = ["Властелин колец"]
        collector.delete_book_from_favorites("Властелин колец")
        assert "Властелин колец" not in collector.favorites

    # --- get_list_of_favorites_books ---
    def test_get_list_of_favorites_books_returns_list(self, collector):
        """Метод get_list_of_favorites_books возвращает список избранных книг"""
        collector.favorites = ["1984", "Война и мир"]
        result = collector.get_list_of_favorites_books()
        assert result == ["1984", "Война и мир"]

    # --- get_books_genre ---
    def test_get_books_genre_returns_full_dict(self, collector):
        """Метод get_books_genre возвращает словарь всех книг с жанрами"""
        collector.books_genre = {
            "1984": "Фантастика",
            "Ревизор": "Комедии"
        }
        result = collector.get_books_genre()
        assert result == {
            "1984": "Фантастика",
            "Ревизор": "Комедии"
        }

