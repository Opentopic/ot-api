def parse_source(raw):
    """
    parse single entry from source endpoints
    :param raw: load json data from channel item
    :return: return dict with formated data according to :class:`Source`
    """
    return {
        'pk': raw['id'],
        'name': raw['name'],
        'source_type': raw['source_type']
    }
