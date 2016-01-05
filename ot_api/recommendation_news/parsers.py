def parse_recommendationnews(raw):
    """
    parse single entry from recommendationnews endpoints
    :param raw: load json data from channel item
    :return: return dict with formated data according to :class:`RecommendationNews`
    """
    return {
        'pk': raw['pk'],
        'title': raw['title'],
        'description': raw['description'],
        'url': raw['url'],
        'image': raw['image_original']
    }