from faker import Faker
from faker.providers import person


objFaker = Faker
objFaker.add_provider(person)

print(objFaker.first_name_nonbinary)
print(objFaker.name())

cursos = ["COMUNICACION", "CTA", "INGLES", "FRENCH"]
