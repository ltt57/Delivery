class HashItem:
    def __init__(self, key, item):
        self.key = key
        self.item = item


class HashMap:
    #Initiate List -- capacity parameter set
    def __init__(self, capacity=10):
        self.tbl = []
        for _ in range(capacity):
            self.tbl.append([])

    #New Key: O(1) -- creates new key 
    def new_key(self, key):
        return int(key) % len(self.tbl)


    #Insert: O(n) -- inputs all package's information
    #Uses key (package id)
    def insert(self, key, value):
        key_hash = self.new_key(key)
        key_value = [key, value]

        if self.tbl[key_hash] == None:
            self.tbl[key_hash] = list([key_value])
            return True
        else:
            for i in self.tbl[key_hash]:
                if i[0] == key:
                    i[1] = key_value
                    return True
            self.tbl[key_hash].append(key_value)
            return True

    #Value: O(n) -- retrieves data values
    #Gets values by key (package id)
    def value(self, key):
        key_hash = self.new_key(key)
        if self.tbl[key_hash] != None:
            for i in self.tbl[key_hash]:
                if i[0] == key:
                    return i[1]
        return None


    #Update: O(n) -- updates information
    #Using key (package id)
    def update(self, key, value):
        key_hash = self.new_key(key)
        if self.tbl[key_hash] != None:
            for i in self.tbl[key_hash]:
                if i[0] == key:
                    i[1] = value
                    print(i[1])
                    return True
        else:
            print('Error Updating -- Key: ' + key)

  
    #Delete: O(n)
    #Using key (package id)
    def delete(self, key):
        key_hash = self.new_key(key)

        if self.tbl[key_hash] == None:
            return False
        for i in range(0, len(self.tbl[key_hash])):
            if self.tbl[key_hash][i][0] == key:
                self.tbl[key_hash].pop(i)
                return True
        return False
