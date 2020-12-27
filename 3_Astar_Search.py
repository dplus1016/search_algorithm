# A* algorithm for 8-puzzle problem
# Have a great time, Good luck!
# programming by An deukha
# email: dplus1016@gyeongui.hs.kr

from copy import deepcopy
import random as rn

Olist=[] # open list [0,[[]],[[]],0]
Clist=[] # close list [[]]

'''
# solvable initial board
Snode=[[5,2,4],
       [1,0,7],
       [3,6,8]]

Gnode=[[1,4,7],
       [2,5,8],
       [3,6,0]]

# unsolvable initial board
Snode=[[1,2,4],
       [5,0,7],
       [3,6,8]]

Gnode=[[1,4,7],
       [2,5,8],
       [3,6,0]]

# solvable initial board
Snode=[[8,3,2],
       [1,6,4],
       [7,0,5]]

Gnode=[[1,2,3],
       [8,0,4],
       [7,6,5]]

# unsolvable initial board
Snode=[[8,2,3],
       [1,6,4],
       [7,0,5]]

Gnode=[[1,2,3],
       [8,0,4],
       [7,6,5]]
'''
# solvable initial board
Snode=[[0,1,2],
       [3,4,5],
       [8,6,7]]

Gnode=[[0,1,2],
       [3,4,5],
       [6,7,8]]
'''
# unsolvable initial board
Snode=[[0,1,2],
       [3,4,5],
       [6,8,7]]

Gnode=[[0,1,2],
       [3,4,5],
       [6,7,8]]
'''

# 휴리스틱 정보(평가함수): 제 자리가 아닌 퍼즐의 숫자
def evaluate(node):
    cnt=0
    for i in range(3):
        for j in range(3):
            if node[i][j]==Gnode[i][j]:
                cnt+=1
    return 9-cnt

# 평가함수 결과를 포함하는 노드 생성
def NodeCreate(node,parentsnode,cnt):
    Nlist=[0,[],[],0]
    Nlist[0]=evaluate(node)+cnt
    Nlist[1]=node
    Nlist[2]=parentsnode
    Nlist[3]=cnt
    return Nlist

# 오픈리스트에 추가(선택된 노드의 자식 노드 추가)
def openList(node):
    global Olist
    Olist.append(node)

# 클로즈리스트에 선택된 노드를 추가(오픈리스트에서는 삭제)
def closeList(i):
    global Olist
    global Clist
    Clist.append(Olist[i][1])
    del Olist[i]

# current 노드 출력
def NodePrint(node,f,g):
    print(f"h={f-g}, g={g}")
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
        if chkNode(leftnode): totalbabynode.append(leftnode)
    if i+1<=2: 
        downnode[i+1][j],downnode[i][j]=downnode[i][j],downnode[i+1][j]
        if chkNode(downnode): totalbabynode.append(downnode)
    if j+1<=2: 
        rightnode[i][j+1],rightnode[i][j]=rightnode[i][j],rightnode[i][j+1]
        if chkNode(rightnode): totalbabynode.append(rightnode)
    if i-1>=0: 
        upnode[i-1][j],upnode[i][j]=upnode[i][j],upnode[i-1][j]
        if chkNode(upnode): totalbabynode.append(upnode) 

    return totalbabynode

def findzero(node):
    for i in range(3):
        for j in range(3): 
            if node[i][j]==0: 
                return i,j

def chkNode(node):
    global Olist
    global Clist
    for i in Olist:
        if i[1] == node: return False
    for i in Clist: 
        if i == node: return False
    return True

def SelectNode():
    global Olist
    tmp=Olist[0][0]
    i=0 
    for O in Olist:
        if O[0]!=tmp: break
        i+=1
    return rn.randint(0,i-1)
    #return 0


openList(NodeCreate(Snode,[],0))

cnt=0
while 1:
    i=SelectNode()
    cnt+=1
    print(f"count: {cnt}")
    print(f"selectNode: {i}")

    currentnode=Olist[i][1]
    parentsnode=Olist[i][2]
    f=Olist[i][0]
    g=Olist[i][3]
    
    closeList(i)
    if currentnode == Gnode:
        NodePrint(currentnode,f,g)
        print("success!!")
        break

    NodePrint(currentnode,f,g)
    Bnodes=babyNode(currentnode,parentsnode)
    for i in Bnodes:
        openList(NodeCreate(i,currentnode,g+1))
    Olist=sorted(Olist, key=lambda x:x[0])
