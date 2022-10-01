from unittest.mock import MagicMock
import pytest

from dao.movie import MovieDAO
from service.movie import MovieService
from setup_db import db


@pytest.fixture
def movie_dao():
	movie_dao = MovieDAO(db)
	movie_dao.get_all = MagicMock(return_value=[{'movie': 1}, {'movie': 2}])
	movie_dao.get_one = MagicMock(return_value={'movie': 1})
	movie_dao.create = MagicMock(return_value="201")
	movie_dao.delete = MagicMock(return_value="deleted")
	movie_dao.update = MagicMock(return_value="204")
	return movie_dao


def test_movie_service(movie_dao):
	ms = MovieService(movie_dao)
	assert ms.get_all() == [{'movie': 1}, {'movie': 2}]
	assert ms.get_one(1) == {'movie': 1}
	assert ms.create(1) == "201"
	assert ms.delete(1) == "deleted"
	assert ms.update(1) == "204"




