import random
min = 1
max = 100
target = random.randint(min,max)
count = 0

print("===========猜數字遊戲===========\n\n")
while True:
    key_in = int(input(f"猜數字的範圍：{min}~{max}:"))
    count += 1

    if key_in >= min and key_in <= max:
        if key_in == target:
            print(f"賓果！你猜對了！答案是{key_in}")
            print(f"您一共猜了{count}次")
            break
        elif key_in > target:
            print("猜錯了,再小一點")
            max = key_in -1
            print(f"您已經猜了{count}次")
        elif key_in < target:
            print("猜錯了,再大一點")
            min = key_in +1
            print(f"您已經猜了{count}次")
    else:
        print("超出範圍")
print("GAME OVER!")