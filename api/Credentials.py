import json

class Credentials:
    """
    @version 1.0.2
    @author Damian Alanis
    @description Class to manage 
    """
    _GATEWAY_URI_KEY             = 'uri'
    _GATEWAY_SECRET_KEY          = 'secret'
    _CREDENTIALS_FILE_NAME       = 'credentials.json'
    _DEFAULT_PATH_TO_CREDENTIALS = '../conf/' + _CREDENTIALS_FILE_NAME

    def __init__(
        self, 
        path_to_credentials = None
    ):
        """
        @param {str} path_to_credentials The path to the credentials file.
        """
        self.path_to_credentials = (
            path_to_credentials if path_to_credentials != None else self._DEFAULT_PATH_TO_CREDENTIALS
        )
        # To be defined later
        self.gateway_uri = None
        self.gateway_secret = None
        # We set the credentials
        self.set_credentials_from_file()

    def set_credentials_from_file(self):
        """Sets the credentials from the values in the credentials.json file"""
        with open(self.path_to_credentials) as file:
            credentials = json.load(file)
        self.gateway_uri = credentials[self._GATEWAY_URI_KEY]
        self.gateway_secret = credentials[self._GATEWAY_SECRET_KEY]

    def get_as_tuple(self):
        """Returns the credentials as tuple."""
        return (self.gateway_uri, self.gateway_secret)
    



