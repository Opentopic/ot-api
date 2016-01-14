import json
import unittest
from .parsers import parse_source


JSON_OBJECT = """
{
    "url": "http://new.opentopic.com/dev/rest-api/sources/2567/",
    "id": 2567,
    "source_type": "facebook",
    "name": "Audi Polska",
    "image": null
}
"""


class TestRecommendation(unittest.TestCase):
    """Basic tests for recommendations"""

    def test_parser(self):
        """
        Test if parser function return correct dict
        """
        json_object = json.loads(JSON_OBJECT)
        parsed_object = parse_source(json_object)

        self.assertEqual(parsed_object['pk'], 2567)
        self.assertEqual(parsed_object['name'], 'Audi Polska')
        self.assertEqual(parsed_object['source_type'], 'facebook')
