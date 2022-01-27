# vault-backup-restore Backup script.
Pass the secret path like recurse_path("secret/test_path/") and it will create dump-vault.sh bash script and after you will run dump-vault.sh and it will restore all the vault secret.
It will recursively backup all secret from given path.

input_path: please source path of secret

ex: secret/tmp1


output_path: destination path of secret


ex: secret/tmp2


python3 vault_backup.py
