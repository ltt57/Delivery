import Track
import Reader

import datetime


#Lists -- truck deliveries
delivery_A = []
delivery_B = []
delivery_C = []

#Lists -- trucks traveling distance
truck_distance_A = []
truck_distance_B = []
truck_distance_C = []

#Time -- leaves the hub
time_one = ['8:00:00']
time_two = ['9:30:00']
time_three = ['11:00:00']

#Delivery Truck One: O(n)
for index, value in enumerate(Reader.truck_one()):
    Reader.truck_one()[index][9] = time_one[0]
    delivery_A.append(Reader.truck_one()[index])
    
#Delivery Truck One & List: O(n^2) -- addresses 
for index, outer in enumerate(delivery_A):
    for inner in Track.address():
        if outer[2] == inner[2]:
            truck_distance_A.append(outer[0])
            delivery_A[index][1] = inner[0]

#Select packages for first delivery truck 
Track.shortest_distance(delivery_A, 1, 0)
total_A = 0

#Total Distance First Truck and Package: O(n)
for index in range(len(Track.truck_A_index())):
    try:
        total_A = Track.total_distance(int(Track.truck_A_index()[index]), int(Track.truck_A_index()[index + 1]), total_A)
        
        delivered = Track.times(Track.track_distance(int(Track.truck_A_index()[index]), int(Track.truck_A_index()[index + 1])), time_one)
        Track.truck_A()[index][10] = (str(delivered))
        Reader.hash().update(int(Track.truck_A()[index][0]), delivery_A)
    except IndexError:
        pass


#Delivery Truck Two: O(n)
for index, value in enumerate(Reader.truck_two()):
    Reader.truck_two()[index][9] = time_two[0]
    delivery_B.append(Reader.truck_two()[index])

#Delivery Truck Two & List: O(n^2) -- addresses 
for index, outer in enumerate(delivery_B):
    for inner in Track.address():
        if outer[2] == inner[2]:
            truck_distance_B.append(outer[0])
            delivery_B[index][1] = inner[0]

#Select packages for second delivery truck 
Track.shortest_distance(delivery_B, 2, 0)
total_B = 0


#Total Distance Second Truck and Package: O(n)
for index in range(len(Track.truck_B_index())):
    try:
        total_B = Track.total_distance(int(Track.truck_B_index()[index]), int(Track.truck_B_index()[index + 1]), total_B)
        
        delivered = Track.times(Track.track_distance(int(Track.truck_B_index()[index]), int(Track.truck_B_index()[index + 1])), time_two)
        Track.truck_B()[index][10] = (str(delivered))
        Reader.hash().update(int(Track.truck_B()[index][0]), delivery_B)
    except IndexError:
        pass

#Delivery Truck Final: O(n)
for index, value in enumerate(Reader.truck_final()):
    Reader.truck_final()[index][9] = time_three[0]
    delivery_C.append(Reader.truck_final()[index])

#Delivery Truck Final & List: O(n^2) -- addresses 
for index, outer in enumerate(delivery_C):
    for inner in Track.address():
        if outer[2] == inner[2]:
            truck_distance_C.append(outer[0])
            delivery_C[index][1] = inner[0]


Track.shortest_distance(delivery_C, 3, 0)
total_C = 0

#Total Distance Final Truck and Package: O(n)
for index in range(len(Track.truck_C_index())):
    try:
        total_C = Track.total_distance(int(Track.truck_C_index()[index]), int(Track.truck_C_index()[index + 1]), total_C)
        
        delivered = Track.times(Track.track_distance(int(Track.truck_C_index()[index]), int(Track.truck_C_index()[index + 1])), time_three)
        Track.truck_C()[index][10] = (str(delivered))
        Reader.hash().update(int(Track.truck_C()[index][0]), delivery_C)
    except IndexError:
        pass

#Total of Track: O(1)
def total_distance():
    return total_A + total_B + total_C