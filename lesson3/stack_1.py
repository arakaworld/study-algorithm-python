MAX = 5
stack = [MAX] * 5

# データを出し入れする位置を管理する変数（スタックポインタ）
sp = 0


def push(d):
    global sp
    if sp < MAX:
        stack[sp] = d
        sp = sp + 1
        print("データ", d, "を追加しました")
    else:
        print("これ以上データを入れられません")


def pop():
    global sp
    if sp > 0:
        sp = sp - 1
        return stack[sp]
    else:
        print("取り出すデータが存在しません")
        return None


for i in range(6):
    push(i)

for i in range(6):
    d = pop()
    print("取り出したデータ", d)
