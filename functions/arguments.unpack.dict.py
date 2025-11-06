
# Dictionary unpacking
# syntax : **dict_name to unpack the key-value pairs    

def personInfo(name, age, city):
    print(name, age, city)
info = {"name": "Kholofelo", "age": 25, "city": "Johannesburg"}
personInfo(**info)  # Output: Kholofelo 25 Johannesburg
