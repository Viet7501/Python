from phone_gen import PhoneNumber
import names

phone_number = PhoneNumber("Great Britain")
d = ['London', 'Madrid', 'New York', 'Boston', 'Paris', 'Hanoi', 'Barcelona', 'Mannheim', 'México D.F.', 'São Paulo', 'Sevilla', 'Frankfurt a.M.', 'San Francisco', 'Montréal', 'Buenos Aires']

# 50 Customers
for j in range(50):
    random_city = random.choice(d)
    number = phone_number.get_mobile()
    j = Customer(name=names.get_last_name(), contact_name=names.get_full_name(), contact_number=number, address=random_city)
    j.save()

# 50 Employees
for i in range(50):
    random_city = random.choice(d)
    i = Employee(name=names.get_full_name(), address=random_city)
    i.save()

# 5-2
Customer.objects.last(update(contact_number='954-640-7780'))


# 5-3

Customer.objects.get_or_create(contact_name='Louis Huang')

Customer.objects.create(name="Cattleman's Ranch", contact_name="Louis Huang", contact_number='954-640-7769',address='Orlando')

Customer.objects.filter(id=1).update(contact_number='957-640-5642')
