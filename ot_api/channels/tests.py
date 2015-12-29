import json
import unittest
from .parsers import parse_channel


JSON_OBJECT = """
{
    "id": 8467,
    "name": "Sample Newsletter",
    "channel_type": "mailchimp"
}
"""


class TestChannel(unittest.TestCase):
    """Basic tests for channels"""

    def test_parser(self):
        """
        Test if parser function return correct dict
        """
        json_object = json.loads(JSON_OBJECT)
        parsed_object = parse_channel(json_object)

        self.assertEqual(parsed_object['pk'], 8467)
        self.assertEqual(parsed_object['name'], 'Sample Newsletter')
        self.assertEqual(parsed_object['channel_type'], 'mailchimp')
