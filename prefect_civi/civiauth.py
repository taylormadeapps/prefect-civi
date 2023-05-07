from pydantic import Field, SecretStr
from types import ModuleType
from typing import Optional
from prefect.blocks.abstract import CredentialsBlock
from .civiclient import CiviClient

class CiviAuth(CredentialsBlock):
    """
    A block that represents authentication against a civicrm instance (v4 api)
    Attributes:
        api_key: Civicrm API key for the target instance.
        connection_url: The url of the v4 api endpoint for civicrm
        basicauth_user: The username used for basic auth, if required
        basicauth_password: The password used for basic auth, if required

    Example:
        ```python
        from prefect_civi import CiviAuth
        civiauth_block = CiviAuth.load("BLOCK_NAME")

        # Get an instance of the prefect_civi.CiviClient class - populated with the configurred CiviCRM credentials configured for this block
        civiclient=civiauth_block.get_client()
        result=civiclient.call_api(entity : str,action :str, payload: dict)
        ```
    """

    _logo_url = "https://civicrm.org/sites/civicrm.org/files/CiviCRM-logo-2019-F2-200px.png"
    _block_type_name = "CiviCRM Authenticator"
    _documentation_url = "https://github.com/taylormadeapps/prefect-civi/blob/main/README.md"  # noqa

    connection_url:str = Field(
        default="http://localhost", description="The url of the root directory of the server (v4 api endpoint for civicrm will be appended automatically)"
    ) 


    api_key: SecretStr = Field(
        default=..., description="Civicrm API key for the target instance"
    )  # ... indicates it's a required field


    basicauth_user: Optional[str] = Field(
        default=None,
        title="Basic Auth User",
        description="The username used for basic auth, if required",
    )


    basicauth_password: Optional[SecretStr] = Field(
        default=None,
        title="Basic Auth Password",
        description="The password used for basic auth, if required",
    )


    def get_client(self) -> CiviClient:
        """
        Gets the Prefect-Civi client.

        Returns:
            The Prefect-Civi client.
        """
        #civiclient.api_key = self.api_key.get_secret_value()
        #civiclient.connection_url = self.connection_url
        #civiclient.basicauth_user= self.basicauth_user
        #civiclient.basicauth_password= self.basicauth_password
        
        
        
        return CiviClient(self.connection_url,self.api_key.get_secret_value(),self.basicauth_user,self.basicauth_password.get_secret_value())