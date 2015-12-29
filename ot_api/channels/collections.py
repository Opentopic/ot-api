from ot_api.base import OpentopicCollection

from .endpoints import CHANNEL_ENDPOINT
from .models import Channel


class ChannelCollection(OpentopicCollection):
    """
    Represent list of channels
    TODO: link to documentation
    """
    model = Channel
    endpoint_name = CHANNEL_ENDPOINT
