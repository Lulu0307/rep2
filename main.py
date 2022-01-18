
from datetime import datetime
from application.salary import calculate_salary
from db.people import get_employees


if __name__ == '__main__':
    print(datetime.now().date())
    get_employees()
    calculate_salary()