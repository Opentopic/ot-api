def parse_channel(raw):
    """
    parse single entry from channel endpoints
    :param raw: load json data from channel item
    :return: return dict with formated data according to :class:`Channel`
    """
    return {
        'pk': raw['id'],
        'name': raw['name'],
        'channel_type': raw['channel_type']
    }
