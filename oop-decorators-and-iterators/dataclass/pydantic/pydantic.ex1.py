# Pydantic is designed around validation.
# DataClass -> I want a class that conveniently represents data.

from pydantic import BaseModel

class User(BaseModel):
    name:str
    email:str
    account_id:int
    
    
user = User(name="Augustine", email="augustine@example.com", account_id=26)
print(user)  # Output: name='Augustine' email='augustine@example.com' account_id=26