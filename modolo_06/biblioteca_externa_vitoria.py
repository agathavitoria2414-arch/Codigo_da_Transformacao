pip install faker
from faker import Faker

fake = Faker("pt_BR")

print("Nome falso:", fake.name())
print("Endereço falso:", fake.address())
print("E-mail falso:", fake.email())
