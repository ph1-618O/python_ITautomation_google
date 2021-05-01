#!/usr/bin/env python3

import os
import csv

def read_employees(csv_location):
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    employee_file = csv.DictReader(open(csv_location), dialect = 'empDialect')
    employee_list = []
    for data in employee_file:
        employee_list.append(data)
    return employee_list

def process_data(employee_list):
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data['Department'])

        department_data = {}
        for department_name in set(department_list):
            department_data[department_name] = department_list.count(department_name)
        return department_data

def write_report(dictionary, report_file):
    with open(report_file, 'w+') as f:
        for k in sorted(dictionary):
            f.write(str(k) + ':' + str(dictionary[k])+'\n')
        f.close()
        
directory = os.getcwd()

employee_list = read_employees(directory + '/data/employees.csv')        
print(employee_list)

dictionary = process_data(employee_list)
print(dictionary)

report_file = os.getcwd()+'/data/report.txt'
write_report(dictionary, report_file)