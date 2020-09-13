#(2) 리스트받아서 중복 제거 후 반환
def get_list(lst):
    newlst = []
    for i in lst:
        if i not in newlst:
            newlst.append(i)
    return newlst

#(3) 초기 설정
def init_combi(lst):
    combi(lst,0)

#(4) 재귀(cnt 원소 pop하면서 재귀)
def combi(lst, cnt):
    if cnt == len(lst):
        if cnt !=0: #(5)공집합 제거용 조건문
            print(lst)
            #print(cnt)
            return
        return

    combi(lst[:], cnt+1)
    lst.pop(cnt)
    combi(lst[:], cnt)


lst = input().split(",")     # (1) "1,2,3"과 같은 형태로 input
init_combi(get_list(lst))
