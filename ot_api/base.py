import json

from booby import Model
from ot_api.endpoints import GET_URL
from ot_api.exceptions import NoParamException
from .utils import build_endpoint_url


class OpentopicModel(Model):
    """
    Base Model class. Provide functionalists for needed in all opentopic objects return by endpoints
    """
    parser = None

    def decode(self, response):
        return self.parser(json.loads(response.body))


class OpentopicCollectionMeta(type):
    """
    Define some params for collection just after create a class, also check
    if all required class params like `endpoint_name` and `parser` are setuped
    """
    def __init__(cls, name, bases, nmspc):
        super(OpentopicCollectionMeta, cls).__init__(name, bases, nmspc)
        cls.collection_name = name.lower().replace('collection', '')

        if not name == 'OpentopicCollection':
            if cls.endpoint_name is None:
                raise NoParamException('No endpoint_name in collection class defined')
            if cls.parser is None:
                raise NoParamException('No parser in collection class defined')


class OpentopicCollection(object, metaclass=OpentopicCollectionMeta):
    """
    Base Collection class. Provide functionalists needed in all opentopic endpoints
    """

    endpoint_name = None
    init_params = []

    def __init__(self, account_name, *args, **kwargs):
        self.account_name = account_name

        missing_params = self.__class__.validate_init_params(kwargs.keys())
        if missing_params:
            raise NoParamException('This Api Endpoint required following params: {0}'.format(
                ','.join(missing_params)))

        for param in self.__class__.init_params:
            setattr(self, param, kwargs.pop(param))
        kwargs = {}

        super(OpentopicCollection, self).__init__(*args, **kwargs)

    @classmethod
    def parser(cls):
        return cls.model.parser

    @property
    def url(self):
        return build_endpoint_url(account_name=self.account_name, endpoint_name=self.endpoint_name)

    def get_url(self, object_pk):
        """return url to to detail of object based on it `pk`"""
        return GET_URL.format(all_url=self.url, object_pk=object_pk)

    @classmethod
    def validate_init_params(cls, params):
        """
        :param params: list of params delivered to init method
        :return: return list of params that are required and that were not delivered
        """
        return list(set(cls.init_params) - set(params))


