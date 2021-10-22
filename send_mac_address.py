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
        # We get the MAC address for the interface specified in the configuration
        device_mac_address = network_manager.get_mac_address(configuration.get_network_interface())
        # We send the MAC address to the server for validation
        response = api_connector.put('/gateways/' + credentials[0] + '/validate_mac')
        if response // 200 != 1:
            raise Exception(response.text)
        print(response.text)
    except Exception as exception:
        print(exception)