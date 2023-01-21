
score = int(input("请输入你的分数："))
level = ('D' if 0 <= score < 60 else
         'C' if 60 <= score < 70 else
         'B' if 70 <= score < 80 else
         'A' if 80 <= score < 90 else
         'S' if score == 100 else
         print("输入错误，请重新输入\n"))
while score < 0 or score > 100:
    score = int(input("请输入你的分数："))
    level = ('D' if 0 <= score < 60 else
             'C' if 60 <= score < 70 else
             'B' if 70 <= score < 80 else
             'A' if 80 <= score < 90 else
             'S' if score == 100 else
             print("输入错误，请重新输入\n"))
    print(level)
