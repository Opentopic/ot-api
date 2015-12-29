from ot_api.base import OpentopicCollection

from .models import TestCollectionModel


class TestCollection(OpentopicCollection):
    """
    Represent list of recommendations
    TODO: link to documentation
    """
    model = TestCollectionModel
    endpoint_name = 'https://just.a.test.collection.org/rest-api/test/'
