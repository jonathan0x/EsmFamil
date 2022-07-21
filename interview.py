# Esm Famil

n = int(input("تعداد بازیکنان را وارد کنید / Te'dad Bazikonan Ra Vared Konid: "))

chP = input("حرف بازی را به صورت فارسی وارد کنید / Harf Bazi Ra Be Soorat Farsi Vared Konid : ")
chE = input("حرف بازی را به صورت انگلیسی وارد کنید / Harf Bazi Ra Be Soorat Engelisi Vared Konid : ")

score = [0 for i in range(n)]

Esm = []
Shahr = []
Ghaza = []
Rang = []

for i in range(1,n+1):
    print("نوبت نفر " , i , "ام / Nobat Nafar " , i , " om :")
    
    E = input("اسم / Esm : ")
    S = input("شهر / Shahr : ")
    G = input("غذا / Ghaza : ")
    R = input("رنگ / Rang : ")

    Esm.append(E)
    Shahr.append(S)
    Ghaza.append(G)
    Rang.append(R)

for i in range(n):
    if Esm[i][0] != chP and Esm[i][0] != chE: score[i] += 0
    elif Esm.count(Esm[i]) <= 1: score[i] += 10
    else: score[i] += 5
    
    if Shahr[i][0] != chP and Shahr[i][0] != chE: score[i] += 0
    elif Shahr.count(Shahr[i]) <= 1: score[i] += 10
    else: score[i] += 5

    if Ghaza[i][0] != chP and Ghaza[i][0] != chE: score[i] += 0
    elif Ghaza.count(Ghaza[i]) <= 1: score[i] += 10
    else: score[i] += 5

    if Rang[i][0] != chP and Rang[i][0] != chE: score[i] += 0
    elif Rang.count(Rang[i]) <= 1: score[i] += 10
    else: score[i] += 5

for i in range(n):
    print("امتیاز نفر " , i+1 , "ام / Emtiaz Nafar " , i+1 , "om: " , score[i])
