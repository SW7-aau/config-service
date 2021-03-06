from flask import Flask, request
app = Flask(__name__)

globals()['valid_hash'] = "none"

def same_version(new_hash):
    if (new_hash == valid_hash): return True
    return False

def update_valid_hash(new_hash):
    print("My current hash is " + str(valid_hash))
    globals()['valid_hash'] = new_hash
    print("Updated Hash to " + str(new_hash))

def update_config_file(config):
    with open("network.json", "w") as outfile:
        outfile.write(config)
    print("Updated Configuration File")

def hash_json(json_object):
    enc = json_object.encode()
    b64 = base64.encodebytes(enc)

    result = hashlib.sha256(b64)

    print("The SHA256 hexadecimal equivalent of hash is : ", end ="")
    print(result.hexdigest())
    return(result.hexdigest())

@app.route('/updateConfigFile', methods=['GET','POST'])
def get_config_file():
    config_file = request.get_json()
    new_config_hash = request.headers.get('version_hash')

    if same_version(new_config_hash):
        return "Same Version"

    update_config_file(config_file)
    update_valid_hash(new_config_hash)

    return "Changed Version"