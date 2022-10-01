from unittest.mock import MagicMock
import pytest

from dao.genre import GenreDAO
from service.genre import GenreService
from setup_db import db


@pytest.fixture
def genre_dao():
    genre_dao = GenreDAO(db)
    genre_dao.get_all = MagicMock(return_value=[{'genre': 1}, {'genre': 2}])
    genre_dao.get_one = MagicMock(return_value={'genre': 1})
    genre_dao.create = MagicMock(return_value="201")
    genre_dao.delete = MagicMock(return_value="deleted")
    genre_dao.update = MagicMock(return_value="204")
    return genre_dao


def test_genre_service(genre_dao):
    gs = GenreService(genre_dao)
    assert gs.get_all() == [{'genre': 1}, {'genre': 2}]
    assert gs.get_one(1) == {'genre': 1}
    assert gs.create(1) == "201"
    assert gs.delete(1) == "deleted"
    assert gs.update(1) == "204"
