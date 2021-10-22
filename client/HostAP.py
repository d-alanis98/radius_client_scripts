import os
import subprocess

class HostAPSSIDManager():
    """
    @author Damian Alanis Ramirez
    @version 1.0.2
    @description Class to manage the SSID of the hotspot. It provides methods to
    get the current SSID from the file (hostapd.conf) and to update it.
    """
    PATH_TO_HOSTAPD_CONFIG = '/etc/hostapd/hostapd.conf'

    def __init__(self):
        self.current_ssid = None

    def set_current_ssid_from_file(self):
        """Sets the current SSID from the value present in the hostapd.conf"""
        # We search the valu by a regular expression
        command = "sed -n -e 's/^ssid=(.*)$//p' " + self.PATH_TO_HOSTAPD_CONFIG
        process = subprocess.Popen([command], stdout = subprocess.PIPE, shell = True)
        self.current_ssid = process.stdout.read().strip()

    def update_ssid(self, ssid_to_update):
        """
        @param {str} ssid_to_update The SSID received from the server. 

        This method compares the received SSID, if it is different from the current one, the hostapd.conf
        file us going to be updated with the new value and the service hostpad is ging to be restarted.
        """
        # We are only going to update the file and restart the service if the SSID is different
        if self.__is_ssid_the_same(ssid_to_update) or ssid_to_update == None:
            return
        os.system("sed -i 's/^ssid=.*/ssid=" + ssid_to_update + "/' " + self.PATH_TO_HOSTAPD_CONFIG)
        os.system('service hostapd restart')

    # Validations
    def __is_ssid_the_same(self, ssid_to_compare):
        return self.current_ssid == ssid_to_compare

class HostAPNetworkManager():
    """
    @author Damian Alanis Ramirez
    @version 0.0.1
    @description Class to manage the network parameters of the host, as the MAC or IP addresses.
    It provides methods to get the main network parameters without having to worry about the underlying
    complexity of parsing network commands outputs.
    """

    def __init__(self):
        self.mac_addresses = {}
    
    def get_mac_address(
        self, 
        interface = 'wlan0', 
        force_update = False
    ):
        """
        @param {str} interface The interface whose MAC address we want to get.
        @param {str} force_update Flag to indicate that the MAC address should be retrieved again from the output 
        of ip addr show, no matter that it already exists in the dictionary.

        Method to get the MAC address of an interface, it checks for the interface in the mac addresses 
        dictionary and if no key is found, the MAC address is set for the first time, this also applies if
        the force_update flag is set to true
        """
        if not interface in self.mac_addresses.keys() or force_update:
            self.set_mac_address_for_interface(interface)
        return self.mac_addresses.get(interface, None)

    def set_mac_address_for_interface(self, interface = 'wlan0'):
        """
        @param {str} interface The interface whose MAC address we want to get.

        Method to set the mac address for a particular interface based on the output of the ip addr show 
        command applied to that interface. The result is stored in the dictionary, so that it can be 
        retrieved by the interface as key.
        """
        command = "ip addr show " + interface + " | sed -n -e 's/link\/ether//p'"
        process = subprocess.Popen([command], stdout = subprocess.PIPE, shell = True)
        self.mac_addresses[interface] = process.stdout.read().strip()

