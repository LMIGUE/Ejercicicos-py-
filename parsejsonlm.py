import json
import yaml
with open ('myfile.json', 'r') as json_file:
    ourjson = json.load(json_file)
#print(ourjson)
# valor y caducidad en segundos del token.
print("The access token is: {}".format(ourjson['access_token']))
print("The access expires in {} seconds.".format(ourjson['expires_in']))
print("The access refresh is: {} seconds.".format(ourjson['refresh_token']))
# datos JSON analizados en un formato de datos YAML
print("----------------FORMATO YAML--------------")
print(yaml.dump (ourjson))