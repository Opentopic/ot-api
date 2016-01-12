"""
Models for recommendation.
"""

from booby import fields
from ot_api.base import OpentopicModel

from .parsers import parse_recommendation


class Recommendation(OpentopicModel):
    """
    Represent single `Recommendation` object

    :param pk: id of `Recommendation`
    :param name: name of `Recommendation`
    """

    pk = fields.Integer()
    name = fields.String()

    parser = parse_recommendation

    @property
    def id(self):
        return self.pk

    def __str__(self):
        return self.name
