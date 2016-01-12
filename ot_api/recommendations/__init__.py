"""
Recommendations are definition's of target personas.

:Example:

>>> from ot_api.api import OpentopicApi
>>> api = OpentopicApi(account_name='account_slug', username='username', password='password')
>>> news = api.get_all_recommendation()
>>> for r in recommendations:
>>>     print(r.pk)
1
2
3
44
57
"""