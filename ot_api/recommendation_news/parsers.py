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
        'image': raw['image_original'],
        'popularity': raw['popularity'],
        'sorting_factor': raw['sorting_factor'],
        'twitter_count': raw['twitter_count'],
        'facebook_like_count': raw['facebook_like_count'],
        'linkedin_share_count': raw['linkedin_share_count'],
        'googleplus_share_count': raw['googleplus_share_count']
    }