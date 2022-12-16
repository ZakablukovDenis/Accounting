from application.salary import calculate_salary
from application.db.people import get_employees
import datetime

now = datetime.datetime.now()
now = now.strftime("%d-%m-%Y (%H:%M:%S)")

if __name__ == '__main__':
    print(f'Текущая дата и время - {now}')
    calculate_salary()
    get_employees()
