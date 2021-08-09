from sys import argv
script_name, work_hours, pay_per_hour, award = argv

print('Имя скрипта:', script_name)
print('Оплата сотрудника:', int(work_hours)*int(pay_per_hour)+int(award))