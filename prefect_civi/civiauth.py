from pydantic import Field, SecretStr
from types import ModuleType
from prefect.blocks.abstract import CredentialsBlock
import civiclient

class CiviAuth(CredentialsBlock):
    """
    A block that represents authentication against a civicrm instance (v4 api)
    Attributes:
        api_key: A string value that should be kept secret.
        connection_url: The url of the v4 api endpoint for civicrm

    Example:
        ```python
        from prefect.blocks.system import Secret
        secret_block = Secret.load("BLOCK_NAME")

        # Access the stored secret
        secret_block.get()
        ```
    """

    _logo_url = "https://civicrm.org/sites/civicrm.org/files/CiviCRM-logo-2019-F2-200px.png"
    _block_type_name = "CiviCRM Credentials"
    _documentation_url = "https://github.com/taylormadeapps/prefect-civi/blob/main/README.md"  # noqa

    connection_url:str = Field(
        default="localhost", description="The url of the v4 api endpoint for civicrm"
    ) 


    api_key: SecretStr = Field(
        default=..., description="A string value that should be kept secret."
    )  # ... indicates it's a required field

    def get_client(self) -> ModuleType:
        """
        Gets the Prefect-Civi client.

        Returns:
            The Prefect-Civi client.
        """
        civiclient.api_key = self.api_key.get_secret_value()
        civiclient.connection_url = self.connection_url
        return civiclient