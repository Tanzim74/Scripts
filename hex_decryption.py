import string

# 1. The scrambled data you provided
cipher_hex = "130d373118762416241c023d0e0b1c337119210b062b0879092b0903223d3531037a1d353d353815"
cipher_bytes = bytes.fromhex(cipher_hex)

# 2. What we know for sure (the flag prefix)
known_prefix = "THM{"

# 3. Recover the beginning of the key: Key = Cipher ^ Plaintext
key_start = ""
for i in range(len(known_prefix)):
    key_start += chr(cipher_bytes[i] ^ ord(known_prefix[i]))

print(f"[*] Recovered start of key: {key_start}")

# 4. Brute-force the remaining character(s)
# We'll assume the key is 5 characters long based on your previous 'GEzJl'
print("[*] Testing potential keys...")

alphabet = string.ascii_letters + string.digits

for char in alphabet:
    test_key = key_start + char

    # Decrypt the ciphertext using this trial key
    decrypted = ""
    for i in range(len(cipher_bytes)):
        decrypted += chr(cipher_bytes[i] ^ ord(test_key[i % len(test_key)]))

    # Check if the result looks like a valid flag (ends with '}')

    if decrypted.endswith("}"):
        print("-" * 30)
        print(f"[+] SUCCESS!")
        print(f"Full Key: {test_key}")
        print(f"Flag:     {decrypted}")
        print("-" * 30)
        break