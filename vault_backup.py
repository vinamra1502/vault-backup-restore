import subprocess
import json
output=""

def kwargs_to_string(kwargs):
    ret = ""
    if not kwargs:
        return ret
    for k,v in kwargs.items():
        ret += " {}=\"{}\" ".format(k,v)
    return ret


def get_secret_formatted(path):
    output = subprocess.run(["vault", "kv", "get", "-format=json", path,], stdout=subprocess.PIPE).stdout.decode('utf-8')
    print("test" , output, path)
    kv=json.loads(output) if output else {}     
    return kwargs_to_string(kv.get("data",{}).get("data",{}))

def list_kv(path):
    output = subprocess.run(["vault", "kv", "list", "-format=json",path], stdout=subprocess.PIPE).stdout.decode('utf-8')
    #print("test" , output)
    return json.loads(output) if output else {}

def recurse_path(path):
    global output
    child_paths = list_kv(path)
    if child_paths:
        for _path in child_paths:
            recurse_path(path+_path+("/" if not _path.endswith("/") else ""))
    else:
        formatted_kv = get_secret_formatted(path)
        output += "\n {} {} {}".format("vault kv put ",path,formatted_kv)
recurse_path("secret/test_path/")    
with open('dump-vault.sh','w') as f:
    f.write(output)
