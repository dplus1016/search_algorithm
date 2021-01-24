# Hill Climbing algorithm for 8-puzzle problem
# Have a great time, Good luck!
# programming by An deukha
# email: dplus1016@gyeongui.hs.kr

from copy import deepcopy

# 해결이 가능한 초기 상태
Snode=[[1,2,3],
       [0,4,6],
       [7,5,8]]
# 목표 상태
Gnode=[[1,2,3],
       [4,5,6],
       [7,8,0]]
'''
# 해결이 불가능한 초기 상태
Snode=[[2,8,3],
       [1,6,4],
       [7,0,5]]
# 목표 상태
Gnode=[[1,2,3],
       [8,0,4],
       [7,6,5]]
'''
# 휴리스틱 정보(평가함수): 제 자리가 아닌 타일의 개수
def evaluate(node):
    cnt=0
    for i in range(3):
        for j in range(3):
            if node[i][j]==Gnode[i][j]:
                cnt+=1
    return 9-cnt

# 노드 출력
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

# 0(빈칸)의 위치 찾기(2차원 배열 인덱스로 반환)
def findzero(node):
    for i in range(3):
        for j in range(3): 
            if node[i][j]==0: 
                return i,j

cnt=0  # 가장 유망한 노드를 선택한 횟수(탐색 횟수)
currentnode=Snode  # 현재 노드 초기화
while True:
    cnt+=1  
    print(f"count: {cnt}")
    h=evaluate(currentnode)   # 현재 노드 평가 함수 값
    NodePrint(currentnode,h)  # 현재 노드(상태) 출력
    
    if currentnode == Gnode:  # 현재 노드(상태)가 목표 상태인지 검사
        print("success!!")
        break
    
    Bnodes=babyNode(currentnode)  # 자식 노드 생성
    min_h=h  # 현재 노드의 평가 함수 값을 최소값으로 지정
    tmp_node=currentnode
    for i in Bnodes:
        tmp_h=evaluate(i)  # 자식 노드의 평가 함수 값
        if min_h>tmp_h:    # 자식 노드의 평가 함수 값 중에서 현재 노드의 평가 함수 값보다 작은 값 검색
            min_h=tmp_h
            tmp_node=i
    if currentnode == tmp_node:  # 유망한 노드를 찾지 못한 경우 탐색 종료
        print("failure!!")
        break

    currentnode = tmp_node
