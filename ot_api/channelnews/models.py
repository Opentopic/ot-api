"""
Models channels.
"""

from booby import fields
from ot_api.base import OpentopicModel

from .parsers import parse_channelnews


class ChannelNews(OpentopicModel):
    """
    Represent single `ChannelNews` object.

    :param pk: channel news id
    :param news_index: unique news index value
    :param title: title of the news, it's title that news was published with
    :param description: description (body) of the news, it's description that news was published with
    :param extra_message: extra_message of the news, TODO: ? what is that ?
    :param url: url of the news, depends on publication options might be original url or blog url
     if news was already published to blog platform (wordpress), also depends on options might be short or long version
    :param is_published: bool value describing if news is already published (with success)
    :param is_scheduled: bool value describing if news is scheduled to be publish
    """

    pk = fields.Integer()
    news_index = fields.String()
    title = fields.String()
    description = fields.String()
    extra_message = fields.String()
    url = fields.String()
    is_published = fields.Boolean()
    is_scheduled = fields.Boolean()

    parser = parse_channelnews

    def __str__(self):
        return self.title
