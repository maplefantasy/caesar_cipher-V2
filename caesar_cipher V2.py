import random
ts1=[]
def ptc(text,n): #明文轉密文
    tr=[]
    ts=list(text) #文字轉清單
    i = len(ts)
    o = i//n #商數
    p = i%n #餘數
    a,b,c,d=0,0,0,0
    while b<n:
        ran = random.randint(1,127)
        tr.append(ran)
        while c < o:#整數拆分
            asc1=ts[d]
            asc1=chr(ord(asc1)+ran)
            ts1.append(asc1)
            c=c+1
            d=d+1
        b=b+1
        c=0
    
    if a<p:
        ran = random.randint(1,127)
        tr.append(ran)
        z=o*n
        while a<p:
            asc1=ts[z+a]
            asc1=chr(ord(asc1)+ran)
            ts1.append(asc1)
            a=a+1

    tr = [str(x) for x in tr]
    Str = "".join(ts1)
    tr = " ".join(tr)
    print(f"密文:[[{Str}]]")
    print(f'拆分值{n-1},密文碼{tr}')


def ctp(text,n,nlist): #密文轉明文
    ts=list(text)
    i=len(ts)
    l=len(nlist)
    if 1 < l:
        o = i//n #商數
        p = i%n #餘數
        a,b,c,d=0,0,0,0
        while b < n:
            num1 = int(nlist[b])
            while c < o:
                asc1=ts[d]
                asc1=chr(ord(asc1)-num1)
                ts1.append(asc1)
                c=c+1
                d=d+1
            b=b+1
            c=0

        if a<p:
            num1 = int(nlist[l-1])
            z=o*n
            while a<p:
                asc1=ts[z+a]
                asc1=chr(ord(asc1)-num1)
                ts1.append(asc1)
                a=a+1


    if n == 1:
        a=0
        while a < i:
            asc1=ts[a]
            num1 = int(nlist[0])
            asc1=chr(ord(asc1)-num1)
            ts1.append(asc1)
            a=a+1

    Str = "".join(ts1)
    print(f"明文:{Str}")


while True:

    while True:

        Grammarsettings = int(input("選擇輸入明文或密文(明文=0密文=1):"))
        if -1 < Grammarsettings < 2:
            break
        else:
            print("範圍外,請重新輸入")
            continue
    if Grammarsettings == 0:
        while True:
            plaintext = input("輸入明文:")
            num = int(input("輸入拆分值0~5(int):"))
            if -1 < num < 6:
                ptc(plaintext,num+1)
                break
            else:
                print("範圍外,請重新輸入")
    if Grammarsettings == 1:
        while True:
            plaintext = input("輸入密文:")
            nu = int(input("輸入拆分值:"))
            input_string = input("輸入密文碼(若有多個數字請以空格分開):")
            list_string = input_string.split()
            num = len(list_string)
            if 0 < num < 7:
                ctp(plaintext,nu+1,list_string)
                break
            else:
                print("範圍外,請重新輸入")
    
    ts1=[]
    list_string=[]