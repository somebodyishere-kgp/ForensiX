import hashlib

def calculate_hash(file_path, algorithm):
    
    hash_obj = hashlib.new(algorithm)

    with open(file_path, "rb") as f: #opening in byte is important because hashes operate in raw bytes

        while chunk := f.read(8192): #reads 8192 bytes at a time, reading entire file means opening it in ram, if file is large ram usage saturation
            hash_obj.update(chunk)

    return hash_obj.hexdigest() #since we converted file to raw bytes earlier so hash_obj.digest() returns raw bytes, therefore convert to hexadecimal

def get_file_hashes(file_path):

    return{
        "md5": calculate_hash(file_path, "md5"),
        "sha1": calculate_hash(file_path, "sha1"),
        "sha256": calculate_hash(file_path, "sha256")
    }