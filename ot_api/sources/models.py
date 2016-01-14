from booby import fields
from ot_api.base import OpentopicModel

from .parsers import parse_source


class Source(OpentopicModel):
    """
    Represent single `Source` object.

    :param pk: id of `Source`
    :param source_type: Type of the source
    :param name: Name of the source
    """

    pk = fields.Integer()
    source_type = fields.String()
    name = fields.String()

    parser = parse_source

    @property
    def id(self):
        return self.pk

    def __str__(self):
        return self.name
