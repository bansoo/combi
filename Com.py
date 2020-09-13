#리스트받아서 중복 제거 후 반환
def get_list(lst):
    newlst = []
    for i in lst:
        if i not in newlst:
            newlst.append(i)
    return newlst


def init_combi(lst):
    combi(lst,0)

#슬라이스하고 재귀
def combi(lst, cnt):
    if cnt == len(lst):
        print(lst)
        return
    print(cnt)
    combi(lst[:], cnt+1)
    lst.pop(cnt)
    combi(lst[:], cnt)


lst = input().split(",")
init_combi(get_list(lst))
