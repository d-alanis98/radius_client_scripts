from requests import Session

class ApiConnector():

    def __init__(
        self, 
        credentials,
        default_path = ''
    ):
        self.session = Session()
        # We set the parameters
        self.credentials = credentials
        self.default_path = default_path
        # We set the authentication from the credentials object
        self.__set_authentication()

    def __set_authentication(self):
        """Sets the authentication for the session"""
        self.session.auth = self.credentials

    # HTTP methods

    def get(self, path, parameters = None):
        """HTTP GET method, it receives the path and the optional params."""
        request_path = self.default_path + path
        print('Requesting to ' + request_path)
        self.session.get(url = request_path, params = parameters)

    def post(self, path, body = None):
        """HTTP POST method, it receives the path and the body of the request."""
        request_path = self.default_path + path
        self.session.post(url = request_path, data = body)

    def put(self, path, body = None):
        """HTTP PUT method, it receives the path and the body of the request."""
        request_path = self.default_path + path
        self.session.put(url = request_path, data = body)

    

    
