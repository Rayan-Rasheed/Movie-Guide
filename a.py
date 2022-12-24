#KMP string searching algorithm
# def computingLPSarray(pattern):
#     lpsArr=[0]*len(pattern)     #making Longest prefix which is also suffix
#     lpsArr[0]=0
#     lpsLength=0
#     idx=1       #initializing 1 to start compare with next
#     while(idx < len(pattern)):
#         if (pattern[lpsLength]==pattern[idx]):
#             lpsLength +=1
#             lpsArr[idx]=len
#             idx +=1
#         else:
#             if lpsLength==0:
#                 lpsArr[idx]=0
#                 idx +=1
#             else:
#                 lpsLength=lpsArr[lpsLength-1]
#     return lpsArr
# def KMPStringSearching(text,pattern):
#         lpsArr=computingLPSarray(pattern)
#         i=0
#         j=0
#         while i < len(text):
#             if(text[i]==pattern[j]):
#                  i +=1
#                  j +=1
#             if(j==len(pattern)):
#                 ret= i-j
#                 j=lpsArr[j-1]
#                 return ret
#             elif(i<len(text) and pattern[j]!=text[i]):
                
#                 if(j==0):
#                     i +=1
#                 else:
#                     j=lpsArr[j-1]
# # KMP string search algorithm end
def parititonArray(A,p,r):
    x=A[r]
    i=p-1
    for j in range(p,r):
        if(A[j]<x):
            i +=1
            (A[i],A[j])=(A[j],A[i])
    (A[i+1],A[r])=(A[r],A[i+1])
    return i+1
def QuickSort(A,p,r):
    if(p<=r):
        q=parititonArray(A,p,r)
        print(A)
        QuickSort(A,p,q-1)
        QuickSort(A,q+1,r)
        
    else:
        return  
A=[11,0,7,5,5,2,2,1,7,8]
QuickSort(A,0,len(A)-1)
print(A)