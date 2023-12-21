class Node:
    def __init__(self, value, key, key2, key3):
        self.value = value
        self.key = key
        self.key2 = key2
        self.key3 = key3
        self.next = None


class hashTable:
    def __init__(self, size):
        self.table = size * [None]
        self.size = size
        
    def hashFunction(self, element):
        sum = 0
        for i in element:
            sum += ord(i)
        return sum % self.size
    
    def addElement(self, element, key, key2, key3):
        index = self.hashFunction(element)
        if self.table[index] is None:
            self.table[index] = Node(element, key, key2, key3)
        else:
            i = index
            while i < self.size:
                if self.table[i] is None:
                    self.table[i] = Node(element, key, key2, key3)
                    break
                i += 1
            # node = self.table[index]
            # while node != None:
            #     node = node.next
            # node = 
        
    def addArray(self, array):
        for i in array:
            if i != None:
                element, key, key2, key3 = i
                self.addElement(element, key, key2, key3)
        self.storeTable()
            
    def searchElement(self, element):
        index = self.hashFunction(element)
        i = index
        while i < self.size:
            if self.table[i] is not None and self.table[i].value == element:
                return self.table[i]
            i += 1
        return None
                
    def printTable(self):
        for i in self.table:
            node = i
            while node != None:
                print(node.value, node.key)
                node = node.next
        # print(self.table)
    def printAllValues(self):
        j = 0
        for i in self.table:
            value = None if i == None else i.value
            print(value, j)
            j+=1

    def storeTable(self):
        file = open("table.txt", "w")
        for i in self.table:
            if(i is None):
                file.write(str(i) + ",")
            else:
                file.write(i.value + ":" + str(i.key) + ":" + str(i.key2) + ":" + str(i.key3) + ',')
                
    def loadTable(self):
        file = open("table.txt", 'r')
        for i in file:
            items = i.split(",")
            for j in items:
                    item = j.split(':')
                    # print(item)
                    if j != "None" and j != "":
                        value, key, key2, key3 = item[0], item[1], item[2], item[3]
                        self.addElement(value, key, key2, key3)
                        
    # def isEmpty(self):
    #     for i in self.table:
    #         if(i != None):
    #             return False
        

# array = [("Size", 3, 1), ("length", 4, 2), ("height", 5, 4), ("name", 5, 2)]
# hash = hashTable(500)
# hash.addArray(array)
# print(hash.searchElement("Size"))
# hash.addElement("AbdulRehman", "45678901", "AbdulRehman@gmail.com", "Admin")
# hash.addElement("Hamza", "45678901", "hamza@gmail.com", "User")
# hash.storeTable()
# hash.loadTable()
# print(hash.searchElement('AbdulRehman'))
# hash.printTable()
        