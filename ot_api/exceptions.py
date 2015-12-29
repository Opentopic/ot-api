class NoParamException(Exception):
    """
    Raise when required params are not given
    """
    pass


class AuthorizationException(Exception):
    """
    Raise during authorization, b'coz of any reason of failure
    """
    pass


class NotAvailableException(Exception):
    """
    Raise when method in specific api endpoint is not available
    """
