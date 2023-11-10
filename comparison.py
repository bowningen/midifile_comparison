import sys
import os

#とにかくtxtファイルから取り出してきて単純に先頭から一個ずつ比較するだけです

#ってか非常にめんどくさいのでできるだけ繰り返し処理ですっきりしたプログラム...は作りません
#もうほぼ全部書きます

path = os.getcwd()
print (path)

#midiファイルの指定
midFile0 = "C:\\Users\\Annie\\Documents\\VScode\\HK_MD\\OS6.txt"
midFile1 = "C:\\Users\\Annie\\Documents\\VScode\\HK_MD\\t61.txt"
midFile2 = "C:\\Users\\Annie\\Documents\\VScode\\HK_MD\\t62.txt"
midFile3 = "C:\\Users\\Annie\\Documents\\VScode\\HK_MD\\t63.txt"
midFile4 = "C:\\Users\\Annie\\Documents\\VScode\\HK_MD\\t64.txt"

#midFile0 = "C:\\Users\\Annie\\Documents\\VScode\\HK_MD\\P1.txt"
#midFile1 = "C:\\Users\\Annie\\Documents\\VScode\\HK_MD\\p11.txt"
#midFile2 = "C:\\Users\\Annie\\Documents\\VScode\\HK_MD\\p12.txt"
#midFile3 = "C:\\Users\\Annie\\Documents\\VScode\\HK_MD\\p13.txt"
#midFile4 = "C:\\Users\\Annie\\Documents\\VScode\\HK_MD\\p14.txt"

midF = [midFile0,midFile1,midFile2,midFile3,midFile4]
dat0 = ""
dat1 = ""
dat2 = ""
dat3 = ""
dat4 = ""
dat0H = []
dat1H = []
dat2H = []
dat3H = []
dat4H = []
datH = [dat0H,dat1H,dat2H,dat3H,dat4H]
#読む
with open(midF[0],'r') as f:
    dat0 = f.read()
    dat0 = dat0.replace("'","").replace("[","").replace("]","").replace("(","").replace(")","").replace(" ","")
    dat0H = dat0.split(",")
with open(midF[1],'r') as f:
    dat1 = f.read()
    dat1 = dat1.replace("'","").replace("[","").replace("]","").replace("(","").replace(")","").replace(" ","")
    dat1H = dat1.split(",")
with open(midF[2],'r') as f:
    dat2 = f.read()
    dat2 = dat2.replace("'","").replace("[","").replace("]","").replace("(","").replace(")","").replace(" ","")   
    dat2H = dat2.split(",")
with open(midF[3],'r') as f:
    dat3 = f.read()
    dat3 = dat3.replace("'","").replace("[","").replace("]","").replace("(","").replace(")","").replace(" ","")    
    dat3H = dat3.split(",")
with open(midF[4],'r') as f:
    dat4 = f.read()
    dat4 = dat4.replace("'","").replace("[","").replace("]","").replace("(","").replace(")","").replace(" ","")   
    dat4H = dat4.split(",")
datF = [dat0,dat1,dat2,dat3,dat4]
datHS = str(datF)
try:
    #開いて書き込みます
    with open("C:\\Users\\Annie\\Documents\\VScode\\HK_MD\\pyread.txt", 'w') as f:
        f.write(datHS)        
    print("I/O OK.")
#例外処理
except Exception as e:
    print(f'[ERROR] {type(e)}:{datHS(e)}')

#全てのノーツ数(元データ)
Anote = 0
#現在処理中のノート
Nnote = 0
#一致数1~4
Cnote1 = 0
Cnote2 = 0
Cnote3 = 0
Cnote4 = 0
#調べるLastTime
Lnote = len(dat0H)
Anote = Lnote
#それに合わせて他のデータのデータ長の調整
LN1 = len(dat1H)
LN2 = len(dat2H)
LN3 = len(dat3H)
LN4 = len(dat4H)
if(LN1 < Lnote):
    while (LN1 != Lnote):
        dat1H.append("0")
        LN1 = len(dat1H)
if(LN2 < Lnote):
    while (LN2 != Lnote):
        dat2H.append("0")        
        LN2 = len(dat2H)
if(LN3 < Lnote):
    while (LN3 != Lnote):
        dat3H.append("0")
        LN3 = len(dat3H)
if(LN4 < Lnote):
    while (LN4 != Lnote):
        dat4H.append("0")    
        LN4 = len(dat4H)

#メイン処理
p = 0

#合計で何個あったかの記録用
A1 = 0
A2 = 0
A3 = 0
A4 = 0

#あるTimeにおける処理中のノーツが何番目なのかの変数
TN = 0

while p < Lnote:
    NH0 = "".join(str(dat0H[Nnote]))
    NHL0 = NH0.split(":")
    NHL0.sort()
    L0 = len(NHL0)
    NH1 = "".join(str(dat1H[Nnote]))
    NHL1 = NH1.split(":")
    NHL1.sort()
    L1 = len(NHL1)
    NH2 = "".join(str(dat2H[Nnote]))
    NHL2 = NH2.split(":")
    NHL2.sort()
    L2 = len(NHL2)
    NH3 = "".join(str(dat3H[Nnote]))
    NHL3 = NH3.split(":")
    NHL3.sort()
    L3 = len(NHL3)
    NH4 = "".join(str(dat4H[Nnote]))
    NHL4 = NH4.split(":")
    NHL4.sort()
    L4 = len(NHL4)


    while TN < L0:
        a = NHL0[TN]

        kp = 0
        for i in NHL1:
            if (a == NHL1[kp]):
                Cnote1 += 1
            A1 += 1
        
        kp = 0
        for i in NHL2:
            if (a == NHL2[kp]):
                Cnote2 += 1
            A2 += 1
        
        kp = 0
        for i in NHL3:
            if (a == NHL3[kp]):
                Cnote3 += 1
            A3 += 1
        
        kp = 0
        for i in NHL4:
            if (a == NHL4[kp]):
                Cnote4 += 1
            A4 += 1
        
        TN += 1
    p += 1
    TN = 0
    Nnote += 1
print("Count =")
print("1 = " + str(A1) + ":" + str(Cnote1))
print("2 = " + str(A2) + ":" + str(Cnote2))
print("3 = " + str(A3) + ":" + str(Cnote3))
print("4 = " + str(A4) + ":" + str(Cnote4))
r1 = Cnote1 / A1
r2 = Cnote2 / A2
r3 = Cnote3 / A3
r4 = Cnote4 / A4
print()
print("Result =")
print("1=" + str(r1))
print("2=" + str(r2))
print("3=" + str(r3))
print("4=" + str(r4))