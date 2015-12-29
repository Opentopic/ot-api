import unittest
from unittest.mock import MagicMock

from .api import OpentopicApi
from .utils import build_endpoint_url

from .exceptions import AuthorizationException, NoParamException
from .testcollection.collections import TestCollection
from .testcollection.models import _generate_test_json, _generate_test_objects


class TestUtils(unittest.TestCase):
    """Test utils functions for api"""

    def test_build_endpoint_url_success(self):
        url = build_endpoint_url(account_name='test_name', endpoint_name='some/path')
        self.assertEqual('https://new.opentopic.com/test_name/rest-api/some/path/', url)


class TestOpentopicAPI(unittest.TestCase):
    """Test case for opentopic main api class"""

    def __test_wrong_creds(self, username, password):
        api = OpentopicApi(account_name='test_account', username=username, password=password)
        with self.assertRaises(AuthorizationException):
            api.authorize()

    def test_api_authorization_wrong_creds(self):
        OpentopicApi.post = MagicMock(
                return_value={'non_field_errors': ["Unable to log in with provided credentials."]})
        self.__test_wrong_creds(username='test_username', password='test_password')

    def test_api_no_username(self):
        OpentopicApi.post = MagicMock(
                return_value={"username": ["This field is required."]})
        self.__test_wrong_creds(username=None, password='test_password')

    def test_api_no_password(self):
        OpentopicApi.post = MagicMock(
                return_value={"password": ["This field is required."]})
        self.__test_wrong_creds(username='test_username', password=None)

    def test_authorization_success(self):
        OpentopicApi.post = MagicMock(
            return_value={"token": "test_token"})
        api = OpentopicApi(account_name="test_account", username="test_username", password="test_password")
        token = api.authorize()
        self.assertEqual(token, "test_token")

    def test_authorization_success_cache(self):
        """
        we have to test if when we will ask for authorization_token once we are not going todo it second time
        """
        OpentopicApi.post = MagicMock(
            return_value={"token": "test_token"})
        api = OpentopicApi(account_name="test_account", username="test_username", password="test_password")
        self.assertEqual(api.authorization_token, "test_token")
        OpentopicApi.post = MagicMock(
            return_value={"token": "different_token"})
        # token shoud remain the same
        self.assertEqual(api.authorization_token, "test_token")

    def test_get_all_one_page(self):
        """
        test getting all objects from api without next page
        """

        OpentopicApi.get = MagicMock(
            return_value=_generate_test_json(0, 6)
        )
        api = OpentopicApi(account_name="test_account", username="test_username", password="test_password")
        items = list(api._get_all(TestCollection))
        self.assertEqual(len(items), 6)
        self.assertEqual(items[0]['name'], 'test_name0')
        self.assertEqual(items[3]['name'], 'test_name3')

    def test_empty_response(self):
        OpentopicApi.get = MagicMock(
            return_value=_generate_test_json(0, 0)
        )
        api = OpentopicApi(account_name="test_account", username="test_username", password="test_password")
        items = list(api._get_all(TestCollection))
        self.assertEqual(len(items), 0)

    def test_get_all_non_standard_response(self):
        """
        some of the endpoints return json with no standard json format, test if it works for us
        """
        OpentopicApi.get = MagicMock(return_value=_generate_test_objects(0, 6))
        api = OpentopicApi(account_name="test_account", username="test_username", password="test_password")
        items = list(api._get_all(TestCollection))
        self.assertEqual(len(items), 6)


class TestOpentopicCollection(unittest.TestCase):
    """
    Test Base Opetnopic Collection class
    """

    def test_validate_init_params(self):
        """
        test if validation of required params is proper
        """

        TestCollection.init_params = []

        # no param required and no param given
        self.assertEqual(TestCollection.validate_init_params([]), [])

        # no param required but one param given
        self.assertEqual(TestCollection.validate_init_params(['additional_param']), [])

        # param required and param given
        TestCollection.init_params = ['channel_pk']
        self.assertEqual(TestCollection.validate_init_params(['channel_pk']), [])

        # param required but not given
        self.assertEqual(TestCollection.validate_init_params([]), ['channel_pk'])

    def test_collection_init(self):
        """
        test if init method for collection works
        """

        TestCollection.init_params = []

        # account_name is required we shouldn't allow for init
        self.assertRaises(TypeError, TestCollection)
        TestCollection(account_name='dev')

        TestCollection.init_params = ('channel_pk',)
        self.assertRaises(NoParamException, TestCollection, account_name='dev')

        # test successful initialization
        collection = TestCollection(account_name='dev', channel_pk=1)
        self.assertEqual(collection.channel_pk, 1)

        TestCollection.init_params = []
