import json
import base64
import hashlib

# Used the generate a JSON object for the configuration file
def generate_config_object():
    cfgDict = {}
    cfgDict["cluster"] = "test"
    cfgDict["neighbours"] = ["127.0.0.1", "127.0.0.2", "127.0.0.3"]

    json_object = json.dumps(cfgDict, indent = 4)
    return(json_object)

# Inputs a JSON objects and output the SHA256 equivalent hash version of it
def hash_json(json_object):
    enc = json_object.encode()
    b64 = base64.encodebytes(enc)

    result = hashlib.sha256(b64)
    return(result.hexdigest())

# Take a JSON object as input and generates a configuration file
def generate_config_file(json_object):
    with open("network.json", "w") as outfile:
        outfile.write(json_object)

json_object = generate_config_object()
verify_hash = hash_json(json_object)
generate_config_file(json_object)
