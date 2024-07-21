from faker import Faker
import random
from .models import Department, StudentID, Student  # Ensure correct import of models

fake = Faker()

def seed_db(n: int = 10) -> None:
    try:
        for i in range(n):
            # Retrieve all departments
            department_objs = Department.objects.all()

            # Select a random department
            random_index = random.randint(0, len(department_objs) - 1)
            department = department_objs[random_index]
            print(f"Selected department: {department}")

            # Generate student data
            student_id = f'STU-0{random.randint(100, 999)}'
            student_name = fake.name()
            student_age = random.randint(20, 30)
            student_address = fake.address()
            student_email = fake.email()
            
            # Create StudentID object
            student_id_obj = StudentID.objects.create(student_id=student_id)
            print(f"Created StudentID: {student_id_obj}")
            
            # Create Student object
            student_obj = Student.objects.create(
                department=department,
                student_id=student_id_obj,
                student_name=student_name,
                student_email=student_email,
                student_age=student_age,
                student_address=student_address,
            )
            print(f"Created Student: {student_obj}")
            
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
# Ensure to call this function appropriately in your Django shell or script.
