def solution(w, h):
    answer = 1
    small = 0
    maxnum = 0
    if w >= h:
        small = h
    else:
        small = w

    for i in range(small):
        if (w % (i + 1)) == 0 and (h % (i + 1)) == 0:
            maxnum = i + 1

    answer = w * h - (w + h - maxnum)
    return answer