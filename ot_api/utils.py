from ot_api.endpoints import BASE_URL


def build_endpoint_url(account_name, endpoint_name, base_url=None):
    """
    build endpoint url based on account_name and api_name
    :param account_name: name of the account in opentopic - actually it's a slug available in url address
    :param endpoint_name: api name that you want to get in to (just a path to api endpoint)
    :param base_url: base url
    :return: str with full url to api endpoint
    """
    if base_url is None:
        base_url = BASE_URL
    return base_url.format(account_name=account_name, endpoint_name=endpoint_name)
