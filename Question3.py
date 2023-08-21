values = [("Fashion item","Price")("Boxy T-Shirt", 140), ("U Neck Tank", 220), ("Rib-Knit Sweater", 230), ("Gwyneth Cupro-Bllend Slip Dress", 230), ("Double-Breasted Jacket ", 500), ("Padded Bomber Jacket", 500), ("Mason Pant ", 1780), ("Full Length Pants", 350), ("Wide-Leg Pants", 370), ("Knee-High Boots ", 700), ("Daybreak Sneaker ", 1200), ("Ruched Midi Dress", 1150), ("Ballet Flats in Leather", 50), ("Laguna Waterproof boot ",1700), ("Maesa Pleated Woven Wide-Leg Cargo Pants", 2100), ("Oversized Single-Breasted Jacket", 755), ("Louisa Lady Jacket in Maritime Tweed", 3500)]

ARR_Lenght = 18
values = [None]*ARR_Lenght

def get_index(key: str):
    return hash(key) % len(values)


class HashTable(object):
    def __init__(self, lenght =18):
        self.array = [None]*lenght

    def hash(self,key):
        length = len(self.array)
        return hash(key) % length

    def add(self, key, value):
        index = self.hash(key)
        if self.array[index] is not None:
            #Index contains values

            for kvp in self.array[index]:
                if kvp[0] == key:
                    kvp[1] == value
                    break
            else:

                self.array[index].append([key,value])
        else:

            self.array[index] = []
            self.array[index].append([key,value])
    
    def get(self, key):
        index = self.hash(key)
        if self.array[index] is None:
            raise KeyError()
        else:
            for kvp in self.array[index]:
                if kvp[0] == key:
                    return kvp[1]
            #IF no return was done during loop
            raise KeyError()