from booby import fields
from ot_api.base import OpentopicModel

from .parsers import parse_channel


class Channel(OpentopicModel):
    """
    Represent single `Channel` object.

    :param pk: id of `Channel`
    :type pk:
    :param name: name of the channel
    :param channel_type: one of the value: mailchimp, facebook, twitter
    """

    pk = fields.Integer()
    name = fields.String()
    channel_type = fields.String()

    parser = parse_channel

    @property
    def id(self):
        return self.pk

    def __str__(self):
        return self.name
