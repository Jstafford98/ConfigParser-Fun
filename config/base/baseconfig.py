from __future__ import annotations

import configparser
from pathlib import Path
from appdirs import user_data_dir
from configparser import ConfigParser

__all__ = ['ConfigFile']

class BaseConfig:
    
    _base_directory : Path = Path(user_data_dir(appname='myapp'))
    _log_directory = 'Logs'
    _data_directory = 'Data'
    _config_directory = 'Config'
    
    def __init__(self) -> None :
        
        self._base_directory.mkdir(parents=True, exist_ok=True)
        
        self.log_directory.mkdir(parents=True, exist_ok=True)
        self.data_directory.mkdir(parents=True, exist_ok=True)
        self.config_directory.mkdir(parents=True, exist_ok=True)
        
    @property
    def config_directory(self) -> Path :
        return self._base_directory / self._config_directory
    
    @property
    def data_directory(self) -> Path :
        return self._base_directory / self._data_directory
    
    @property
    def log_directory(self) -> Path :
        return self._base_directory / self._log_directory

class ConfigFile(BaseConfig):
    
    _user_config_section = 'user_config'
      
    def __init__(self, config_name : str, default_config : dict = None) -> None :
        super().__init__()
        
        self.config_name = Path(config_name)
        self.default_config = default_config

        self.load()
    
    @property
    def location(self) -> Path :
        return self.config_directory / self.config_name
    
    @property
    def default_parser(self) -> ConfigParser :
        return ConfigParser(defaults=self.default_config, allow_no_value=True)

    def get_user_section(self) -> configparser._Section :
        return self.parser[self._user_config_section]
    
    def get_user_option(self, option : str) -> str :
        ''' 
            raises:
                configparser.NoOptionError if option does not exist 
        '''
        return self.parser.get(
            section = self._user_config_section, option = option
        )
        
    def set_user_option(self, option : str, value : str) -> None :
        self.parser.set(
            section=self._user_config_section, option=option, value=value
        )
    
    def remove_user_option(self, option : str) -> bool :
        return self.parser.remove_option(
            section=self._user_config_section, option=option
        )
        
    def remove_user_option(self, option : str) -> bool :
        return self.parser.remove_option(
            section=self._user_config_section, option=option
        )
        
    def new_config(self) -> ConfigParser :
        parser = self.default_parser
        parser.add_section(section = self._user_config_section)
        return parser
    
    def load(self) -> ConfigParser :
        
        if not self.location.is_file():
            self.parser = self.new_config()
            return
        
        self.parser = ConfigParser(allow_no_value=True)
        self.parser.read(filenames=str(self.location))
    
    def save(self) -> None :
        self.location.touch(exist_ok=True)
        with open(self.location, 'w') as conf:
            self.parser.write(fp=conf)
            
    def delete(self) -> None :
        self.location.unlink()
        self.load()
    
