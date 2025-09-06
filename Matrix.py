# 41. Transpose
mat=[[1,2,3],[4,5,6]]
print(list(zip(*mat)))

# 42. Multiply matrices
A=[[1,2],[3,4]]
B=[[2,0],[1,2]]
res=[[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]
print(res)

# 43. Boundary elements
mat=[[1,2,3],[4,5,6],[7,8,9]]
n=len(mat)
for i in range(n):
    for j in range(n):
        if i in [0,n-1] or j in [0,n-1]:
            print(mat[i][j], end=" ")
print()

# 44. Diagonal sum
mat=[[1,2,3],[4,5,6],[7,8,9]]
print(sum(mat[i][i] for i in range(len(mat)))+sum(mat[i][len(mat)-i-1] for i in range(len(mat)))-mat[len(mat)//2][len(mat)//2])

# 45. Rotate by 90
mat=[[1,2,3],[4,5,6],[7,8,9]]
print(list(zip(*mat[::-1])))

# 46. Spiral order
def spiral(mat):
    res=[]
    while mat:
        res+=mat[0]; mat=mat[1:]
        if mat: mat=list(zip(*mat))[::-1]
    return res
print(spiral([[1,2,3],[4,5,6],[7,8,9]]))
