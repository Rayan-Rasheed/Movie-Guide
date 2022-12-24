import random as rand
import sys
import math as m
import random

#-------------------------------------------------------
#insertion both
#selection both
#merge both
#hybridmerge both
#bubble both
#quick both
#counting both
#radix both
#bucket both
#pigeonhole both
#cocktail both
#postman both


#--------------------------------------------------------
def InsertionSort(array,attr,start,end):  
    for i in range(start+1,end+1):
        key=array[i]
        k=i-1
        while(k>=0 and getattr(key,attr)<getattr(array[k],attr)):
            array[k+1]=array[k]
            k=k-1
        array[k+1]=key
    
    return array


def InsertionSortDesc(array,attr,start,end):  
    
    for i in range(start,end+1):
        key=array[i]
        k=i-1
        while(k>=0 and getattr(key, attr) > getattr(array[k],attr)):
            array[k+1]=array[k]
            k=k-1
        array[k+1]=key
   
    return array
#----------------------------------------------------------
def SelectionSort(array,attr,start,end):
    
    for i in range(start,end+1):
        min=i
        for j in range(i,end+1):
            if((getattr(array[j],attr))<(getattr(array[min],attr))):
                min=j  
        swap=array[min]
        array[min]=array[i]
        array[i]=swap
    return array

def SelectionSortDec(array,attr,start,end):
    for i in range(start,end+1):
        maxx=i
        for j in range(i,end+1):
            if(getattr(array[j],attr)>getattr(array[maxx],attr)):
                maxx=j  
        swap=array[maxx]
        array[maxx]=array[i]
        array[i]=swap
    return array
#---------------------------------------------------------
import copy
def Merge(Arr,attr,p,q,r):
    n1=q-p+1
    n2=r-q
    L=[]
    R=[]
    for i in range(n1):
        L.append(Arr[p+i])
    for j in range(n2):
         R.append(Arr[q+j+1])
    attribute=getattr(Arr[0], attr)
    if(type(attribute)!=str):
        a=copy.deepcopy(Arr[4])
        setattr(a, attr, sys.maxsize)
        L.append(a)
        R.append(a)

    else:
        a=copy.deepcopy(Arr[4])
        setattr(a, attr, "zzzzzzzzzzz")
        L.append(a)
        R.append(a)
   
    i=0
    j=0
    for k in range(p,r+1):
        if(getattr(L[i],attr)<getattr(R[j],attr)):
            Arr[k]=L[i]
            i +=1
        else:
            Arr[k]=R[j]
            j +=1
   
def MergeSort(Arr,attr,p,r):
    if(p<r):
        q=m.floor((p+r)/2)
        MergeSort(Arr,attr,p, q)
        MergeSort(Arr,attr,q+1,r)
        Merge(Arr,attr,p,q,r)
        return Arr
    else:
        return Arr 

#-------------------------------------------------------
def MergeDesc(Arr,attr,p,q,r):
    n1=q-p+1
    n2=r-q
    L=[]
    R=[]
    for i in range(n1):
        L.append(Arr[p+i])
    for j in range(n2):
         R.append(Arr[q+j+1])
    if(type(L[0])!=str):
        L.append(-sys.maxsize-1)
        R.append(-sys.maxsize-1)
    else:
        L.append("zyzzyvas")
        R.append("zyzzyvas")
   
    i=0
    j=0
    for k in range(p,r+1):
        if(getattr(L[i],attr)>getattr(R[j],attr)):
            Arr[k]=L[i]
            i +=1
        else:
            Arr[k]=R[j]
            j +=1
   
def MergeSortDesc(Arr,attr,p,r):
    if(p<r):
        q=m.floor((p+r)/2)
        MergeSortDesc(Arr,attr,p, q)
        MergeSortDesc(Arr,attr,q+1,r)
        MergeDesc(Arr,attr,p,q,r)
    else:
        return  
#-------------------------------------------------------
def BubbleSort(array,attr,start,end):
    swap_flag=False
    for i in range(start,end):
        #loop each element of arrray
        for j in range(start,end-i):
            #compare element next to it
            #if greater the next element it should swap
            if(getattr(array[j],attr)>getattr(array[j+1],attr)):
                #swapping the element by creating a temporary(swap) variable
                swap=array[j]
                array[j]=array[j+1]
                array[j+1]=swap
                swap_flag=True
        if not swap_flag:
            break
    return array           #break if the element next to it is greater than it

def BubbleSortDesc(array,attr,start,end):
    swap_flag=False
    for i in range(start,end):
        #loop each element of arrray
        for j in range(start,end-i):
            #compare element next to it
            #if greater the next element it should swap
            if(getattr(array[j],attr)<getattr(array[j+1],attr)):
                #swapping the element by creating a temporary(swap) variable
                swap=array[j]
                array[j]=array[j+1]
                array[j+1]=swap
                swap_flag=True
        if not swap_flag:
            break
    return array           #break if the element next to it is greater than it
#-----------------------------------------------------
def HybridMergeSort(array,attr,start,end):
    if (end -start< 32):      
       #value of n is 35 where merge become fast than insertion
        InsertionSort(array,attr, start, end)  
    else:
        mid=m.floor((start+end)/2)
        HybridMergeSort(array,attr,start, mid)
        HybridMergeSort(array,attr,mid+1,end)
        Merge(array,attr,start,mid,end)
        
  #-----------------------------------------------------------          
def HybridMergeSortDesc(array,attr,start,end):
    if (end -start< 32):
       #value of n is 35 where merge become fast than insertion
        InsertionSortDesc(array,attr , start, end) 
    else:
        mid=m.floor((start+end)/2)
        HybridMergeSortDesc(array,attr,start, mid)
        HybridMergeSortDesc(array,attr,mid+1,end)
        MergeDesc(array,attr,start,mid,end)
        
#-------------------------------------------------------------
#partition,randomizedpartition,quicksort for ascending          
def parititonArray(A,attr,p,r):
    x=getattr(A[r],attr)
    i=p-1
    for j in range(p,r):
        if(getattr(A[j],attr)<x):
            i +=1
            (A[i],A[j])=(A[j],A[i])
    (A[i+1],A[r])=(A[r],A[i+1])
    return i+1
def randomizedPartition(A,attr,p,r):
    i=random.randint(p,r)
    (A[r],A[i])=(A[i],A[r])
    return parititonArray(A,attr,p,r)
def QuickSort(A,attr,p,r):
    if(p<r):
        q=parititonArray(A,attr,p,r)
        #print(A)
        QuickSort(A,attr,p,q-1)
        QuickSort(A,attr,q+1,r)
    else:
        return  

def RandomizedQuickSort(A,attr,p,r):
    if(p<r):
        q=randomizedPartition(A,attr,p,r)
        RandomizedQuickSort(A,attr,p,q-1)
        RandomizedQuickSort(A,attr,q+1,r)
    else:
        return   
#------------------------------------------------------------
#partition,randomizedpartition,quicksort for descnding
def parititonArrayDesc(A,attr,p,r):
    x=getattr(A[r],attr)
    i=p-1
    for j in range(p,r):
        if(getattr(A[j],attr)>x):
            i +=1
            (A[i],A[j])=(A[j],A[i])
    (A[i+1],A[r])=(A[r],A[i+1])
    return i+1  
def RandomizedQuickSortDesc(A,attr,p,r):
    if(p<r):
        q=randomizedPartitionDesc(A,attr,p,r)
        RandomizedQuickSortDesc(A,attr,p,q-1)
        RandomizedQuickSortDesc(A,attr,q+1,r)
    else:
        return   
def randomizedPartitionDesc(A,attr,p,r):
    i=random.randint(p,r)
    (A[r],A[i])=(A[i],A[r])
    return parititonArrayDesc(A,attr,p,r)
#___________________________________
def CountingSort(A,attr,start,end): #donot accept floating points
    A1=[]
    for i in range(len(A)):
        A1.append(getattr(A[i],attr))
    attribute=getattr(A[0], attr)
    if(type(attribute)!=str):  
        maxA = int(max(A1))
        minA = int(min(A1))
        k = maxA - minA + 1
    else:
        maxA=max(A1)
        minA=min(A1)
        k=maxA-minA  

    B=[0]*len(A)
    C=[0]*k 
    for i in range(len(A1)):
        C[getattr(A[i],attr)-minA] +=1
    for j in range(1,k):
        C[j]=C[j]+C[j-1]
    for j in range(len(A)-1,-1,-1):
        B[C[getattr(A[j],attr)-minA]-1]=A[j]   #-1 because according to algorthm the A array start from 1 and C from 0 
        C[getattr(A[j],attr)-minA] -=1
    #print(B)
    for i in range(len(A)):
        A[i]=B[i]
    return A

def CountingSortDesc(A,attr,start,end): #donot accept floating points
    A1=[]
    for i in range(len(A)):
        A1.append(getattr(A[i],attr))
    attribute=getattr(A[0], attr)
    if(type(attribute)!=str):  
        maxA = int(max(A1))
        minA = int(min(A1))
        k = maxA - minA + 1
    else:
        maxA=max(A1)
        minA=min(A1)
        k=maxA-minA 
    B=[0]*len(A)
    C=[0]*k
    for i in range(len(A)):
        C[getattr(A[i],attr)-minA] +=1
    for j in range(1,k):
        C[j]=C[j]+C[j-1]
    length=len(A)
    for j in range(length-1,-1,-1):
        switch=length-C[getattr(A[j],attr)-minA]+1   #because array start from 1 so +1
        B[switch-1]=getattr(A[j],attr)   #-1 because according to algorthm the A array start from 1 and C from 0 
        C[getattr(A[j],attr)-minA] -=1
    for i in range(len(A)):
        A[i]=B[i]
    return B
#_________________________________________   
def RadixSort(A,attr,start,end):  #donot accept floating points
    A1=[]
    for i in range(len(A)):
        A1.append(getattr(A[i],attr))
    
    maxA=max(A1)-min(A1)  #-min to make it also for negative
    d=len(str(maxA))
    
    minA=int(min(A1))
    for traverse in range(d): 
        B=[]
        for x in range(10):
            B.append([])
        bucket=0
        for idx in range(len(A)):
            div=A1[idx]-minA
            for n in range(traverse+1):
                bucket=div%10
                div=div//10
            B[bucket].append(A1[idx])
        A2=[]
        for i in B:
            for j in range(len(i)):
                A2.append(i[j])
    for i in range(len(A2)):
        A[i]=A2[i]
    return A           

def RadixSortDesc(A,start,end):  #donot accept floating points
    maxA=max(A)-min(A)  #-min to make it also for negative
    d=len(str(maxA))
    
    minA=int(min(A))
    for traverse in range(d): 
        B=[]
        for x in range(10):
            B.append([])
        bucket=0
        for idx in range(len(A)):
            div=A[idx]-minA
            for n in range(traverse+1):
                bucket=div%10
                div=div//10
            B[bucket].append(A[idx])
        x=0
        for i in range(len(B)-1,-1,-1):
            for buck in B[i]:
                
                A[x]=buck
                x +=1
    return A           
import math      
#______________________________________________________   
def bucketSort(A,start,end):
    minA=min(A)
    temp=[]
    buckets=10
    for i in range(buckets):
        temp.append([])
    realMax=max(A)
    
    RealtiveMaxNum=max(A)-min(A)
    for num in A:
        if(num!=realMax):
            pointing=(num-minA)/RealtiveMaxNum      #- for negative number
            idx=math.floor(pointing*buckets)
            temp[idx].append(num)
    for InArr in temp:
        InsertionSort(InArr,0,len(InArr)-1)
    A=[]
    for i in temp:
        for j in i:
           A.append(j)
    A.append(realMax)
    return A
#for bucket descending order
def bucketSortDesc(A,start,end):
    minA=min(A)
    temp=[]
    buckets=10
    for i in range(buckets):
        temp.append([])
    realMax=max(A)
    
    RealtiveMaxNum=max(A)-min(A)
    for num in A:
        if(num!=realMax):
            pointing=(num-minA)/RealtiveMaxNum      #- for negative number
            idx=math.floor(pointing*buckets)
            temp[idx].append(num)
    for InArr in temp:
        InsertionSortDesc(InArr,0,len(InArr)-1)
    A=[]
    for i in range(len(temp)-1,-1,-1):
        for j in temp[i]:
           A.append(j)
    A.append(realMax)
    return A

#__________________________________________________________-             
def pigeonHoleSort(A,start,end):
    temp=[]# not for floating number
    minA=min(A)
    length=len(A)
    rangeA=max(A)-minA+1
    for i in range(rangeA):
        temp.append([])
    for idx in range(length):
        n=A[idx]-minA
        temp[n].append(A[idx])
    x=0
    for i in range(len(temp)):
        for lst in temp[i]:
            A[x]=lst
            x +=1
    return A
#for pigeon descending________________________________
def pigeonHoleSortDecs(A,start,end):
    temp=[]# not for floating number
    minA=min(A)
    length=len(A)
    rangeA=max(A)-minA+1
    for i in range(rangeA):
        temp.append([])
    for idx in range(length):
        n=A[idx]-minA
        temp[n].append(A[idx])
    x=0
    for i in range(len(temp)-1,-1,-1):
        for lst in temp[i]:
            A[x]=lst
            x +=1
    return A
#______________________________________________________________   
def PostmanSorting(A,start,end):  #donot accept floating points
    maxA=max(A)-min(A)  #-min to make it also for negative
    d=len(str(maxA))
    
    minA=int(min(A))
    for traverse in range(d): 
        B=[]
        for x in range(10):
            B.append([])
        bucket=0
        for idx in range(len(A)):
            div=A[idx]-minA
            for n in range(traverse,-1,-1):
                bucket=div%10
                div=div//10
            B[bucket].append(A[idx])
        A=[]
        for i in B:
            for j in range(len(i)):
                
                A.append(i[j])
    return A         
def PostmanSortingDesc(A,start,end):  #donot accept floating points
    maxA=max(A)-min(A)  #-min to make it also for negative
    d=len(str(maxA))
    
    minA=int(min(A))
    for traverse in range(d): 
        B=[]
        for x in range(10):
            B.append([])
        bucket=0
        for idx in range(len(A)):
            div=A[idx]-minA
            for n in range(traverse,-1,-1):
                bucket=div%10
                div=div//10
            B[bucket].append(A[idx])
        x=0
        for i in range(len(B)-1,-1,-1):
            for buck in B[i]:
                
                A[x]=buck
                x +=1
    return A               
def CockTailSorting(A,start,end):
    swap_nothing=False
    while(swap_nothing==False):
        swap_nothing=True
        for i in range(start,end):
            if(A[i]>A[i+1]):
                A[i],A[i+1]=A[i+1],A[i]
                swap_nothing=False
        if(swap_nothing):
            break   #if array sorted break
        end -=1
        swap_nothing=True
        for j in range(end-1,start-1,-1):
            if(A[j+1]<A[j]):
                A[j],A[j+1]=A[j+1],A[j]
                swap_nothing=False
        start +=1
        if(swap_nothing):
            break #if array sorted break  
    return A
def CockTailSortingDesc(A,start,end):
    swap_nothing=False
    while(swap_nothing==False):
        swap_nothing=True
        for i in range(start,end):
            if(A[i]<A[i+1]):
                A[i],A[i+1]=A[i+1],A[i]
                swap_nothing=False
        if(swap_nothing):
            break   #if array sorted break
        end -=1
        swap_nothing=True
        for j in range(end-1,start-1,-1):
            if(A[j+1]>A[j]):
                A[j],A[j+1]=A[j+1],A[j]
                swap_nothing=False
        start +=1
        if(swap_nothing):
    
            break   #if array sorted break 
    return A     

#-----------------Increasing Order-----------------
def max_heapify(A,len_of_arr,parent):
    largest=parent
    left=2*largest
    right=left+1
    if(left<len_of_arr and A[left]>A[parent]):
        largest=left
    if(right<len_of_arr and A[right]>A[largest]):
        largest=right
    if(largest!=parent):
        A[largest],A[parent]=A[parent],A[largest]
        max_heapify(A, len_of_arr, largest)

def HeapSort(A):
    n=len(A)
    #---Building Heap Sort---
    for i in range(len(A)//2-1,-1,-1):
        max_heapify(A, n, i)
    # -----------------------
    # ----Deleting from Array----
    for i in range(len(A)-1,0,-1):
        A[0],A[i]=A[i],A[0] #Swapping root with last leaf node 
        max_heapify(A, i, 0) #decreasing the length of array
    # ---------------------------    
#---------------------------------------------------------
#--------------Decreasing Order---------------------------
def min_heapify(A,len_of_arr,i): # min_heapify runs in O(n) times
    smallest=i
    l=(2*i)
    r=(2*i)+1
    if(l<len_of_arr and A[l]<A[smallest]):
        smallest=l
    if(r<len_of_arr and A[r]<A[smallest]):
        smallest=r
    if(smallest!=i):
        (A[i],A[smallest])=(A[smallest],A[i])
        min_heapify(A,len_of_arr, smallest)
def HeapSortDecreasing(A,start,end):
    n=len(A)
    for i  in range(len(A)//2-1,-1,-1): #Build Max Heapify and it takes O(nlgn) time
        min_heapify(A,n, i)
    for i in range(len(A)-1,0,-1): #Deleting the last index from array and then again applying the max heapify 
        A[0],A[i]=A[i],A[0]
        min_heapify(A,i, 0)
    print(A)
#---------------------------------------------------------

def Binary_Search(A,low,high,value):
    if(low==high):
        if(A[low]>value):
            return low
        else:
            return low+1
    elif(low>high):
        return low
    else:
        mid=math.floor((low+high)/2)
        if(A[mid]==value):
            return mid
        elif(A[mid]<value):
            return Binary_Search(A, mid+1, high, value)
        else:
            return Binary_Search(A, low, mid-1, value)

def Binary_Insertion_Sort(A):
    for i in range(1,len(A)):
        key=A[i]
        k=Binary_Search(A, 0, i-1, key)
        A=A[:k]+[key]+A[k:i]+A[i+1:]
    return A

def Shell_Sort(A):
    g=len(A)//2
    while (g>0):
        k=g
        while(k<len(A)):      
            j=k-g
            while(j>=0):
                if(A[j+g]>A[j]):
                    break
                else:
                    A[j+g],A[j]=A[j],A[j+g]
                j=j-g     
            k+=1
        g=g//2
    return A


def Block_Sort():
    pass        
           
#A=dict{0:'1',2:'2'}   
arr=[12,32,1,43,21,122]
A=Shell_Sort(arr)
print(A)
print("This is me")
# A=[-9,5324,54,5234,4352,5432,542,991,6,-8,884,33,5454,3545,554,345345,4554,-333,-44,4444,123,231,213,321,102]
# #A=['a','A','b','B','z','Z','ZZZZ','zzzz']
# B=A.copy()
# B.sort()
# #B.reverse()
# print(B)
# Hea(A)
# print(A)
# print(A==B)


