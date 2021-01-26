# A* algorithm for 8-puzzle problem by turtle
# Have a great time, Good luck!
# programming by An deukha
# email: dplus1016@gyeongui.hs.kr

import turtle as t
import time
import os
from copy import deepcopy
import random as rn

# 가장 유망한 노드로 선택된 노드의 자식 노드 저장
# 가장 유망한 노드로 선정이 되면 삭제
# [h, node, g, num, p]
Olist=[] 

Plist=[] # 방문한 모든 노드 저장
Path=[]  # 해답 경로 저장

# 해결이 가능한 초기 상태
Snode=[[1,2,3],
       [4,5,8],
       [6,0,7]]
# 목표 상태
Gnode=[[1,2,3],
       [4,5,6],
       [7,8,0]]
'''
# 해결이 불가능한 초기 상태
Snode=[[1,2,4],
       [5,3,7],
       [0,8,6]]
# 목표 상태
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
    Nlist[0]=evaluate(node)+g  # 평가함수 값: f=h+g
    Nlist[1]=node              # 생성 노드(2차원 배열)
    Nlist[2]=g                 # 초기 노드부터 현재 노드까지의 거리
    Nlist[3]=num               # 각 노드별 고유 번호
    Nlist[4]=p                 # 부모 노드의 고유 번호
    return Nlist

# 노드 출력
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

# 0(빈칸)의 위치 찾기(2차원 배열 인덱스로 반환)
def findzero(node):
    for i in range(3):
        for j in range(3): 
            if node[i][j]==0: 
                return i,j

# 이미 생성된 노드들 중에 똑같은 것이 있는지 확인
def chkNode(node):
    for i in Plist:
        if i[1] == node: return False
    return True

# 가장 유망한 노드 선택
def SelectNode():
    tmp=Olist[0][0]  # 평가값이 가장 유망한(낮은) 값
    i=0 
    for O in Olist:
        if O[0]!=tmp: break  # 가장 유망한 노드가 복수일 경우, 유망한 노드의 인덱스들 중에..
        i+=1
    return rn.randint(0,i-1) # ..무작위로 선정하여 반환

# Olist와 Plist는 역할이 다름
# Olist는 가장 유망한 노드를 선택하기 위한 저장 공간
# Plist는 방문한 모든 노드 저장
Olist.append(NodeCreate(Snode,0,0,0))  # 초기 노드 생성
Plist.append([0,Snode,0])              # 초기 노드 생성

# cnt와 num은 다름
cnt=0  # 가장 유망한 노드를 선택한 횟수(탐색 횟수)
num=0  # 생성한 모든 노드의 고유 번호
while 1:
    i=SelectNode()
    cnt+=1
    print(f"count: {cnt}")
    print(f"selectNode: {i}")

    currentnode=Olist[i][1]  # 현재 노드
    f=Olist[i][0]
    g=Olist[i][2]
    p=Olist[i][3]  # 부모노드의 고유 번호
    
    del Olist[i]   # 가장 유망한 노드로 선택한 노드를 Olist에서 삭제
    
    NodePrint(currentnode,f,g,p)  # 현재 노드(상태) 출력
    
    if currentnode == Gnode:  # 현재 노드(상태)가 목표 상태인지 검사
        Pnum=p
        print("success!!")
        break

    Bnodes=babyNode(currentnode)  # 자식 노드 생성
    for i in Bnodes:
        num+=1  # 고유번호 최신화
        Olist.append(NodeCreate(i,g+1,num,p))  # 자식 노드를 Olist에 추가
        Plist.append([num,i,p])  # 자식 노드를 Plist에 추가

    Olist=sorted(Olist, key=lambda x:x[0])  # Olist에 있는 노드들을 평가함수 값(h)순으로 정렬

# 경로 탐색 완료
# Plist에 있는 노드들을 고유번호(num) 순으로 정렬
Plist=sorted(Plist, key=lambda x:x[0])

# 목표 상태에 도달한 노드에서부터 부모 노드의 고유번호를 참조하여 경로 추적
while True:
    Path.append(Plist[Pnum][1])
    if not Pnum: break
    Pnum=Plist[Pnum][2]

print()  # 줄바꿈
Path.reverse()  # 역방향으로 되어있는 경로를 순방향으로 조정
for i in Path:  # 최종 경로 출력
    for j in i: 
        print(j) 
    print() 

#----------turtle--------------#

T=[]
W=[]
for i in range(9):
    T.append(t.Turtle())
    W.append(t.Turtle())
    T[i].ht()
    W[i].ht()

d=100
c=10
x_i=-(d*3+c*2)/2; y_i=(d*3+c*2)/2

def rect(x,y,tt,ww,num): 
    n=str(num)
    ww.clear(); ww.speed(0); ww.penup(); ww.goto(x+d/2, y-d/2-10)
    tt.clear(); tt.speed(0); tt.penup(); tt.goto(x,y); tt.pendown()
    for i in range(4):
        tt.fd(d)
        tt.right(90)
    ww.write(n,False,"center",("",20))
    time.sleep(0.1)

def move(i, mode):
    for j in range(1,12): 
        x[i]=x[i] + (20*(mode//2)-30)*(mode//3)
        y[i]=y[i] + (20*mode-30)*(1-mode//3) 
        rect(x[i],y[i],T[i],W[i],i)

hp=[]
for i in Snode:
    for j in i: 
        hp.append(j)

x=[0]*10
y=[0]*10

for i in range(1,9):
    tmp=hp.index(i)
    x[i]=x_i+(d+c)*(tmp%3)
    y[i]=y_i-(d+c)*(tmp//3)
    rect(x[i],y[i],T[i],W[i],i)

#   2    1=y-10 ; 2=y+10   y + (20*mode-30)*(1-mode//3)   
# 3   4  3=x-10 ; 4=x+10   x + (20*(mode//2)-30)*(mode//3)                        
#   1    

time.sleep(2)

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
