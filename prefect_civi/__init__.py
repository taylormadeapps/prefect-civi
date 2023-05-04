import civicrmapi
from .civiauth import *

def hello():
    print("hello from prefect-civi")
    
    
CiviAuth.register_type_and_schema()