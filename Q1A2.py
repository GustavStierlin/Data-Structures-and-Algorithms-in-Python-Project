from platform import java_ver


def string_permutation(name):
    i = 0
    
    for i in name:
        j = 1
        for j in name:
            if j == i:
                i = i+1
                return i
                
            else:
                
                return string_permutation
                

person = input("NAme: ")
string_permutation(person)
        
