process=eval(input("how many processes you want to run? "))
name=[]
arrivaltime=[]
bursttime=[]
for i in range(process):
    print("enter the name of " , i+1," process")
    name1=input()
    name.append(name1)
    print("enter the arrival time of " , i+1," process")
    arrive=eval(input())
    arrivaltime.append(arrive)
    print("enter the burst time of " , i+1," process")
    burst=eval(input())
    bursttime.append(burst)

for i in range(process):
    for j in range(0,process-i-1):
        if arrivaltime[j]>arrivaltime[j+1]:
            temp=arrivaltime[j+1]
            arrivaltime[j+1]=arrivaltime[j]
            arrivaltime[j]=temp
            temp1=bursttime[j+1]
            bursttime[j+1]=bursttime[j]
            bursttime[j]=temp1
            temp2=name[j+1]
            name[j+1]=name[j]
            name[j]=temp2




finishtime = []
finishtime.append(arrivaltime[0]+bursttime[0])
print("The process ",name[0]," started at ",arrivaltime[0] , " and ended at ",arrivaltime[0]+bursttime[0])
name[0]=[]
arrivaltime[0]=[]
bursttime[0]=[]


for i in range(process):
    for j in range(process):
        if arrivaltime[j] > finishtime[i]:
            minimum = j
            break

    minvalue = bursttime[0]
    for k in range(minimum):
        if bursttime[k]>minvalue:
            minvalue=bursttime[k].index
    finishtime.append(finishtime[i]+bursttime[minvalue])
    print("The process ", name[minvalue], " started at ",finishtime[i], " and ended at ", finishtime[i+1])
    bursttime[minvalue]=[]
    arrivaltime[minvalue]=[]
    name[minvalue]=[]










