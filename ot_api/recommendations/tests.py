import json
import unittest
from .parsers import parse_recommendation


JSON_OBJECT = """
{
    "id": 1,
    "avatar": 8,
    "name": "Games",
    "gender": null,
    "age_group": null,
    "role": null,
    "industry": null,
    "location": null,
    "interests": [
        489
    ],
    "story": null,
    "language": null,
    "interests_array": [
        {
            "id": 489,
            "name": "games"
        }
    ],
    "created_at": "2015-11-14T14:37:06Z",
    "popularity_level": null,
    "min_desc_length": null,
    "sorting_factor": null,
    "interests_tree": [
        {
            "sub_categories": [
                {
                    "sub_categories": [],
                    "selected": true,
                    "id": 489,
                    "name": "games"
                }
            ],
            "selected": false,
            "id": 15,
            "name": "hobbies and interests"
        }
    ],
    "hours_ago": 24
}
"""


class TestRecommendation(unittest.TestCase):
    """Basic tests for recommendations"""

    def test_parser(self):
        """
        Test if parser function return correct dict
        """
        json_object = json.loads(JSON_OBJECT)
        parsed_object = parse_recommendation(json_object)

        self.assertEqual(parsed_object['pk'], 1)
        self.assertEqual(parsed_object['name'], 'Games')
