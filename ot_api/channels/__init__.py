"""
Channel are place where you can publish content. There is many type of channels, listed below:

- Facebook
- Twitter
- LinkedIn
- Viadeo
- Wordpress
- Sharepoint
- HubSpot
- Blogger
- Rss Feed
- Tumblr
- HTML Widget
- HTML Blog
- Mailchimp
- HTML Newsletter

All type of channel might required specific data for publications.

.. function:: ot_api.api.OpentopicApi.get_all_channel()

    Get list of channels :class:`Channel`

    :return: iterator of :class:`ot_api.channels.models.Channel`


:Example:

>>> from ot_api.api import OpentopicApi
>>> api = OpentopicApi(account_name='account_slug', username='username', password='password')
>>> channels = api.get_channel()
>>> for channel in channels:
>>>     print(channel.name)
Tomasz Twitter
Daily Newsletter
Opentopic Facebook
"""