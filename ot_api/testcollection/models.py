"""
Test collection used only for testing purpose
"""
import json

from booby import fields
from ot_api.base import OpentopicModel

from .parsers import test_parser


def _generate_test_object(i):
    """
    :return: dist with test object
    """
    return {
        'id': i,
        'name': 'test_name{0}'.format(str(i))
    }


def _generate_test_objects(offset, limit):
    """
    generate list with test objects
    :return: list iwth generated objects
    """
    return [_generate_test_object(i) for i in range(offset, limit)]


def _generate_test_json(offset, limit, next_page=None):
    """
    Generat test json
    :return: dict
    """
    results = list(_generate_test_objects(offset, limit))
    json_response = {
        'results': results,
        'next': next_page,
        'count': len(results),
        'previous': None
    }

    return json_response


class TestCollectionModel(OpentopicModel):
    """
    Represent recommendation object.
    TODO: link to documentation
    """

    pk = fields.Integer()
    name = fields.String()

    parser = test_parser

    @property
    def id(self):
        return self.pk

    def __str__(self):
        return self.name
