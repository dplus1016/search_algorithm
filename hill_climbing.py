from copy import deepcopy

# t2=deepcopy(t1)
# Tlist=[t1,t2]; s=sorted(Tlist, key=lambda x:x[0])

Olist=[] # open list
Clist=[] # close list
nodeNum=1
'''
Snode=[[1,2,4],
       [5,0,7],
       [3,6,8]]

Gnode=[[1,4,7],
       [2,5,8],
       [3,6,0]]

Snode=[[2,8,3],
       [1,6,4],
       [7,0,5]]

Gnode=[[1,2,3],
       [8,0,4],
       [7,6,5]]
'''

Snode=[[2,8,3],
       [1,6,4],
       [7,0,5]]

Gnode=[[1,2,3],
       [4,5,6],
       [7,8,0]]

# 휴리스틱 정보(평가함수): 제 자리가 아닌 퍼즐의 숫자
def evaluate(node):
    cnt=0
    for i in range(3):
        for j in range(3):
            if node[i][j]==Gnode[i][j]:
                cnt+=1
    return 9-cnt

# 평가함수 결과를 포함하는 노드 생성
def NodeCreate(node,parentsnode):
    global nodeNum
    Nlist=[0,[],[]]
    Nlist[0]=evaluate(node)
    Nlist[1]=node
    Nlist[2]=parentsnode
    return Nlist

# 오픈리스트에 추가(선택된 노드의 자식 노드 추가)
def openList(node):
    global Olist
    Olist.append(node)

# 클로즈리스트에 선택된 노드를 추가(오픈리스트에서는 삭제)
def closeList():
    global Olist
    global Clist
    Clist.append(Olist[0][1])
    del Olist[0]

# current 노드 출력
def NodePrint(node):
    for i in node:
        print(i)
    print("---------")

# 자식노드 생성
def babyNode(node,parentsnode):
    i,j=findzero(node)
    
    leftnode=deepcopy(node)
    rightnode=deepcopy(node)
    upnode=deepcopy(node)
    downnode=deepcopy(node)

    totalbabynode=[]
    
    if j-1>=0: 
        leftnode[i][j-1],leftnode[i][j]=leftnode[i][j],leftnode[i][j-1]
        if leftnode!=parentsnode: totalbabynode.append(leftnode)
    if i+1<=2: 
        downnode[i+1][j],downnode[i][j]=downnode[i][j],downnode[i+1][j]
        if downnode!=parentsnode: totalbabynode.append(downnode)
    if j+1<=2: 
        rightnode[i][j+1],rightnode[i][j]=rightnode[i][j],rightnode[i][j+1]
        if rightnode!=parentsnode: totalbabynode.append(rightnode) 
    if i-1>=0: 
        upnode[i-1][j],upnode[i][j]=upnode[i][j],upnode[i-1][j]
        if upnode!=parentsnode: totalbabynode.append(upnode)    

    return totalbabynode

def findzero(node):
    for i in range(3):
        for j in range(3): 
            if node[i][j]==0: 
                return i,j

openList(NodeCreate(Snode,[]))

while Olist:
    currentnode=Olist[0][1]
    parentsnode=Olist[0][2]
    closeList()
    if currentnode == Gnode:
        print("success!!")
        break
    NodePrint(currentnode)
    Bnodes=babyNode(currentnode,parentsnode)
    for i in Bnodes:
        openList(NodeCreate(i,currentnode))
    Olist=sorted(Olist, key=lambda x:x[0])

print("---close---")

for i in Clist: 
    for j in i: 
        print(j)
    print("--------")