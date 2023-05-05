from civicrmapi.rest import RestApiV4

api_key=""
connection_url=""
basicauth_user=None
basicauth_password=None

static_rest_instance=None

def get_client():
    global static_rest_instance
    
    if not static_rest_instance:
        if basicauth_user and basicauth_password:
            auth_str={"user":basicauth_user,"pass":basicauth_password.get_secret_value()}
        else:
            auth_str=None
        
        static_rest_instance=RestApiV4(connection_url,api_key,auth_str)
    
    return static_rest_instance
    
class CiviClient:
    def __init__(self,connection_url,api_key,basicauth_user,basicauth_password):
        if basicauth_user and basicauth_password:
            auth_str={"user":basicauth_user,"pass":basicauth_password}
        else:
            auth_str=None
        self.rest_client=RestApiV4(connection_url,api_key,auth_str)
        
        
    def call_api(self,entity : str,action :str, payload):
        return self.rest_client._perform_api_call(entity,action,payload)