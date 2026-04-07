import json

#
#   1. Convert Python dictionary into JSON format
#      To convert Python into JSON use the json.dump() method.
#
pydict = {"key1" : "value1", "key2" : "value2"}

py_to_json = json.dumps(pydict)

print(pydict)

#
#   2. Access value of key 2 from JSON.
#      To parse JSON string into Python obbject, use json.loads()method.
#
json_obj = """{"key1": "value1", "key2": "value2"}"""

json_to_py = json.loads(json_obj)

print(json_to_py['key2'])

#
#   3. PrettyPrint JSON data
#      Print data with indent level 2 and a seprator of '='
#
json_obj = {"key1": "value1", "key2": "value2"}

prettyPrint = json.dumps(json_obj, indent = 2, separators = (",","="))

print(prettyPrint)

#
#   4. Sort JSON keys and write them into a file
#      Use dump() instead for file storage as dumps() is used for API responses and memory manipulation. 
#
json_obj = {"id" : 1, "name" : "value2", "age" : 29}

print("Writing JSON data into a file")
try:
    with open("JSONdata.json", "w") as file:
        json.dump(json_obj, file, indent=4, sort_keys=True)
    print("JSON data written to file.")
except (TypeError, ValueError) as error:
    print(f"Error: {error}")

#
#   5. Access nested key 'salary' from JSON
#
json_obj = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

json_to_py = json.loads(json_obj)

print(json_to_py['company']['employee']['payble']['salary'])

#
#   6. Convert Vehicle Object into JSON
#      The JSON Encoder must be imported to help serialize the object.
#
from json import JSONEncoder

class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

class VehicleEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

vehicle = Vehicle("Toyota RAV4", "2.5L", 32000)

print("Encode vehicle object into json")
json_to_py = json.dumps(vehicle, indent=4, cls=VehicleEncoder)
print(json_to_py)

#
#   7. Covert JSON into Object
#      Create a function that takes a dictioanry as an input and returns an instance of a class.
#      To parse JSON string into Python obbject, use json.loads()method. Within the loads() method,
#      use 'objecct_hook' to deserialize the object into a Python object. 
#
class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

def vehDecoder(obj):
    return Vehicle(obj['name'], obj['engine'], obj['price'])

vehObject = json.loads('{ "name": "Toyota Rav4", "engine": "2.5L", "price": 32000 }', object_hook=vehDecoder)

print("Type of decoded object from given JSON data:")
print(type(vehObject))
print("Vehicle details:")
print(vehObject.name, vehObject.engine, vehObject.price)

#
#   8. Check if JSON object is valid
#      Use the echo command and json.tool module to validate the object.
#
def validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        return False
    return True

j_Data = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000
            "bonus":800
         }
      }
   }
}"""
isValid = validateJSON(j_Data)

print("Is given JSON string is Valid?:", isValid)

#
#   9. Parse JSON data to get value within an array.
#      Get the values of 'name'. Use loads() to convert JSON format string 
#      into Python format. Use 'item.get' to retrieve values from keys and 'for'
#      to loop through every element in the JSON data.
#
json_data = """[ 
   { 
      "id":1,
      "name":"name1",
      "color":[ 
         "red",
         "green"
      ]
   },
   { 
      "id":2,
      "name":"name2",
      "color":[ 
         "pink",
         "yellow"
      ]
   }
]"""

data = []
try:
    data = json.loads(json_data)
except Exception as e:
    print(e)

dataList = [item.get('name') for item in data]
print(dataList)