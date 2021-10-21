import sys
# API
from api.Credentials import Credentials
from api.ApiConnector import ApiConnector
# Host configuration
from client.Configuration import HostConfiguration
# SSID manager
from client.HostAP import HostAPSSIDManager

if __name__ == '__main__':
    try:
        credentials = Credentials().get_as_tuple()
        radius_server_url = HostConfiguration().get_radius_server() + 'IoT'
        # We request the current SSID to the server
        api_connector = ApiConnector(
            credentials,
            default_path = radius_server_url
        )
        received_ssid = api_connector.get('/gateways/' + credentials[0] + '/current_ssid').text
        print(received_ssid)
        # We are going to update thisvalue (if needed) via a HostAPSSIDManager instance
        ssid_manager = HostAPSSIDManager()
        # We set the current SSID value from the file
        ssid_manager.set_current_ssid_from_file()
        # We update the SSID (if the obtained from the API call is different from the current one in hostapd)
        ssid_manager.update_ssid(ssid_to_update = received_ssid)
    except Exception as exception:
        # We log the failure
        print(exception)