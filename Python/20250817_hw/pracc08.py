# Человек работает в компании с накоплением отпускных дней с автоматическим индексированием зарплаты:
# [+] каждый месяц она увеличивается на  100 рублей
# [+] а за каждые две недели появляется один день отпуска
# [-] Отпускные рассчитываются как зарплата на конец предыдущего месяца
# [+] Человек вводит дату поступления на работу
# [+] Вывести количество дней отпуска и сумму отпускных, предполагая, что он ещё ни разу не брал отпуск.
# [+] Усложнение: человек вводит своё имя. В "базе данных" хранится для каждого человека количество взятых дней отпуска. {'Вася': 42}

### START ###

#install programs
import datetime

#datetime_maual_input
start_year = int(input('Введите год, 4 цифры, в котором начали работу: '))
start_month = int(input('Введите номер месяца в котором начали работу: '))
start_day = int(input('Введите день в который начали работу: '))
start_time = datetime.date(start_year,start_month,start_day)

#datetime_input
# start_time = datetime.date(2022, 7, 1) # для проверки

#datetime_now
date_now = datetime.date.today()

#days_of_work
days_of_work = (date_now-start_time)

# preview
# print(days_of_work.days) # для проверки
# print(time_of_work) # для проверки

#counting_month_and_doule_week
month = days_of_work.days // 30 # 30 округлил количество дней в месяц до 30
double_week = month // 2

#vacation_day
vacation_day = double_week

#monthly_allowance_in_money
monthly_allowance = month * 100

#parameters member
salary_in_month = 150000
salary_plus_bonus = salary_in_month + monthly_allowance

#result
print(f'Зарплата {salary_plus_bonus}')
print(f'Дней отпуска {vacation_day}')

employees = {
    "СанПедро": vacation_day
}

pedroname = input("Введите имя, например СанПедро: ")

if pedroname in employees:
    print(employees[pedroname])
else:
    exit()