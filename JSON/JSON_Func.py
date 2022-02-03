import json

data='{"var1":"Hello World", "var2":69 }'
#JSON .loads convert the data into a dictionary
parsed=json.loads(data)
print(parsed['var1'])
print(type(parsed))

data2={"cars":['BMW','AUDI'],
        "fridge":('ICE Cream','Bread')
        }

# .dumps turns data into java script compatible data
jscomp=json.dumps(data2)
print(jscomp)