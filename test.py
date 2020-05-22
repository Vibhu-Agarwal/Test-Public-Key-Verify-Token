import jwt

token = input('Enter Token:\n').strip()

public_key = open('jwt_key.pub').read()

payload = jwt.decode(token, public_key, algorithms=['RS256'])

print(payload)