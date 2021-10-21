import json

class HostConfiguration():
    """
    @version 0.0.1
    @author Damian Alanis Ramirez
    @description Dataclass that contains the configuration for the device
    running it.
    """
    # Properties available
    RADIUS_SERVER       = 'radius_server'
    NETWORK_INTERFACE   = 'interface' 
    # Private
    _PATH_TO_HOST_CONFIG = '../../conf/conf.json'

    def __init__(self):
        self.configuration = None
        # We set the configuration from the file
        self.__set_configuration_from_file()
    

    def __set_configuration_from_file(self):
        """Method to load the config file and save it as a dictionary to a member variable"""
        with open(self._PATH_TO_HOST_CONFIG) as file:
            self.configuration = json.load(file)

    def get_value(self, key):
        """Method to get a specific value from the configuration"""
        return self.configuration.get(key, None)

    # Facade
    def get_radius_server(self):
        """Method to get directly the radius server property"""
        return self.get_value(self.RADIUS_SERVER)

    def get_network_interface(self):
        """Method to get directly the network interface"""
        return self.get_value(self.NETWORK_INTERFACE)

    