# You can merge dictionaries using the update() method .

dic1 = {"city":"Dhaka", "population":"21 million", "region": "Central"}
dic2 = {"temperature": "30°C", "humidity": "70%", "condition": "Cloudy"}
print(f"Dictionary1: {dic1}\nDictionary2:{dic2}")

print(f"Before Merged Dictionary: {dic1}")
dic1.update(dic2)
print(f"After Merged Dictionary: {dic1}")