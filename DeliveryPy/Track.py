import csv
import datetime

#Distance & Location - Csv Files to Pull Data 
with open('Distances.csv') as file_distance:
    csv_distance = list(csv.reader(file_distance, delimiter=','))
with open('Locations.csv') as file_location:
    csv_location = list(csv.reader(file_location, delimiter=','))


    #Lists - optimized trucks for delivery
    t_A = []
    t_B = []
    t_C = []

    t_A_index = []
    t_B_index = []
    t_C_index = []

    #Distance & Delivery Trucks: O(n) -- 
    #Convert string to appropriate time representation [in DateTime]
    def times(distance, trucks):
      updated_time = distance / 18   #average truck mph
      minutes = '{0:02.0f}:{1:02.0f}'.format(
        *divmod(updated_time * 60, 60))
      last = minutes + ':00'
      trucks.append(last)
      total = datetime.timedelta()
      
      #Time Retrieved -- add truck's distances for total
      for i in trucks:
        (h, m, s) = i.split(':')
        total += datetime.timedelta(hours=int(h), 
        minutes=int(m), seconds=int(s))
      
      return total


    #Address: O(1)
    def address():
      return csv_location


    #Track Distance: O(1)
    def track_distance(row, column):
      distance = csv_distance[row][column]
      if distance == '':
          distance = csv_distance[column][row]

      return float(distance)


    #Calculate Total Distance: O(1)
    def total_distance(row, column, total):
      distance = csv_distance[row][column]
      if distance == '':
          distance = csv_distance[column][row]

      return total + float(distance)


    #Greedy Algorithm: O(n^2) -- This algorithm optimizes intuitively at each step in efforts to find the most efficient solutions. Using the tracked location of the trucks, the algorithm's approach works recursively; identifying the best choice for which package is to be delivered next based off previous steps taken. The self-adjusting algorithm enables response to dynamically changing input automatically until conditions are met.

    #The shortest distance per package is set at 60 miles. Going through each and every package that is up for delivery, the greedy method uses Dijkstra algorithm to find shortest distances to select the next shortest path. Based off all decisions made prior, it comes up with the optimal answer for the problem. The decision made then places the correct packages to the correct trucks contained in the lists, beginning with the first optimal truck (t_A).

    #The space complexity is O(n^2). This complexity is a selection sort which ensures that each object index (i) is the smallest on the list. Big O squared contains two for loops as the first loop goes through the list and the second goes through the remainining lists.

    def shortest_distance(packages, trucks, track_location): #Parameters
      if not len(packages):    
        return packages         

      shortest_int = 60.0       
      location = 0             


      #Determine location 
      for i in packages:    
          x = int(i[1])  #package index set as variable x
          if track_distance(track_location, x) <= shortest_int: 
            shortest_int = track_distance(track_location, x)
            location = x

      #Iterates through lists to build the solution
      for i in packages:
        if track_distance(track_location, int(i[1])) == shortest_int:
          if trucks == 1:
            t_A.append(i)
            t_A_index.append(i[1])
            packages.pop(packages.index(i))
            track_location = location
            shortest_distance(packages, 1, track_location)
          elif trucks == 2:
            t_B.append(i)
            t_B_index.append(i[1])
            packages.pop(packages.index(i))
            track_location = location
            shortest_distance(packages, 2, track_location)
          elif trucks == 3:
            t_C.append(i)
            t_C_index.append(i[1])
            packages.pop(packages.index(i))
            track_location = location
            shortest_distance(packages, 3, track_location)


    #Defined Lists: O(1)
    def truck_A():
      return t_A
    
    def truck_B():
      return t_B

    def truck_C():
      return t_C

    t_A_index.insert(0, '0')
    t_B_index.insert(0, '0')
    t_C_index.insert(0, '0')

    def truck_A_index():
      return t_A_index

    def truck_B_index():
      return t_B_index

    def truck_C_index():
      return t_C_index
