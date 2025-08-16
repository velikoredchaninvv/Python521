import datetime

start_date = datetime.date(2023,10,26) # год, месяц, день
end_date = datetime.date(2023,11,5)

delta = datetime.timedelta(days=1) # интервал в один день

# current_date = start_date
# while current_date <= end_date:
#     print(f' Дата: {current_date}')
#     print(f' Год: {current_date.year}')
#     print(f' Месяц: {current_date.month}')
#     print(f' День: {current_date.day}')

#     current_date += delta

temp = end_date-start_date
print(temp)
