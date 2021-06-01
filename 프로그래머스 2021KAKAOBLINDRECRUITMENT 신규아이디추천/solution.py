def solution(new_id):
    answer = ''
    exc = list('~!@#$%^&*()=+[{]}:?,<>/')
    templist = list(new_id)
    removelist = []
    # 1단계 string 라이브러리의 대문자 소문자 함수
    for i in range(len(templist)):
        if templist[i].isupper():
            templist[i] = templist[i].lower()
    # 2단계 >> for i in templist 이 구문을 쓰면 도중에 pop, remove되면 커서가 바뀐다... 주의
    removecnt = 0
    for i in range(len(templist)):
        if templist[i - removecnt] in exc:
            templist.pop(templist.index(templist[i - removecnt]))
            removecnt = removecnt + 1
    # 3단계 >> i가 같을경우 동일한 인덱스를 두번 저장하는 문제 index()함수는 같은 내용이있으면 가장 앞의 인덱스를 출력
    iscomma = 0
    removecnt = 0
    for i in range(len(templist)):
        if templist[i - removecnt] == '.':
            if iscomma == 1:
                templist.pop(templist.index(templist[i - removecnt]))
                removecnt = removecnt + 1
            else:
                templist[i - removecnt] = '='
                iscomma = 1
        else:
            iscomma = 0
    for i in range(len(templist)):
        if templist[i] == '=':
            templist[i] = '.'
    # 4단계
    while templist and templist[0] == '.':
        templist.pop(0)
    while templist and templist[-1] == '.':
        templist.pop()
    # 5단계
    if not templist:
        templist.append('a')
    # 6단계
    if len(templist) >= 16:
        templist = templist[0:15]
    while templist and templist[-1] == '.':
        templist.pop()
    # 7단계
    if len(templist) <= 2:
        while len(templist) < 3:
            templist.append(templist[-1])
    answer = ''.join(templist)

    return answer