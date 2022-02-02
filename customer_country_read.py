import csv

customers = open('customers.csv','r')

customer_file = csv.reader(customers, delimiter=',')
customer_country = open('customer_country1.csv','w')
#to skip a line if the file contains a header record
next(customer_file)         

for record in customer_file:
    customer_country.write(record[1]+","+record[2]+","+record[4]+"\n")


customer_country.close()
    
