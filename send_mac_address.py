# API
from api.Credentials import Credentials
from api.ApiConnector import ApiConnector
# Host 
from client.HostAP import HostAPNetworkManager
from client.Configuration import HostConfiguration


if __name__ == '__main__':
    try:
        credentials = Credentials().get_as_tuple()
        configuration = HostConfiguration()
        radius_server_url = configuration.get_radius_server() + 'IoT'
        # We request the current SSID to the server
        api_connector = ApiConnector(
            credentials,
            default_path = radius_server_url
        )
        # We are going to get the current mac (in file) via a HostAPNetworkManager instance
        network_manager = HostAPNetworkManager()
        print(network_manager.get_mac_address(configuration.get_network_interface()))
    except Exception as exception:
        print(exception)
