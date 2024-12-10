#!/bin/bash

# Variables
HOST="192.168.43.230"           # Target MySQL host
USER="testuser"                 # MySQL username
PASSWORD="password"        # MySQL password
TARGET_DB="testdb"              # Database to target
TARGET_TABLE="users"            # Table to extract data from
OUTPUT_FILE="/tmp/data_dump_users.txt"  # Local file to store results

# Insert sample data into the 'users' table if it's empty
mysql -h "$HOST" -u "$USER" -p"$PASSWORD" --skip-ssl -e  "USE $TARGET_DB; INSERT INTO $TARG>

# Query data from the 'users' table and output to a local file
mysql -h "$HOST" -u "$USER" -p"$PASSWORD" --skip-ssl -e "USE $TARGET_DB; SELECT * FROM $TAR>

# Notify user of completion
if [[ -s "$OUTPUT_FILE" ]]; then
    echo "[+] Data extraction completed successfully. Results saved to $OUTPUT_FILE."
else
    echo "[-] Data extraction failed or returned no results. Check permissions and table da>
fi





