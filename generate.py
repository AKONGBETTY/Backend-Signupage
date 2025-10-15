import secrets
import base64

# Generate a URL-safe, base64-encoded 32-byte secret (256 bits)
secret_bytes = secrets.token_bytes(32)
secret_token = base64.urlsafe_b64encode(secret_bytes).decode('utf-8')

print(secret_token)
print(f"Length of the secret token: {len(secret_token)} characters")
