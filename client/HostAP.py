import os
import subprocess

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
