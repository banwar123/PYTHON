from itertools import permutations 
  
def allPermutations(str): 
       
     
     permlist = permutations(str) 
  
     
     for perm in list(permlist): 
         print (''.join(perm)) 
        



str1 = str(input("enter string"))
allPermutations(str1) 

