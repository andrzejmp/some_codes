from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt()
password = 'ala ma kota'
hashed_password = bcrypt.generate_password_hash(password)
print(hashed_password)

print(bcrypt.check_password_hash(hashed_password, 'ala ma'))
print(bcrypt.check_password_hash(hashed_password, 'ala ma kota'))

#-------------------------------------------------------------

from werkzeug.security import generate_password_hash, check_password_hash
hashed_password = generate_password_hash(password)
print(hashed_password) 
print(check_password_hash(hashed_password, 'ala ma'))
print(check_password_hash(hashed_password, 'ala ma kota'))