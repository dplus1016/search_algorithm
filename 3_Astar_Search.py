# A* algorithm for 8-puzzle problem
# Have a great time, Good luck!
# programming by An deukha
# email: dplus1016@gyeongui.hs.kr

from copy import deepcopy
import random as rn

Olist=[] # open list [0,[[]],0,0,0] [h, node, g, num, p]
Clist=[] # close list [[]]
Plist=[] # path list 
Path=[]

# solvable initial board
Snode=[[1,2,3],
       [4,5,8],
       [6,0,7]]

Gnode=[[1,2,3],
       [4,5,6],
       [7,8,0]]
'''
Snode=[[1,2,4],
       [5,3,7],
       [0,8,6]]

Gnode=[[1,2,3],
       [4,5,6],
       [7,8,0]]
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
def NodeCreate(node,g,num,p):
    Nlist=[0,[],0,0,0]
    Nlist[0]=evaluate(node)+g
    Nlist[1]=node
    Nlist[2]=g
    Nlist[3]=num
    Nlist[4]=p
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
def NodePrint(node,f,g,num):
    print(f"f={f}, g={g}, num={num}")
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
    tmp=Olist[0][0]  # 평가값이 가장 유망한(낮은) 값
    i=0 
    for O in Olist:
        if O[0]!=tmp: break  # 평가값이 가장 유망한(낮은) 것들이 복수일 경우
        i+=1
    return rn.randint(0,i-1)
    #return 0

openList(NodeCreate(Snode,0,0,0))
Plist.append([0,Snode,0])

cnt=0
num=0
while 1:
    i=SelectNode()
    cnt+=1
    print(f"count: {cnt}")
    print(f"selectNode: {i}")

    currentnode=Olist[i][1]
    f=Olist[i][0]
    g=Olist[i][2]
    p=Olist[i][3]
    
    closeList(i)
    
    NodePrint(currentnode,f,g,p)
    
    if currentnode == Gnode:
        Pnum=p
        print("success!!")
        break

    Bnodes=babyNode(currentnode)
    for i in Bnodes:
        num+=1
        openList(NodeCreate(i,g+1,num,p))
        Plist.append([num,i,p])
    Olist=sorted(Olist, key=lambda x:x[0])

Plist=sorted(Plist, key=lambda x:x[0])

while True:
    Path.append(Plist[Pnum][1])
    if not Pnum: break
    Pnum=Plist[Pnum][2]

print()
Path.reverse()
for i in Path: 
    for j in i: 
        print(j) 
    print() 
