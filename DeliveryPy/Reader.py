import csv
from HashTable import HashMap

#Data CSV files
with open('Data.csv') as file:
    
    csv_data = csv.reader(file, delimiter=',')

    hash_map = HashMap()  

    #Packages List: O(1)
    def hash():
        return hash_map

    #Lists -- trucks delivery
    t_1 = []
    t_2 = []
    t_f = []

    #Insert -- stored & retrievable with index: O(n)
    for row in csv_data:
        id = row[0]
        address = row[1]
        city = row[2]
        state = row[3]
        zipcode = row[4]
        delivery = row[5]
        size = row[6]
        notes = row[7]
        delivery_start = ''
        address_location = ''
        delivery_status = 'At The Hub'

        #Values -- in order
        value = [id, address_location, address, city, state, zipcode, delivery, size, 
            notes, delivery_start, delivery_status]

        #Packages Assigned To Trucks -- conditions:
        if '84104' in value[5] and '10:30' not in value[6]:
            t_f.append(value)

        if value[6] != 'EOD':
            if 'Must' in value[8] or 'None' in value[8]:
                t_1.append(value)

        if 'Can only be' in value[8]:
            t_2.append(value)
        
        if 'Delayed' in value[8]:
            t_2.append(value)  

        if 'Wrong address listed' in value[8]:
            value[2] = '410 S State St'
            value[5] = '84111'
            t_f.append(value)


        #Remaining Packages
        if value not in t_1 and value not in t_2 and value not in t_f:
            t_2.append(value) if len(t_2) < len(t_f) else t_f.append(value)

        hash_map.insert(id, value)


    #Delivery One: O(1)
    def truck_one():
        return t_1

    #Delivery Two: O(1)
    def truck_two():
        return t_2

    #Delivery Final: O(1)
    def truck_final():
        return t_f

