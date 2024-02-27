from .base import ConfigFile
from multiprocessing import cpu_count

class ProgramConfigFile(ConfigFile):
    
    def __init__(self) -> None :
        super().__init__(
            config_name='myapp.conf',
            default_config={
                'max_workers' : cpu_count(),
                'program_name' : 'myapp'
            }
        ) 
        
    @property
    def max_workers(self) -> str :
        return self.get_user_option(option='max_workers')
    
    @max_workers.setter
    def max_workers(self, max_workers : str) -> None :
        self.set_user_option(option='max_workers', value=max_workers)
        
    @property
    def program_name(self) -> str :
        return self.get_user_option(option='program_name')
    
    @program_name.setter
    def program_name(self, program_name : str) -> None :
        self.set_user_option(option='program_name', value=program_name)
    