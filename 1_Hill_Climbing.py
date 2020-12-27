from copy import deepcopy

# solvable initial board
Snode=[[1,2,3],
       [0,4,6],
       [7,5,8]]

Gnode=[[1,2,3],
       [4,5,6],
       [7,8,0]]
'''
# unsolvable initial board
Snode=[[2,8,3],
       [1,6,4],
       [7,0,5]]

Gnode=[[1,2,3],
       [8,0,4],
       [7,6,5]]
'''
# 휴리스틱 정보(평가함수): 제 자리가 아닌 퍼즐의 숫자
def evaluate(node):
    cnt=0
    for i in range(3):
        for j in range(3):
            if node[i][j]==Gnode[i][j]:
                cnt+=1
    return 9-cnt

# current 노드 출력
def NodePrint(node,h):
    print(f"h={h}")
    for i in node:
        print(i)
    print("---------")

# 자식노드 생성
def babyNode(node):
    i,j=findzero(node)
    
    leftnode=deepcopy(node)
    rightnode=deepcopy(node)
    upnode=deepcopy(node)
    downnode=deepcopy(node)

    totalbabynode=[]
    
    if j-1>=0: 
        leftnode[i][j-1],leftnode[i][j]=leftnode[i][j],leftnode[i][j-1]
        totalbabynode.append(leftnode)
    if i+1<=2: 
        downnode[i+1][j],downnode[i][j]=downnode[i][j],downnode[i+1][j]
        totalbabynode.append(downnode)
    if j+1<=2: 
        rightnode[i][j+1],rightnode[i][j]=rightnode[i][j],rightnode[i][j+1]
        totalbabynode.append(rightnode) 
    if i-1>=0: 
        upnode[i-1][j],upnode[i][j]=upnode[i][j],upnode[i-1][j]
        totalbabynode.append(upnode)    

    return totalbabynode

def findzero(node):
    for i in range(3):
        for j in range(3): 
            if node[i][j]==0: 
                return i,j

cnt=0
currentnode=Snode
while True:
    cnt+=1
    h=evaluate(currentnode)
    NodePrint(currentnode,h)
    print(f"count: {cnt}")

    if currentnode == Gnode:
        print("success!!")
        break
    
    Bnodes=babyNode(currentnode)
    min_h=h
    tmp_node=currentnode
    for i in Bnodes:
        tmp_h=evaluate(i)
        if min_h>tmp_h:
            min_h=tmp_h
            tmp_node=i
    if currentnode == tmp_node:
        print("failure!!")
        break

    currentnode = tmp_node
