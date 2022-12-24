import math
import random as rand
import time
def RandomArray(size):
    A=[]
    for i in range(size):
        A.append(rand.randint(1, 100000))
    return A

def linearSearch(Arr,x):
    for i in range(len(Arr)):
        if(Arr[i]==x):
            return i
    else:
        return -1
# binary search only for integers and sorted numbers
def binarySearch(Arr,left,right,x):          #implement for only sorted array
    
    if(left<right):
        mid=math.floor((left+right)/2)
        if(Arr[mid]==x):
            return mid
        elif(Arr[mid]<x):
            return binarySearch(Arr,mid+1,right,x)   #left=mid+1 if number is greater than mid number 
            
        else:
            return binarySearch(Arr,left,mid-1,x) 
    else:
        return -1
       
#KMP string searching algorithm
def computingLPSarray(pattern):
    lpsArr=[0]*len(pattern)     #making Longest prefix which is also suffix
    lpsArr[0]=0
    lpsLength=0
    idx=1       #initializing 1 to start compare with next
    while(idx < len(pattern)):
        if (pattern[lpsLength]==pattern[idx]):
            lpsLength +=1
            lpsArr[idx]=len
            idx +=1
        else:
            if lpsLength==0:
                lpsArr[idx]=0
                idx +=1
            else:
                lpsLength=lpsArr[lpsLength-1]
    return lpsArr

# KMP string search algorithm end        
def KMPStringSearching(text,pattern):
        lpsArr=computingLPSarray(pattern)
        i=0
        j=0
        while i < len(text):
            if(text[i]==pattern[j]):
                 i +=1
                 j +=1
            if(j==len(pattern)):
                ret= i-j
                j=lpsArr[j-1]  #ret store index of string means character
                return True
            elif(i<len(text) and pattern[j]!=text[i]):
                
                if(j==0):
                    i +=1
                else:
                    j=lpsArr[j-1]
        return False
    


                      
        
        
   
        
    