from ot_api.base import OpentopicCollection
from ot_api.exceptions import NotAvailableException
from ot_api.utils import build_endpoint_url

from .models import RecommendationNews
from .endpoints import RECOMMENDATIONNEWS_ENDPOINT


class RecommendationNewsCollection(OpentopicCollection):

    model = RecommendationNews
    endpoint_name = RECOMMENDATIONNEWS_ENDPOINT
    init_params = ('recommendation_pk',)

    @property
    def url(self):
        return build_endpoint_url(
            account_name=self.account_name,
            endpoint_name=self.endpoint_name.format(recommendation_pk=self.recommendation_pk)
        )

    def get_url(self, object_pk):
        raise NotAvailableException
