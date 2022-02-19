for i in range(1, 101):
    # 対象の値の半分の値より大きな数では割り切れないことが明白(そりゃそうか…)
    h = i // 2 # 切り捨て
    f = True
    for j in range(2, h + 1):
        if i % j == 0:
            f = False
            break
    if f == True:
        print(i, end=",")