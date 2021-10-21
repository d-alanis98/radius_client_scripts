import os
import sys
# API
from api.Credentials import Credentials
from api.ApiConnector import ApiConnector
# Host configuration
from client.Configuration import HostConfiguration



class HostAPSSIDManager():
    """
    @author Damian Alanis Ramirez
    @version 0.0.2
    @description Class to manage the SSID of the hotspot. It provides methods to
    get the current SSID from the file (hostapd.conf) and to update it.
    """
    PATH_TO_HOSTAPD_CONFIG = '/etc/hostapd/hostapd.conf'

    def __init__(self):
        self.current_ssid = None

    def set_current_ssid_from_file(self):
        """Sets the current SSID from the value present in the hostapd.conf"""
        self.current_ssid = os.system("sed -n -e 's/^ssid=//p' " + self.PATH_TO_HOSTAPD_CONFIG)

    def update_ssid(self, ssid_to_update):
        """
        @param {str} ssid_to_update The SSID received from the server. 

        This method compares the received SSID, if it is different from the current one, the hostapd.conf
        file us going to be updated with the new value and the service hostpad is ging to be restarted.
        """
        # We are only going to update the file and restart the service if the SSID is different
        if self.__is_ssid_the_same(ssid_to_update):
            return
        os.system("sed -i 's/^ssid=.*/ssid=" + ssid_to_update + "/' " + self.PATH_TO_HOSTAPD_CONFIG)
        os.system('service hostapd restart')

    # Validations
    def __is_ssid_the_same(self, ssid_to_compare):
        return self.current_ssid == ssid_to_compare

if __name__ == '__main__':
    try:
        credentials = Credentials().get_as_tuple()
        radius_server_url = HostConfiguration().get_radius_server() + 'IoT'
        # We request the current SSID to the server
        api_connector = ApiConnector(
            credentials,
            default_path = radius_server_url
        )
        received_ssid = api_connector.get('/gateways/' + credentials[0] + '/current_ssid')
        # We are going to update thisvalue (if needed) via a HostAPSSIDManager instance
        ssid_manager = HostAPSSIDManager()
        # We set the current SSID value from the file
        ssid_manager.set_current_ssid_from_file()
        # We update the SSID (if the obtained from the API call is different from the current one in hostapd)
        ssid_manager.update_ssid(ssid_to_update = received_ssid)
    except Exception as exception:
        # We log the failure
        print(exception)
        sys.stderr.write(exception)
