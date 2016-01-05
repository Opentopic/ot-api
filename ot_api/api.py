from functools import partialmethod
from pip._vendor import requests
from ot_api.endpoints import AUTHORIZATION_TOKEN
from ot_api.exceptions import AuthorizationException

from .recommendations.collections import RecommendationCollection
from .channels.collections import ChannelCollection
from .channelnews.collections import ChannelNewsCollection
from .recommendation_news.collections import RecommendationNewsCollection


class OpentopicApiMeta(type):
    """
    Meta class for OpentpicAPI, just to make things a bit easier at the end
    """

    def __init__(cls, name, bases, nmspc):
        super(OpentopicApiMeta, cls).__init__(name, bases, nmspc)
        # iterate over all collections and make methods for them

        for collection in cls.COLLECTIONS:
            get_all_func_name = 'get_all_{0}'.format(collection.collection_name)
            get_func_name = 'get_{0}'.format(collection.collection_name)

            setattr(cls, get_all_func_name, partialmethod(cls._get_all, collection=collection))
            setattr(cls, get_func_name, partialmethod(cls._get, collection=collection))


class OpentopicApi(object, metaclass=OpentopicApiMeta):
    """
    Main opentopic api client class that you should use for communication with service.

    `COLLECTIONS`: tuple of collection classes supported by api client

    Example:
    api = OpentopicApi(account_name='test_account', username='test_user', password='test_pass')
    api.recommendations_all()
    """

    # TODO: collect all collections automatically
    COLLECTIONS = (
        RecommendationCollection,
        ChannelCollection,
        ChannelNewsCollection,
        RecommendationNewsCollection
    )

    def __init__(self, account_name, username, password):
        self.account_name = account_name
        self.username = username
        self.password = password

        self._authorization_token = None

    @property
    def authorization_token(self):
        """
        :return: authorization_token, used to authorize with api
        """
        if not self._authorization_token:
            self._authorization_token = self.authorize()
        return self._authorization_token

    def authorize(self):
        """
        Make authorization to opentopic api
        :return: authorization token
        """
        response = self.post(
            url=AUTHORIZATION_TOKEN,
            username=self.username,
            password=self.password,
            authorization_required=False
        )

        # response has token key this mean authorization is success
        if 'token' in response.keys():
            return response['token']
        elif 'non_field_errors' in response.keys():
            raise AuthorizationException(response['non_field_errors'])
        elif 'username' in response.keys():
            raise AuthorizationException(response['username'])
        elif 'password' in response.keys():
            raise AuthorizationException(response['password'])
        else:
            raise AuthorizationException(response)

    def post(self, url, authorization_required=True, **data):
        """
        Send post request to api endpoint
        :param url: url of the api endpoint
        :param data: data to send in POST
        :return: data from post response
        """
        return self._request(method=requests.post, authorization_required=authorization_required, url=url, data=data)

    def get(self, url, authorization_required=True, **data):
        """
        Send get request to api endpoint
        :param url: url of the api endpoint
        :param data: data to send in GET
        :return: data from post response
        """
        return self._request(method=requests.get, authorization_required=authorization_required, url=url, data=data)

    def _request(self, method, url, data, authorization_required=True):
        if authorization_required:
            headers = {'Authorization': 'Token {0}'.format(self.authorization_token)}
        else:
            headers = None
        r = method(url, data=data, headers=headers)
        return r.json()

    def _get_all(self, collection, **kwargs):
        """get all elements from given collection"""
        col = collection(account_name=self.account_name, **kwargs)

        def response_iterator(url):
            """
            iterate over all elements in api if there is next page do the same again
            """
            json_response = self.get(url=url)

            # TODO: all api endpoints should be standarize, some of them looks to have different json structure
            is_standard_json = type(json_response) == dict
            items = json_response['results'] if is_standard_json else json_response
            for item in items:
                obj = collection.model(**collection.parser()(item))
                yield obj

            next = json_response['next'] if is_standard_json and json_response.get('next') else None
            if next:
                for item in response_iterator(url=next):
                    yield item

        return response_iterator(col.url)

    def _get(self, collection, object_pk, **kwargs):
        """get object from collection by object_pk"""
        col = collection(account_name=self.account_name, **kwargs)
        json_response = self.get(col.get_url(object_pk=object_pk))
        return col.model(**collection.parser(json_response))
