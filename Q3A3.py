class HashTable(object):
    def __init__(self, size=18):
        self.array = [None] * size  #Initiate array with empty values
    def hash(self, key):
        lenght = len(self.array)  #Hash function
        return hash(key) % lenght

    def add(self,key,data):
        index = self.hash(key)    
        if self.array[index] is not None:
            for kcp in self.array[index]:  #Before storing a key value, check if it exists
                if kcp[0] == key:
                    kcp[1] = data  #If key is found, update the new value
                    break
            else:
                self.array[index].append([key, data]) #If loop is not broken, add the new key pair to the end
        else:
            self.array[index] = []  #Empty index, create a list and add key pair value
            self.array.append([key,data])

    def retrieve(self,key):
        index = self.hash(key)
        if self.array[index] is None:
            raise KeyError()
        else:                                  #kvp = key value pair
            for kvp in self.array[index]:      # loop through all kvp, to see if the key exist, if it exits return the value
                if kvp[0] == key:
                    return kvp[1]

            raise KeyError()   #If there was no return, the key didnt exists
    
    def Delete(self,key):
        index = self.hash(key)
        if self.array[index] is None:
            raise KeyError()
        else:
            for kvp in self.array[index]:
                if kvp[0] == key:
                    self.array.remove(kvp)
                    


                




