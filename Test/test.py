import json

splitPresentAddress = "{\"district\":[\"South\"],\"state\":[[\"Delhi\"]],\"city\":[\"Bhati\"],\"pincode\":\"400000\",\"country\":[\"IN\",\"IND\",\"INDIA\"],\"addressLine\":\"New Delhi Delhi\"}"

nd_splited = '{"district":["West"],"state":[["Delhi"]],"city":["Bapraula"],"pincode":"110043","country":["IN","IND","INDIA"],"addressLine":"185 block c5 nangli vihar"}'

address_dict = json.loads(nd_splited)

district = address_dict["district"][0]
state = address_dict["state"][0][0]
city = address_dict["city"][0]
pincode = address_dict["pincode"]
country = address_dict["country"][2]

print(district, state, city, pincode, country)