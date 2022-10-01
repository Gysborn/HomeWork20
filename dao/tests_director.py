from unittest.mock import MagicMock
import pytest

from dao.director import DirectorDAO
from service.director import DirectorService
from setup_db import db


@pytest.fixture
def director_dao():
    director_dao = DirectorDAO(db)
    director_dao.get_all = MagicMock(return_value=[{'director': 1}, {'director': 2}])
    director_dao.get_one = MagicMock(return_value={'director': 1})
    director_dao.create = MagicMock(return_value="201")
    director_dao.delete = MagicMock(return_value="deleted")
    director_dao.update = MagicMock(return_value="204")
    return director_dao


def test_director_service(director_dao):
    ds = DirectorService(director_dao)
    assert ds.get_all() == [{'director': 1}, {'director': 2}]
    assert ds.get_one(1) == {'director': 1}
    assert ds.create(1) == "201"
    assert ds.delete(1) == "deleted"
    assert ds.update(1) == "204"
