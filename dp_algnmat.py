mat=5
mis=-4
s1="acgtacgtacgtacgt"
s2="acgtacgtacgtacgt"
matrix=[[0]*(len(s1)+1)]*(len(s2)+1)
def rec(s1,s2,i,j):
    global matrix
    if(i==1 and j==1):
        if(s1[i-1]==s2[j-1]):
            matrix[i][j]=matrix[i-1][j-1]+mat
        else:
            matrix[i][j]=max(matrix[i-1][j-1]+mis,matrix[i][j-1]+mis,matrix[i-1][j]+mis)
    else:
        rec(s1,s2,i-1,j)
        rec(s1,s2,i,j-1)
        if(s1[i-1]==s2[j-1]):
            matrix[i][j]=matrix[i-1][j-1]+mat
        else:
            matrix[i][j]=max([matrix[i-1][j-1]+mis,matrix[i][j-1]+mis,matrix[i-1][j]+mis])
rec(s1,s2,len(s1),len(s2))
print("-",end="\t")
for i in s1:
    print(s1,end="\t")
print("-",end="\t")
for i in range(len(s2)+1):
    for j in range(len(s1)+1):
        print(matrix[i])
    print(s2[i],end="\t")
