from ot_api.base import OpentopicCollection

from .endpoints import RECOMMENDATION_ENDPOINT
from .models import Recommendation


class RecommendationCollection(OpentopicCollection):
    """
    Represent list of recommendations
    TODO: link to documentation
    """
    model = Recommendation
    endpoint_name = RECOMMENDATION_ENDPOINT
