# prefect-civi

CiviCRM Integration for Prefect

Sponsored by Encircle Solutions Ltd: https://www.encircle.co.uk

## Usage

### To register an Civi Authentication block in prefect server
prefect block register --module prefect_civi.CiviAuth

```
from prefect_civi import CiviAuth
civiauth_block = CiviAuth.load("civitest")

# Get an instance of the prefect_civi.CiviClient class - populated with the configurred CiviCRM credentials configured for this block
civiclient=civiauth_block.get_client()


```



## CiviCRM Config

### Allowing APIv4 access in CiviCRM
https://docs.civicrm.org/sysadmin/en/latest/setup/api-keys/
Install AuthX (builtin) extension.

Install API Key extension: https://civicrm.org/extensions/api-key
Generate an API Key for a civi contact that is going to be used by the prefect client



## Drupal Config


Edit permissions i.e. /admin/people/permissions
and allow the following permissions for the anonymous role
- AuthX: Authenticate to services with API key
- CiviCRM: access AJAX API
- CiviCRM: access CiviCRM backend and API
    
AuthX will protect the restapi endpoint. Make sure Authentication guard is on i.e. /civicrm/admin/setting/authx
And also make sure: Acceptable credentials (HTTP X-Header) - has API KEY added.
