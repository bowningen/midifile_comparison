import os
import sys
import re
import mido

#カレントディレクトリの取得
path = os.getcwd()
print (path)


#読み込み
print("midifile_comparisoner v0.20")
print("Prease enter filePath:" , end="")
filepath = input()
print("")
print("Seaching " + filepath + "...")
if (os.path.isfile(filepath) == True):
    midFile = filepath
    print("found.")
else:
    print("Error. Not found.")
    input()
    sys.exit(1)
print("")

#付けたい名前を入れるのね
print("Prease enter creating txt Name")
midName = input()

#mifiファイルネーム(略称)
AmidN = [midName]
#midiファイルパス
AmidNF = [midFile]

midiC = 0
midi = mido.MidiFile(AmidNF[midiC])
#stringに変換
t = str(midi)
#改行コードごとに分けた配列化
ts = t.splitlines()

#textに書き込みますね
#textのパス
#textPath = path + "\\pyRead.txt"
textPath = AmidN[midiC] + ".txt"
#配列を結合してstring化...？(tと同じ希ガス)
tss = "\n".join(ts)
try:
    #開いて書き込みます
    with open(textPath, 'w',encoding="utf-8") as f:
        f.write(tss)

#例外処理
except Exception as e:
    print(f'[ERROR] {type(e)}:{str(e)}')

#必要な要素の切り出し
MainStr = tss.replace('　', '').replace('\r','').replace('\n','').replace('\r\n','').replace('MetaMessage','').replace('(','').replace(')','').replace('[','').replace(']','').replace('channel=0','').replace('Message','').replace(',','').replace('\'','').replace('\"','')
#今回は音の大きさは考えない(考えてるときりがないしおかしくなることは必然なので)

#切り分けミスった時用の関数
def ReSplit(count):
    print("Error. Recalculating...")
    MainStr2 = MainStr[noteOnList[0]:EDT[0]]
    try:
        with open(textPath, 'w',encoding="utf-8") as f:
            f.write(MainStr2)    
    except Exception as e:
        print(f'[ERROR] {type(e)}:{MainStr2(e)}')
    noteOnList = [m.start() for m in re.finditer('note_on', MainStr2)]
    noteOffList = [m.start() for m in re.finditer('note_off', MainStr2)]
    OnOffList = noteOnList + noteOffList
    OnOffList.sort()
    l = count*10 + 0
    count += 1
    if(OnOffList[0] < OnOffList[l]):
        p = MainStr2.find(("track_name"))
        s = OnOffList[1] - p
        nL = [m.start() for m in re.finditer('    ', MainStr2)]
        nL2 = []
        nL2.append(nL[0])
        for item in nL:
            if (item > OnOffList[1]):
                nL2.append(item)
            elif(item == OnOffList[1]):
                nL2.append(item)
        q = 0
        noneList = []
        noneList.append(nL[0])
        for item in nL2:
            if (q != 0): 
                noneList.append (nL2[q])
            q += 1
    else:
        noneList = [m.start() for m in re.finditer('    ', MainStr2)]
        i = 0
        DList = []
        for item in OnOffList:
            DList.append(str(OnOffList[i]) + "," + str(noneList[i]))
            i  += 1
        DListStr = "\n".join(DList)
        try:
            with open(textPath, 'w',encoding="utf-8") as f:
                f.write(DListStr)
        except Exception as e:
            print(f'[ERROR] {type(e)}:{DListStr(e)}')
        i = 0
        Mainlist = []
        for item in DList:
            Mainlist.append(MainStr2[OnOffList[i]:noneList[i]])
            i += 1
        p = str(Mainlist)
        try:
            with open(textPath, 'w',encoding="utf-8") as f:
                f.write(p)
        except Exception as e:
            print(f'[ERROR] {type(e)}:{p(e)}')
            
#note_onの位置
noteOnList = [m.start() for m in re.finditer('note_on', MainStr)]
#print(noteOnList)
#note_offの位置
noteOffList = [m.start() for m in re.finditer('note_off', MainStr)]
#print(noteOffList)

#EDTの位置
if("marker" in MainStr):
    #別の形式だとmarkerの位置にしないとおかしくなるぽい
    EDT = [m.start() for m in re.finditer('marker', MainStr)]
    #2つ以上ある場合は最後のものを使用(しないとおかしくなるので)
    if (len(EDT) != 1):
        k = EDT[-1]
        EDT.clear()
        EDT.append(k)
    #print(EDT)
else:
    EDT = [m.start() for m in re.finditer('end_of_track', MainStr)]
    #2つ以上ある場合は最後のものを使用(しないとおかしくなるので)
    if (len(EDT) != 1):
        k = EDT[-1]
        EDT.clear()
        EDT.append(k)
    #print(EDT)

MainStr2 = MainStr[noteOnList[0]:EDT[0]]
try:
    #開いて書き込みます
    with open(textPath, 'w',encoding="utf-8") as f:
        f.write(MainStr2)        

#例外処理
except Exception as e:
    print(f'[ERROR] {type(e)}:{MainStr2(e)}')
#note_onの位置(やりなおし)
noteOnList = [m.start() for m in re.finditer('note_on', MainStr2)]
#note_offの位置(やりなおし)
noteOffList = [m.start() for m in re.finditer('note_off', MainStr2)]
#合体
OnOffList = noteOnList + noteOffList
#整列
OnOffList.sort()

#また別形式用の分岐
#ここの60って値は適当に調整しなさい(投げやり)
if(OnOffList[0] < OnOffList[60]):
    p = MainStr2.find(("track_name"))
    s = OnOffList[1] - p
    #区別しやすい空白の位置
    nL = [m.start() for m in re.finditer('    ', MainStr2)]
    nL2 = []
    nL2.append(nL[0])
    for item in nL:
        if (item > OnOffList[1]):
            nL2.append(item)
        elif(item == OnOffList[1]):
            nL2.append(item)

    q = 0
    noneList = []
    noneList.append(nL[0])

    for item in nL2:
        if (q != 0): 
            noneList.append (nL2[q])
        q += 1
else:
    #区別しやすい空白の位置
    noneList = [m.start() for m in re.finditer('    ', MainStr2)]

i = 0
DList = []
for item in OnOffList:
    DList.append(str(OnOffList[i]) + "," + str(noneList[i]))
    i  += 1
#print(DList)    

DListStr = "\n".join(DList)
try:
    #開いて書き込みます
    with open(textPath, 'w',encoding="utf-8") as f:
        f.write(DListStr)

#例外処理
except Exception as e:
    print(f'[ERROR] {type(e)}:{DListStr(e)}')

#とりあえずここまでで各音のON/OFFの処理部分だけを切り出せましたよーと
#で、その切り出した部分をさらに配列化
i = 0
Mainlist = []
for item in DList:
    Mainlist.append(MainStr2[OnOffList[i]:noneList[i]])
    i += 1
p = str(Mainlist)
try:
    #開いて書き込みます
    with open(textPath, 'w',encoding="utf-8") as f:
        f.write(p)        

#例外処理
except Exception as e:
    print(f'[ERROR] {type(e)}:{p(e)}')

#さらに簡略化していらないところを切る
i = 0
listLast = []
for item in Mainlist:
    rK = 0
    reb = 0
    while (rK == 0):
        rK = 1
        str2 = Mainlist[i]
        str2 = str2.replace('note_on  ', 'on.').replace('note_off  ', 'off.')
        #note=の位置
        vel = [m.start() for m in re.finditer('velocity=', str2)]
        #timeの位置
        time = [m.start() for m in re.finditer('time=', str2)]
        #例外処理
        if(len(vel) != 1):
            ReSplit(reb)
            rK = 0
            break
        else:
            strL = list(str2)
            noteL = vel[0]
            timeL = time[0]
            #velocityは考えないので削除
            del strL[noteL:timeL]
            #さらに無駄なところの削除
            strR = ''.join(strL)
            #timeの相対時間から絶対時間への変換の為目印を置きます
            strLast = strR.replace('note=', ';').replace(' time=', ':')
            listLast.append(strLast)
            reb += 1
            i += 1

Astr = (','.join(listLast))
Astr = Astr + ","
try:
    #開いて書き込みます
    with open(textPath, 'w',encoding="utf-8") as f:
        f.write(Astr)

#例外処理
except Exception as e:
    print(f'[ERROR] {type(e)}:{Astr(e)}')

#timeを相対時間から絶対時間へ変換するやつ

#:の位置
colon = [m.start() for m in re.finditer(':', Astr)]
#,の位置
camma = [m.start() for m in re.finditer(',', Astr)]
#Timeのみの切り出し
deltaTime = []
realTime = []
k = 0
for i in colon:
    kp = colon[k] + 1
    r = Astr[kp:camma[k]]
    deltaTime.append(r)
    k += 1
#ここで変換かけます
k = 0
kTime = 0
IDeltaTime= [int(s) for s in deltaTime]
for i in deltaTime:
    realTime.append(IDeltaTime[k] + kTime)
    kTime = kTime + IDeltaTime[k]
    k += 1


#Astrにおけるtimeの置き換え
t = 0
for i in listLast:
    #:の位置
    colon = [m.start() for m in re.finditer(':', listLast[t])]
    #置き換え
    RT = realTime[t]
    OT = listLast[t]
    CL = colon[0]
    CLI = int(CL)
    LT = OT[0:CLI]
    RTS = str(RT)
    LT2 = LT + ":" + RTS
    listLast[t] = LT2
    t += 1

#絶対時間で一つの配列に突っ込みます
t = 0
dotL = []
#各キーごとになっているかどうかの確認
YNCheck = []
#現在時間(初期値は0)
nTime = 0
LastL = 0
s = 0
count = 0
while (s == 0):
    YNCheck.append (0)
    #print(t)
    nowStr = listLast[t]
    #colonの位置
    colonL = [m.start() for m in re.finditer(':', listLast[t])]
    CL2 = colonL[0]
    Len = len(nowStr)
    CLI2 = int(CL2)
    CLIL = CLI2 + 1
    LTL = nowStr[CLIL:Len]
    #LTLBが絶対時間なのでこれに対応するとこにつっこみます
    LTLB = int(LTL)
    #次にon/offの取得
    if ("on" in nowStr):
        YN = 1
    elif ("off" in nowStr):
        YN = 0
    else:
        print("This format is not supported.")
        input()
        sys.exit(1)

    #YN = 1ならkey_on YN = 0
    #それからkeyの取得
    #semiの位置
    dotL = [m.start() for m in re.finditer(';', listLast[t])]
    dotL2 = dotL[0] + 1
    DTL = nowStr[dotL2:CLI2]
    #DTLがkeyになります
    #現在時間の変更の有無
    if (count != 0):
        if (LTLB != LastL):
            nTime += 1

    #ここからがメイン
    if (nTime == LTLB):
        kd = YNCheck[nTime]
        fp = nTime - 1
        kdp = YNCheck[fp]
        if (YN == 1):
            if (YNCheck[fp] == 0):
                YNCheck[nTime] = DTL
            else:
                YNCheck[nTime] = YNCheck[fp] + ":" +  DTL
                LastL = LTLB
        else:
            if (str(DTL) in str(YNCheck[fp])):
                kdpa = kdp.split(':')
                u = 0
                for i in kdpa:
                    if (kdpa[u] == DTL):
                        st = len(kdpa)
                        del kdpa[u]
                        u += 1
                    else:
                        u += 1
                kds = ":".join(kdpa)
                if (kds == ""):
                    kds = 0
                YNCheck[nTime] = kds
                    
        #break条件の確認
        if(t == len(listLast) - 1):
            s = 1
        
        LastL = LTLB
        #処理してる配列の位置を+1します
        t += 1
    else:
        if (count != 0):
            fp = nTime - 1
            YNCheck[nTime] = YNCheck[fp]
        else:
            YNCheck[nTime] = 0
        
    count += 1

nb = 0
RStr = []
YNL = len(YNCheck)
for i in YNCheck:
    RStr.clear()
    #重複要素の削除
    G = str(YNCheck[nb]).split(":")
    ksd = 0
    for r in G:
        if G[ksd] not in RStr:
            RStr.append(G[ksd])
        ksd += 1
    fdt = ':'.join(RStr)
    YNCheck[nb] = fdt
    nb += 1
RStr2 = str(YNCheck)
try:
    #開いて書き込みます
    with open(textPath, 'w') as f:
        f.write(RStr2)        

#例外処理
except Exception as e:
    print(f'[ERROR] {type(e)}:{RStr2(e)}')

midiC += 1
print("")
print("Processing completed.")