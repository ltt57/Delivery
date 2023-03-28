
from Reader import hash
from Packages import total_distance

import datetime


class Main:
  
  #Title -- centered
  a = 'WGUPS \n'
  a2 = a.center(50, ' ')
  print(a2)

  print('Daily Local Deliveries  |  Tracking System \n')
     
  print(f'Delivery Completion - Total: {total_distance():.2f} miles \n')

  #User Input Keys -- view information
  enter = input("""
  Please Use Search Keys:

      To View A Package With ID & Time: 'search' 

      To View All Packages Status At Time: 'track'
         
      To Return: 'exit' 

    """)

  #If User Entry Is Not Exit...
  while enter != 'exit':
     
    #Search Package: O(n) -- User enters package ID & time
    if enter == 'search':
      try:
        total = input('Enter Package ID: ')
        time_A = hash().value(str(total))[9]
        time_B = hash().value(str(total))[10]
        
        package_time = input('Enter Time [00:00:00]: ')
        (h, m, s) = package_time.split(':')
        convert_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        (h, m, s) = time_A.split(':')
        convert_time_A = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        (h, m, s) = time_B.split(':')
        convert_time_B = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

        #Departured
        if convert_time_A >= convert_time:
          hash().value(str(total))[10] = 'At The Hub'
          hash().value(str(total))[9] = 'Departure Time: ' + time_A
                    
          print(f'Package ID: {hash().value(str(total))[0]}\n'
            f'Address: {hash().value(str(total))[2], hash().value(str(total))[3], hash().value(str(total))[4], hash().value(str(total))[5]} \n'
            f'Delivery Deadline: {hash().value(str(total))[6]}\n'
            f'Weight (kg): {hash().value(str(total))[7]}\n'
            f'Truck Status -- {hash().value(str(total))[9]}\n'
            f'Delivery Status -- {hash().value(str(total))[10]}\n' + time_B)

        #En Route        
        elif convert_time_A <= convert_time:
          if convert_time < convert_time_B:
            hash().value(str(total))[10] = 'En Route'
            hash().value(str(total))[9] = 'Departure Time: ' + time_A

            print(f'Package ID: {hash().value(str(total))[0]}\n'
              f'Address: {hash().value(str(total))[2], hash().value(str(total))[3], hash().value(str(total))[4], hash().value(str(total))[5]} \n'
              f'Delivery Deadline: {hash().value(str(total))[6]}\n'
              f'Weight (kg): {hash().value(str(total))[7]}\n'
              f'Truck Status -- {hash().value(str(total))[9]}\n'
              f'Delivery Status -- {hash().value(str(total))[10]}\n' + time_B)

          
          #Delivered
          else:
            hash().value(str(total))[10] = 'Delivered: ' + time_B
            hash().value(str(total))[9] = 'Departure Time: ' + time_A

            
            print(f'Package ID: {hash().value(str(total))[0]}\n'
              f'Address: {hash().value(str(total))[2], hash().value(str(total))[3], hash().value(str(total))[4], hash().value(str(total))[5]} \n'
              f'Delivery Deadline: {hash().value(str(total))[6]}\n'
              f'Weight (kg): {hash().value(str(total))[7]}\n'
              f'Truck Status -- {hash().value(str(total))[9]}\n'
              f'Delivery Status -- {hash().value(str(total))[10]}\n' )

      except ValueError:
        print('ERROR: Entry Is Invalid, Please Try Again!')
        exit()
    #Track: 0(n) -- User enters time
    elif enter == 'track':
      try:
        package_time = input('Enter Time [00:00:00]:  ')
        (h, m, s) = package_time.split(':')
        convert_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

        for total in range(1,41):
          try:
            time_A = hash().value(str(total))[9]
            time_B = hash().value(str(total))[10]
            (h, m, s) = time_A.split(':')
            convert_time_A = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            (h, m, s) = time_B.split(':')
            convert_time_B = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
          
          except ValueError:
            pass
                    
          #Departured
          if convert_time_A >= convert_time:
            hash().value(str(total))[10] = 'At The Hub '
            hash().value(str(total))[9] = 'Departure Time: ' + time_A

            print(f'Package ID: {hash().value(str(total))[0]}\n'
              f'Address: {hash().value(str(total))[2], hash().value(str(total))[3], hash().value(str(total))[4], hash().value(str(total))[5]} \n'
              f'Delivery Deadline: {hash().value(str(total))[6]}\n'
              f'Weight (kg): {hash().value(str(total))[7]}\n'
              f'Truck Status -- {hash().value(str(total))[9]}\n'
              f'Delivery Status -- {hash().value(str(total))[10]}\n' )

          #En Route
          elif convert_time_A <= convert_time:
            if convert_time < convert_time_B:
              hash().value(str(total))[10] = 'En Route'
              hash().value(str(total))[9] = 'Departure Time: ' + time_A

                    
              print(f'Package ID: {hash().value(str(total))[0]}\n'
               f'Address: {hash().value(str(total))[2], hash().value(str(total))[3], hash().value(str(total))[4], hash().value(str(total))[5]} \n'
              f'Delivery Deadline: {hash().value(str(total))[6]}\n'
              f'Weight (kg): {hash().value(str(total))[7]}\n'
              f'Truck Status -- {hash().value(str(total))[9]}\n'
              f'Delivery Status -- {hash().value(str(total))[10]}\n' )

            #Delivered          
            else:
              hash().value(str(total))[10] = 'Delivered: ' + time_B
              hash().value(str(total))[9] = 'Departure Time: ' + time_A

              print(f'Package ID: {hash().value(str(total))[0]}\n'
               f'Address: {hash().value(str(total))[2], hash().value(str(total))[3], hash().value(str(total))[4], hash().value(str(total))[5]} \n'
              f'Delivery Deadline: {hash().value(str(total))[6]}\n'
              f'Weight (kg): {hash().value(str(total))[7]}\n'
              f'Truck Status -- {hash().value(str(total))[9]}\n'
              f'Delivery Status -- {hash().value(str(total))[10]}\n' )

      except IndexError:
        print(IndexError)
        exit()
      
      except ValueError:
        print('ERROR: Entry Is Invalid, Please Try Again!')
        exit()
    

    #Exit
    elif enter == 'exit':
      exit()

    #Error With Entry
    else:
      print('ERROR: Entry Is Invalid, Please Try Again!')
      exit()
