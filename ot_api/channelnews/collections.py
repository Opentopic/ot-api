__all__ = ['ChannelNewsCollection']


from ot_api.base import OpentopicCollection
from ot_api.exceptions import NotAvailableException
from ot_api.utils import build_endpoint_url

from .endpoints import CHANNELNEWS_ENDPOINT
from .models import ChannelNews


class ChannelNewsCollection(OpentopicCollection):

    model = ChannelNews
    endpoint_name = CHANNELNEWS_ENDPOINT
    init_params = ('channel_pk',)

    @property
    def url(self):
        return build_endpoint_url(
            account_name=self.account_name,
            endpoint_name=self.endpoint_name.format(channel_pk=self.channel_pk)
        )

    def get_url(self, object_pk):
        raise NotAvailableException
