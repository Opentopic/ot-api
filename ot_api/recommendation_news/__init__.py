"""
Recommendation News are all newses that are classified to be displayed in recommendation.

.. function:: ot_api.api.OpentopicApi.get_all_recommendation_news(recommendation_pk)

    Get all news from :class:`Recommendation`

    :param recommendation_pk: Id of :class:`Recommendation`
    :type recommendation_pk: int
    :return: iterator of :class:`ot_api.recommendation_news.models.RecommendationNews`


:Example:

>>> from ot_api.api import OpentopicApi
>>> api = OpentopicApi(account_name='account_slug', username='username', password='password')
>>> news = api.get_all_recommendation_news(recommendation_pk=123)
>>> for n in news:
>>>     print(n.title)
Profiling Python using cProfile: a concrete case
10 Reasons Python is Awesome
Doing Math with Python Available now!
Ubuntu 14.10 Has Reached End of Life, Upgrade to Ubuntu 15.04 Now
The Next Industrial Revolution Should Happen In America
Quantitative Research in Python: Using Notebooks
SciPy 2015: Scientific Computing with Python Conference
Why the Ubuntu developer portal moved to DjangoCMS
Python video: P is better than NP :)
Ubuntu may beat Windows 10 to phone-PC convergence after all
"""
