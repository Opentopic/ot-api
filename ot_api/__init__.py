"""
To start using Api you should use :class:`OpentopicApi`. To initialize api you need `account_name`,
`username` and `password`. Client will authorize with rest api with first query that will required that, so just
after :class:`OpentopiApi` initialization you can start using available endpoints.

:Example:

>>> from ot_api.api import OpentopicApi
>>> api = OpentopicApi(account_name='account_slug', username='username', password='password')
>>> api.get_all_channels()
[channel_1, channel_2]

"""

__author__ = 'tomaszroszko'
