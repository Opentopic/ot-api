def parse_recommendation(raw):
    """
    parse single entry from recommendation endpoints
    :param raw: load json data from recommendation item
    :return: return dict with formated data according to :class:`Recommendation`
    """
    return {
        'pk': raw['id'],
        'name': raw['name'],
    }
