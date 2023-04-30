from pydantic import Field, SecretStr
from prefect.blocks.core import Block

class CiviAuth(Block):
    """
    A block that represents a secret value. The value stored in this block will be obfuscated when
    this block is logged or shown in the UI.

    Attributes:
        value: A string value that should be kept secret.

    Example:
        ```python
        from prefect.blocks.system import Secret
        secret_block = Secret.load("BLOCK_NAME")

        # Access the stored secret
        secret_block.get()
        ```
    """

    _logo_url = "https://civicrm.org/sites/civicrm.org/files/CiviCRM-logo-2019-F2-200px.png"

    value: SecretStr = Field(
        default=..., description="A string value that should be kept secret."
    )  # ... indicates it's a required field

    def get(self):
        return self.value.get_secret_value()
        
