# A* algorithm for 8-puzzle problem by turtle
# Have a great time, Good luck!
# programming by An deukha
# email: dplus1016@gyeongui.hs.kr

import turtle as t
import time
import os
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
Snode=[[1,2,3],
       [4,6,5],
       [8,7,0]]
Gnode=[[1,2,3],
       [4,5,6],
       [7,8,0]]

# unsolvable initial board
Snode=[[8,2,3],
       [1,6,4],
       [7,0,5]]
Gnode=[[1,2,3],
       [8,0,4],
       [7,6,5]]
# solvable initial board
Snode=[[0,1,2],
       [3,4,5],
       [8,6,7]]
Gnode=[[0,1,2],
       [3,4,5],
       [6,7,8]]
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

#----------turtle--------------#

t.ht()
t1=t.Turtle() ; w1=t.Turtle() ; t1.ht() ; w1.ht()
t2=t.Turtle() ; w2=t.Turtle() ; t2.ht() ; w2.ht() 
t3=t.Turtle() ; w3=t.Turtle() ; t3.ht() ; w3.ht() 
t4=t.Turtle() ; w4=t.Turtle() ; t4.ht() ; w4.ht() 
t5=t.Turtle() ; w5=t.Turtle() ; t5.ht() ; w5.ht()
t6=t.Turtle() ; w6=t.Turtle() ; t6.ht() ; w6.ht() 
t7=t.Turtle() ; w7=t.Turtle() ; t7.ht() ; w7.ht() 
t8=t.Turtle() ; w8=t.Turtle() ; t8.ht() ; w8.ht() 

d=100
c=10
x_i=-(d*3+c*2)/2; y_i=(d*3+c*2)/2

def rect(x,y,tt,ww,num): 
    n=str(num)
    ww.clear()
    ww.speed(0)
    ww.penup()
    ww.goto(x+d/2, y-d/2-10)
    tt.clear()
    tt.speed(0)
    tt.penup()
    tt.goto(x,y)
    tt.pendown()
    for i in range(4):
        tt.fd(d)
        tt.right(90)
    ww.write(n,False,"center",("",20))
    time.sleep(0.1)

def move(chk, mode):
    for i in range(1,12): 
        if chk==1:
            x[chk]=x[chk] + (20*(mode//2)-30)*(mode//3) ; y[chk]=y[chk] + (20*mode-30)*(1-mode//3) 
            rect(x[chk],y[chk],t1,w1,chk)
        elif chk==2:
            x[chk]=x[chk] + (20*(mode//2)-30)*(mode//3) ; y[chk]=y[chk] + (20*mode-30)*(1-mode//3) 
            rect(x[chk],y[chk],t2,w2,chk)
        elif chk==3:
            x[chk]=x[chk] + (20*(mode//2)-30)*(mode//3) ; y[chk]=y[chk] + (20*mode-30)*(1-mode//3) 
            rect(x[chk],y[chk],t3,w3,chk)
        elif chk==4:
            x[chk]=x[chk] + (20*(mode//2)-30)*(mode//3) ; y[chk]=y[chk] + (20*mode-30)*(1-mode//3) 
            rect(x[chk],y[chk],t4,w4,chk)
        elif chk==5:
            x[chk]=x[chk] + (20*(mode//2)-30)*(mode//3) ; y[chk]=y[chk] + (20*mode-30)*(1-mode//3) 
            rect(x[chk],y[chk],t5,w5,chk)
        elif chk==6:
            x[chk]=x[chk] + (20*(mode//2)-30)*(mode//3) ; y[chk]=y[chk] + (20*mode-30)*(1-mode//3) 
            rect(x[chk],y[chk],t6,w6,chk)
        elif chk==7:
            x[chk]=x[chk] + (20*(mode//2)-30)*(mode//3) ; y[chk]=y[chk] + (20*mode-30)*(1-mode//3) 
            rect(x[chk],y[chk],t7,w7,chk)
        elif chk==8:
            x[chk]=x[chk] + (20*(mode//2)-30)*(mode//3) ; y[chk]=y[chk] + (20*mode-30)*(1-mode//3) 
            rect(x[chk],y[chk],t8,w8,chk)

hp=[]
for i in Snode:
    for j in i: 
        hp.append(j)

x=[0]*10
y=[0]*10

tmp=hp.index(1)
x[1]=x_i+(d+c)*(tmp%3) ; y[1]=y_i-(d+c)*(tmp//3)
rect(x[1],y[1],t1,w1,1)

tmp=hp.index(2)
x[2]=x_i+(d+c)*(tmp%3) ; y[2]=y_i-(d+c)*(tmp//3)
rect(x[2],y[2],t2,w2,2)

tmp=hp.index(3)
x[3]=x_i+(d+c)*(tmp%3) ; y[3]=y_i-(d+c)*(tmp//3)
rect(x[3],y[3],t3,w3,3)

tmp=hp.index(4)
x[4]=x_i+(d+c)*(tmp%3) ; y[4]=y_i-(d+c)*(tmp//3)
rect(x[4],y[4],t4,w4,4)

tmp=hp.index(5)
x[5]=x_i+(d+c)*(tmp%3) ; y[5]=y_i-(d+c)*(tmp//3)
rect(x[5],y[5],t5,w5,5)

tmp=hp.index(6)
x[6]=x_i+(d+c)*(tmp%3) ; y[6]=y_i-(d+c)*(tmp//3)
rect(x[6],y[6],t6,w6,6)

tmp=hp.index(7)
x[7]=x_i+(d+c)*(tmp%3) ; y[7]=y_i-(d+c)*(tmp//3)
rect(x[7],y[7],t7,w7,7)

tmp=hp.index(8)
x[8]=x_i+(d+c)*(tmp%3) ; y[8]=y_i-(d+c)*(tmp//3)
rect(x[8],y[8],t8,w8,8)

#   2    1=y-10 ; 2=y+10   x + (20*(mode//2)-30)*(mode//3) ; y + (20*mode-30)*(1-mode//3) 
# 3   4  3=x-10 ; 4=x+10                           
#   1    

time.sleep(3)

#chk=0
#mode=0

i,j=findzero(Path[0])
pos=i*3+j
for index in range(1,len(Path)): 
    i,j=findzero(Path[index])
    tmp=(i*3+j)-pos
    chk=Path[index-1][i][j]
    if tmp==3: # 0 아래쪽
        move(chk,2)
    elif tmp==-3: # 0 위쪽
        move(chk,1)
    elif tmp==1:  # 0 오른쪽
        move(chk,3)
    elif tmp==-1: # 0 왼쪽
        move(chk,4)

    pos=(i*3+j)

os.system("Pause")
