import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    """Фикстура для инициализации BooksCollector"""
    return BooksCollector()
