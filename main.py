import csv
import requests

print('чтение списка кортежей')
with open('in.csv', 'r', encoding='cp1251') as f: #utf-8
    csv_in_file = csv.reader(f, delimiter=';') #по умолчанию delimiter=','
    rows = list()
    for row in csv_in_file:
        print(row)
        rows.append(row)

print('запись списка кортежей')
with open('out.csv', 'w', newline='') as f: #newline='' что бы избежать пустых строк между строк с данными
    csv_out_file = csv.writer(f) #по умолчанию delimiter=","
    csv_out_file.writerows(rows)

print('чтение списка словарей, ключи задаем самостоятельно')
with open('in.csv', 'r') as f:
    fieldnames = ['id', 'Имя']
    csv_in_file = csv.DictReader(f, delimiter=';', fieldnames=fieldnames)
    for row in csv_in_file:
        print(row)

print('чтение списка словарей, ключи берем из первой строки')
with open('in_with_col_name.csv', 'r') as f:
    csv_in_file = csv.DictReader(f, delimiter=';')
    for row in csv_in_file:
        print(row)

        #Тестирование
        #sfsdf

