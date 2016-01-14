from ot_api.base import OpentopicCollection

from .endpoints import SOURCE_ENDPOINT
from .models import Source


class SourceCollection(OpentopicCollection):
    """
    Represent list of sources
    """
    model = Source
    endpoint_name = SOURCE_ENDPOINT
