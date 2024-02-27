from config import ConfigurationPanel

if __name__ == '__main__':
    
    ConfigurationPanel.start()
    
    ConfigurationPanel._user_config.username = 'user1234'
    ConfigurationPanel._user_config.firstname = 'John'
    ConfigurationPanel._user_config.lastname = 'User'
    ConfigurationPanel._user_config.emailaddress = 'user@website.com'
    
    ConfigurationPanel._program_config.program_name = 'MyApplication'
    
    ConfigurationPanel.reload()
    
    ConfigurationPanel.display()
    
    ConfigurationPanel.delete_configs()
    
    ConfigurationPanel.display()