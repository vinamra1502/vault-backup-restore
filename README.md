# vault-backup-restore Backup script.
Pass the secret path like recurse_path("secret/test_path/") and it will create dump-vault.sh bash script and after you will run dump-vault.sh and it will restore all the vault secret.
It will recursively backup all secret from given path.

Vault login like.

export VAULT_ADDR=https://dns_name


vault login 

Run Like. 
python3.x vault_backup.py --- for Backup.


./dump-vault.sh --- for Restore
