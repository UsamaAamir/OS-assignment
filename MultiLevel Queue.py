print("there are two types of queues foreground and background with foreground having higher priority")
fore=eval(input("how many processes you want in the foreground processes?"))
back=eval(input("how many processes you want in background?"))
fname=[]
farrival=[]
fburst=[]
bname=[]
barrival=[]
bburst=[]
for i in range(fore):
    print("enter the name of " , i+1," process in foreground ")
    name1=input()
    fname.append(name1)
    print("enter the arrival time of " , i+1," process in foreground")
    arrive=eval(input())
    farrival.append(arrive)
    print("enter the burst time of " , i+1," process in foreground")
    burst=eval(input())
    fburst.append(burst)

for i in range(back):
    print("enter the name of " , i+1," process in background")
    name1=input()
    bname.append(name1)
    print("enter the arrival time of " , i+1," process in background")
    arrive=eval(input())
    barrival.append(arrive)
    print("enter the burst time of " , i+1," process in background")
    burst=eval(input())
    bburst.append(burst)


for i in range(fore):
    for j in range(0,fore-i-1):
        if farrival[j]>farrival[j+1]:
            temp=farrival[j+1]
            farrival[j+1]=farrival[j]
            farrival[j]=temp
            temp1=fburst[j+1]
            fburst[j+1]=fburst[j]
            fburst[j]=temp1
            temp2=fname[j+1]
            fname[j+1]=fname[j]
            fname[j]=temp2

ffinish=[]

ffinish.append(farrival[0]+fburst[0])
print("The process ",fname[0]," started at ",farrival[0]," and ended at ",farrival[0]+fburst[0])
for i in range(fore):
    if farrival[i+1]>ffinish[i]:
        ffinish.append(farrival[i+1]+fburst[i+1])
        print("The process ", fname[i+1], " started at ", farrival[i+1], " and ended at ", ffinish[i+1])
        print("Waiting time = ",farrival[i+1]-ffinish[i])

    else:
        ffinish.append(ffinish[i]+fburst[i+1])
        print("The process ", fname[i + 1], " started at ", ffinish[i], " and ended at ", ffinish[i+1])



for i in range(back):
    for j in range(0,back-i-1):
        if barrival[j]>barrival[j+1]:
            temp=barrival[j+1]
            barrival[j+1]=barrival[j]
            barrival[j]=temp
            temp1=bburst[j+1]
            bburst[j+1]=bburst[j]
            bburst[j]=temp1
            temp2=bname[j+1]
            bname[j+1]=bname[j]
            bname[j]=temp2



for i in range(back):
    if barrival[i]>ffinish[fore-1]:
        ffinish.append(barrival[i]+bburst[i])
        print("The process ", bname[i], " started at ", barrival[i], " and ended at ", ffinish[fore+i])
        print("Waiting time = ",barrival[i]-ffinish[fore+i-1])

    else:
        ffinish.append(ffinish[fore+i-1]+bburst[i])
        print("The process ", bname[i], " started at ", ffinish[fore+i-1], " and ended at ", ffinish[fore+i])
