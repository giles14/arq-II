from cryptography.fernet import Fernet

key = Fernet.generate_key()  # store in a secure location
print("Key:", key.decode())

def encrypt(message: bytes, key: bytes) -> bytes:
    return Fernet(key).encrypt(message)

def decrypt(token: bytes, key: bytes) -> bytes:
    return Fernet(key).decrypt(token)
message = "Lograste coordinarlo exitosamente"
token = encrypt(message.encode(), key)
print(token.decode())
message = "Sigue intentando, aun no logras coordinarlo"
token = encrypt(message.encode(), key)
print(token.decode())
#token = 'gAAAAABiJ5tsHbVatf2K_MGoV1LbgdcS3_KsWBKH6ZbQdIHnU7I93DzGQ2jZ59uKoa03UegXDYZl4JzdJbdV5bu8AVlQhfCQTw=='
#token = token.encode()
#key = 'JEgE2Uxsf9ksFU6IiyBXZlnDwcVChjFkHTDqAH8AEtQ='
#key = key.encode()
#token = 'gAAAAABiJ5yAL5w-6JhunGHm98MUhHOew8KaZmBDzORdHTccvLmI90Fccd8sjiB1EPEEySVA4qrO9684DogvYbFbB0pHYM8LrA=='
#token = token.encode()

print(decrypt(token, key).decode())
