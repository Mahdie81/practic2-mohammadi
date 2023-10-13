class User:
  def __init__(self, username , password ):
    self.username = username 
    self.password = password


class Buyer(User):
  def __init__(self, address , melicode ):
    self.address = address 
    self.melicode = melicode





print1 = User("mahdieh mohammadi", m0372304087 , "qom-bonyad", "0372304087")

print(print1.username)
print(print1.password)
print(print1.address)
print(print1.melicode)


