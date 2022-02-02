import csv

employees = open('EmployeePay.csv','r')

employee_file = csv.reader(employees, delimiter=',')

#to skip a line if the file contains a header record
         
next(employees)
for record in employee_file:
    bonus = int(record[3])*float(record[4])
    total = bonus + int(record[3])
    print('ID:',record[0])
    print('first name:',record[1])
    print('last name:',record[2])
    print('Total pay:', total)

employees.close()
