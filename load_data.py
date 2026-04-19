import csv
from apps.bookmodule.models import Student, Address

with open('students.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        city_name = row['city'].strip()
        address = Address.objects.get(city=city_name)

        Student.objects.create(
            name=row['name'],
            age=row['age'],
            address=address
        )