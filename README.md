# prefect-civi

## register block in prefect server
prefect block register --module prefect_civi.CiviAuth


## Allowing APIv4 access in CiviCRM
https://docs.civicrm.org/sysadmin/en/latest/setup/api-keys/
Install AuthX (builtin) extension.

Install API Key extension: https://civicrm.org/extensions/api-key
Generate an API Key for a civi contact that is going to be used by the prefect client



### Drupal 
    Edit permissions i.e. /admin/people/permissions
    and allow the following permissions for the anonymous role
    - AuthX: Authenticate to services with API key
    - CiviCRM: access AJAX API
    - CiviCRM: access CiviCRM backend and API
    
AuthX will protect the restapi endpoint. Make sure Authentication guard is on i.e. /civicrm/admin/setting/authx
And also make sure: Acceptable credentials (HTTP X-Header) - has API KEY added.
