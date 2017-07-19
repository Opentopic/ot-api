import json
import unittest
from .parsers import parse_recommendationnews


JSON_OBJECT = """
{
    "pk": "AVFaODSJOzQLcrw_vSbk",
    "url": "https://hbr.org/2015/11/how-to-support-employee-health-instead-of-sapping-it",
    "domain": "hbr.org",
    "created_at": "2015-11-30T21:06:51Z",
    "updated_at": "2015-12-07T11:57:48Z",
    "title": "How to Support Employee Health Instead of Sapping It",
    "description": "<p>How do you create a great place to work?</p>",
    "description_length": 7035,
    "description_plain": "How do you create a great place to work?",
    "paragraph_count": 24,
    "chars_lb_ratio": 286,
    "image_original": "https://hbr.org/resources/images/article_assets/2015/11/"
                      "nov15-30-dave-wheeler-work-life-850x478.jpeg",
    "has_image": true,
    "video": null,
    "has_video": false,
    "icon": "https://hbr.org/resources/images/favicon.ico",
    "author": "Ron Friedman",
    "tags": [
        "Employment",
        "Health",
        "Physical fitness",
        "Employee engagement",
        "Dieting"
    ],
    "summary": "Once, paying people well, offering interesting assignments, "
               "and providing recognition may have been enough. But the nature of work has changed.  "
               "Over the past decade, technological advances have enabled us to work at all hours, "
               "often at great expense to our sleep.  We’re surrounded by devices that make everything "
               "feel urgent, peppering us with distractions and contributing to an ongoing experience of stress.",
    "publication_date": "2015-11-30T00:00:00Z",
    "sources": [
        3894,
        83025,
        34243,
        83023,
        12248,
        4006,
        27803,
        18516,
        26970,
        53950
    ],
    "influencers": [
        34243,
        4006,
        452361,
        946531,
        18516,
        3894,
        12248,
        53950
    ],
    "influencer": {
        "source_type": "facebook",
        "image": null,
        "is_my_influencer": false,
        "name": "hbr",
        "id": 34243
    },
    "main_source": null,
    "topics": [],
    "featured": [],
    "featured_video": [],
    "published": [],
    "scheduled": [],
    "twitter_count": 0,
    "facebook_like_count": 3408,
    "linkedin_share_count": 2243,
    "googleplus_share_count": 0,
    "popularity": 5651,
    "sorting_factor": 12.0,
    "visited": [],
    "language": "en",
    "is_infographic": false,
    "is_draft": false,
    "kind": 0,
    "sites_allowed": null,
    "is_unread": null,
    "is_published": false,
    "is_scheduled": false,
    "is_featured": false,
    "is_featured_video": false,
    "can_be_deleted": null,
    "url_publish": "/dev/news/publish-manually/AVFaODSJOzQLcrw_vSbk/?target=117",
    "url_delete": "/dev/rest-api/recommendations/targets/news_delete/?news_pk=AVFaODSJOzQLcrw_vSbk",
    "trend": 0.0,
    "categories": [
        10
    ],
    "recommendation": {
        "basechannel": {
            "id": 6480,
            "name": "www.startupundvcnews.de Test",
            "channel_type": "wordpress",
            "channel_type_name": "Wordpress",
            "group_name": "Web",
            "group_id": 1
        },
        "schedule": {}
    }
}
"""


class TestRecommendation(unittest.TestCase):
    """Basic tests for recommendations"""

    def test_parser(self):
        """
        Test if parser function return correct dict
        """
        json_object = json.loads(JSON_OBJECT)
        parsed_object = parse_recommendationnews(json_object)

        self.assertEqual(parsed_object['pk'], 'AVFaODSJOzQLcrw_vSbk')
        self.assertEqual(parsed_object['title'], 'How to Support Employee Health Instead of Sapping It')
        self.assertEqual(parsed_object['description'], '<p>How do you create a great place to work?</p>')
        self.assertEqual(parsed_object['description_plain'], 'How do you create a great place to work?')
        self.assertEqual(
            parsed_object['url'], 'https://hbr.org/2015/11/how-to-support-employee-health-instead-of-sapping-it')
        self.assertEqual(
            parsed_object['image'],
            'https://hbr.org/resources/images/article_assets/2015/11/nov15-30-dave-wheeler-work-life-850x478.jpeg')
        self.assertEqual(parsed_object['popularity'], 5651)
        self.assertEqual(parsed_object['sorting_factor'], 12.0)
        self.assertEqual(parsed_object['twitter_count'], 0)
        self.assertEqual(parsed_object['facebook_like_count'], 3408)
        self.assertEqual(parsed_object['linkedin_share_count'], 2243)
        self.assertEqual(parsed_object['googleplus_share_count'], 0)
        self.assertEqual(parsed_object['keywords'],
                         'Employment, Health, Physical fitness, Employee engagement, Dieting')
