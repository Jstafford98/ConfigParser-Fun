from .base import ConfigFile

class UserConfigFile(ConfigFile):
    
    def __init__(self) -> None :
        super().__init__(
            config_name='user.ini',
            default_config={
                'username' : None,
                'firstname' : None,
                'lastname' : None,
                'emailaddress' : None
            }
        )
    
    @property
    def username(self) -> str :
        return self.get_user_option(option='username')
    
    @username.setter
    def username(self, username : str) -> None :
        self.set_user_option(option='username', value=username)
    
    @property
    def firstname(self) -> str :
        return self.get_user_option(option='firstname')
    
    @firstname.setter
    def firstname(self, firstname : str) -> None :
        self.set_user_option(option='firstname', value=firstname)
    
    @property
    def lastname(self) -> str :
        return self.get_user_option(option='lastname')
    
    @lastname.setter
    def lastname(self, lastname : str) -> None :
        self.set_user_option(option='lastname', value=lastname)
    
    @property
    def emailaddress(self) -> str :
        return self.get_user_option(option='emailaddress')
    
    @emailaddress.setter
    def emailaddress(self, emailaddress : str) -> None :
        self.set_user_option(option='emailaddress', value=emailaddress)
