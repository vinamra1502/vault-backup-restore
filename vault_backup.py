import subprocess
import json
import os


class VaultCopy:
    """
    Copy vault from one path to another recursively
    """

    def __init__(self) -> None:
        os.environ['VAULT_ADDR'] = 'https://vault_domain'
        os.environ["VAULT_TOKEN"] = "s.xxxxxxxxxxxxxxxx"

    def get_secret_formatted(self, _path):
        output = subprocess.run(["vault", "kv", "get", "-format=json", _path], stdout=subprocess.PIPE).stdout.decode("utf-8")
        kv=json.loads(output) if output else {}
        _data = kv.get("data", {}).get("data", {})
        return _data

    def create_json_file(self, json_data):
        with open("vault.json", "w") as f:
            f.write(json.dumps(json_data))

    def push_to_vault(self, output_path):
        print("Writing data to {}".format(output_path))
        subprocess.run(["vault", "kv", "put", "-format=json", output_path, "@vault.json"])

    def list_kv(self, path):
        output = subprocess.run(["vault", "kv", "list", "-format=json", path], stdout=subprocess.PIPE).stdout.decode('utf-8')
        return json.loads(output) if output else {}

    def recurse_path(self, input_path, output_path):
        child_paths = self.list_kv(input_path)
        if child_paths:
            for _path in child_paths:
                suffix = _path+("/" if not _path.endswith("/") else "")
                self.recurse_path(
                    input_path+suffix,
                    output_path+suffix
                )
        else:
            self.process(input_path, output_path)

    def process(self, input_path, output_path):
        print("Processing: {}".format(input_path))
        json_data = self.get_secret_formatted(input_path, )
        self.create_json_file(json_data)
        self.push_to_vault(output_path)


VaultCopy().recurse_path(
    input_path="input_path",
    output_path="output_path"
)
