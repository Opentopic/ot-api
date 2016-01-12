"""
Models channels.
"""

from booby import fields
from ot_api.base import OpentopicModel

from .parsers import parse_recommendationnews


class RecommendationNews(OpentopicModel):
    """
    Represent single `RecommendationNews` object.

    :param pk: unique news index value
    :param title: title of the news, it's title that news was published with
    :param description: description (body) of the news, it's description that news was published with
    :param description_plain: same as description, except that html is excluded
    :param url: url of the news, depends on publication options might be original url or blog url
     if news was already published to blog platform (wordpress), also depends on options might be short or long version
    :param image: url to original image attached to news
    :param keywords: keywords for content
    :param popularity: total popularity from social medias
    :param twitter_count: number of twitter shares
    :param facebook_like_count: number of facebook shares
    :param linkedin_share_count: number of linkedin shares
    :param googleplus_share_count: number of g+ shares
    :param sorting_factor: int value represent opentopic algo score
    """

    pk = fields.String()
    title = fields.String()
    description = fields.String()
    description_plain = fields.String()
    url = fields.String()
    image = fields.String()
    keywords = fields.String()

    popularity = fields.Integer()
    twitter_count = fields.Integer()
    facebook_like_count = fields.Integer()
    linkedin_share_count = fields.Integer()
    googleplus_share_count = fields.Integer()

    sorting_factor = fields.Float()

    parser = parse_recommendationnews

    def __str__(self):
        return self.title
