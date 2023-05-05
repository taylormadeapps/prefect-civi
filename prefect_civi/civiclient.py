from civicrmapi.rest import RestApiV4


class CiviClient:
    def __init__(self,connection_url,api_key,basicauth_user,basicauth_password):
        if basicauth_user and basicauth_password:
            auth_str={"user":basicauth_user,"pass":basicauth_password}
        else:
            auth_str=None
        #print("apikey: "+api_key)
        #print("connection_url: "+connection_url)
        #print("basicauth_user: "+basicauth_user)
        #print("basicauth_password: "+basicauth_password)
        
        self.rest_client=RestApiV4(connection_url,api_key,auth_str)
        
        
    def call_api(self,entity : str,action :str, payload):
        return self.rest_client._perform_api_call(entity,action,payload)