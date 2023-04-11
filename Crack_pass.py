# Get file paths from the user
hashes_file = input("Enter the path to the hash.ntds file: ")
output_file = input("Enter the path to the output.txt file (created by hashcat): ")

# Determine the path for the combined_output.txt file
combined_output_file = os.path.join(os.path.dirname(output_file), 'combined_output.txt')

# Read the cracked passwords
cracked_passwords = {}
with open(output_file, 'r') as f:
    for line in f.readlines():
        if not line.strip():  # Skip blank lines or lines with only whitespace
            continue
        try:
            ntlm_hash, password = line.split(':')[:2]
            cracked_passwords[ntlm_hash] = password.strip()
        except ValueError:
            print(f"Unexpected line format in output.txt: {line.strip()}")

# Read the original hash file
with open(hashes_file, 'r') as f:
    original_hashes = {line.split(':')[3]: line.split(':', 1)[0] for line in f.readlines()}

# Combine the results and create the combined_output.txt file
with open(combined_output_file, 'w') as f:
    for ntlm_hash, username in original_hashes.items():
        if ntlm_hash in cracked_passwords:
            f.write(f'{username}:{cracked_passwords[ntlm_hash]}\n')

print(f"Combined results have been saved to {combined_output_file}.")
