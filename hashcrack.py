import hashlib

def hash_password(password, algorithm="sha256"):
    """Generate a hash of the password using a specified algorithm."""
    hash_func = getattr(hashlib, algorithm, None)
    if not hash_func:
        raise ValueError("Unsupported hash algorithm")
    return hash_func(password.encode()).hexdigest()

def crack_hash(hash_value, wordlist_file, algorithm="sha256"):
    """Try to find the original password by matching with common passwords."""
    hash_func = getattr(hashlib, algorithm, None)
    if not hash_func:
        raise ValueError("Unsupported hash algorithm")
    
    with open(wordlist_file, "r", encoding="utf-8") as file:
        for word in file:
            word = word.strip()
            if hash_func(word.encode()).hexdigest() == hash_value:
                return word  # Password found
    return None  # Password not found

if __name__ == "__main__":
    print("1️⃣ Hash a password")
    print("2️⃣ Crack a password hash")
    choice = input("Enter choice (1 or 2): ")

    if choice == "1":
        password = input("Enter password to hash: ")
        algorithm = input("Enter hash algorithm (md5, sha1, sha256, sha512): ")
        print(f"🔐 Hashed password: {hash_password(password, algorithm)}")

    elif choice == "2":
        hash_value = input("Enter the hashed password: ")
        wordlist = input("Enter path to wordlist file: ")
        algorithm = input("Enter hash algorithm (md5, sha1, sha256, sha512): ")
        cracked_password = crack_hash(hash_value, wordlist, algorithm)
        
        if cracked_password:
            print(f"✅ Password found: {cracked_password}")
        else:
            print("❌ Password not found in wordlist.")

    else:
        print("❌ Invalid choice.")
