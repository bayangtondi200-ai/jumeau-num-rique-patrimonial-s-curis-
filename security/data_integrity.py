
import hashlib

def generate_hash(file_path):
    """Génère un hash SHA-256 pour un fichier"""
    sha256 = hashlib.sha256()
    
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    
    return sha256.hexdigest()


def verify_integrity(file_path, original_hash):
    """Vérifie si un fichier a été modifié"""
    current_hash = generate_hash(file_path)
    return current_hash == original_hash


if __name__ == "__main__":
    file = "../gis/sample_data.geojson"
    
    original = generate_hash(file)
    print("Hash original :", original)

    is_valid = verify_integrity(file, original)
    print("Intégrité vérifiée :", is_valid)
