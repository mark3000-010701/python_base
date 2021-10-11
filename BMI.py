chieucao, cannang = map(int, input().split())
BMI = cannang / (chieucao * chieucao)
'''BMI < 16: Gầy cấp độ III
16 <= BMI < 17:  Gầy cấp độ II
17<= BMI < 18.5: Gầy cấp độ I
18.5 <= BMI < 25: Bình thường
25 <= BMI < 30: Thừa cân
30 <= BMI < 35 : Béo phì cấp độ I
35 <= BMI < 40: Béo phì cấp độ II
BMI > 40: Béo phì cấp độ III'''
if BMI < 16:
    print("gầy cấp độ III")
elif 16 <= BMI < 17:
    print("gầy cấp độ II")
elif 17 <= BMI < 18.5:
    print("gầu cấp độ I")
elif 18.5 <= BMI < 25:
    print("bình thường")
elif 25 <= BMI < 30:
    print("Thừa cân")
elif 30 <= BMI < 35:
    print("báo phí cấp độ I")
elif 35 <= BMI < 40:
    print("Beeos phì cấp II")
else:
    print("Béo phì cấp III")
