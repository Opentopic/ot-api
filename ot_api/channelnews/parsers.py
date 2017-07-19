def parse_channelnews(raw):
    """
    parse single entry from channelnews endpoints
    :param raw: load json data from channel item
    :return: return dict with formated data according to :class:`ChannelNews`
    """
    return {
        'pk': raw['id'],
        'news_index': raw['news_index'],
        'title': raw['title'],
        'description': raw['description'],
        'url': raw['url'],
        'is_published': raw['is_published'],
        'is_scheduled': raw['is_scheduled'],
        'extra_message': raw['extra_message']
    }
