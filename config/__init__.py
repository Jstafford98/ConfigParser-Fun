from __future__ import annotations

from .user_config import UserConfigFile
from .program_config import ProgramConfigFile

__all__ = ['ConfigurationPanel']

class ConfigurationPanel:
    
    _user_config = None
    _program_config = None
    
    @classmethod
    def set_user_config(cls : ConfigurationPanel, user_config : UserConfigFile) -> None :
        cls._user_config = user_config
        
    @classmethod
    def set_program_config(cls : ConfigurationPanel, program_config : ProgramConfigFile) -> None :
        cls._program_config = program_config
    
    @classmethod
    def get_user_config(cls : ConfigurationPanel) -> UserConfigFile :
        return cls._user_config
    
    @classmethod
    def get_program_config(cls : ConfigurationPanel) -> ProgramConfigFile :
        return cls._program_config
    
    @classmethod
    def load_configs(cls : ConfigurationPanel) -> None :
        cls._user_config = UserConfigFile()
        cls._program_config = ProgramConfigFile()
        
    @classmethod
    def save_configs(cls : ConfigurationPanel) -> None :
        cls._user_config.save()
        cls._program_config.save()
        
    @classmethod
    def delete_configs(cls : ConfigurationPanel) -> None :
        cls._user_config.delete()
        cls._program_config.delete()
    
    @classmethod
    def reload(cls : ConfigurationPanel) -> None :
        cls.save_configs()
        cls.start()
        
    @classmethod
    def start(cls : ConfigurationPanel) -> None :
        cls.load_configs()
        
    @classmethod
    def display(cls : ConfigurationPanel) -> None :
        print(f'User Config : {dict(cls._user_config.get_user_section())}')
        print(f'App Config  : {dict(cls._program_config.get_user_section())}')
    