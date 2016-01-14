import json
import unittest
from .parsers import parse_channelnews
from .collections import ChannelNewsCollection


JSON_OBJECT = """
{
    "id": 123,
    "news_index": "AVER72uWFut5Shklwyv4",
    "title": "Profiling Python using cProfile: a concrete case",
    "description": "Test Description",
    "extra_message": "Profiling Python using cProfile",
    "url": "https://goo.gl/32",
    "is_published": true,
    "is_scheduled": false
}
"""


class TestChannelNews(unittest.TestCase):
    """Basic tests for channels"""

    def test_parser(self):
        """
        Test if parser function return correct dict
        """
        json_object = json.loads(JSON_OBJECT)
        parsed_object = parse_channelnews(json_object)

        self.assertEqual(parsed_object['news_index'], 'AVER72uWFut5Shklwyv4')
        self.assertEqual(parsed_object['title'], 'Profiling Python using cProfile: a concrete case'),
        self.assertEqual(parsed_object['description'], "Test Description")
        self.assertEqual(parsed_object['extra_message'], "Profiling Python using cProfile")
        self.assertEqual(parsed_object['url'], 'https://goo.gl/32')
        self.assertTrue(parsed_object['is_published'])
        self.assertFalse(parsed_object['is_scheduled'])

    def test_url(self):
        """
        Test if correct urls is constructed
        """
        channel_news = ChannelNewsCollection(account_name='dev', channel_pk=5)
        self.assertEqual(
            channel_news.url,
            'https://new.opentopic.com/dev/rest-api/channels/5/news/'
        )
