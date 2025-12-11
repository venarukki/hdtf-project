class Employee:
    # Вместо инструкции pass напишите свой код.
    vacation_days = 28

    def __init__(self, first_name, second_name, gender):
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender


# Создайте экземпляры класса Employee с различными значениями атрибутов.
employee1 = Employee(first_name='Роберт', second_name='Крузо', gender='М')
employee2 = Employee(first_name='Анджелина', second_name='Джоли', gender='Ж')


# Допишите код для вывода информации о сотрудниках.
print(f'ФИО: {employee1.first_name} {employee1.second_name}, Пол: {employee1.gender}, Отпуск в году: {employee1.vacation_days}.')
print(f'ФИО: {employee2.first_name} {employee2.second_name}, Пол: {employee2.gender}, Отпуск в году: {employee2.vacation_days}.')
