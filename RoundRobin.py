process=eval(input("how many processes you want to run? "))
quantum=eval(input("Quantum time for each process is?"))
IO=input("which processes will go for I/O even or odd?")
IOtime=eval(input("after running for how much time will  the input output bound processes go fo I/O?"))
IOwaiting=eval(input("what will be thewaiting time for I/O processes"))
name=[]
arrivaltime=[]
bursttime=[]
starttime=[]
finishtime=[]
returntime=[]
returnindex=[]
count=0
count1=0
IOtimearr=[]
for i in range(process):
    IOtimearr.append(IOtime)

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


if IO=='even':
    starttime.append(arrivaltime[0])
    if bursttime[0]>quantum:
        bursttime[0]=bursttime[0]-quantum
        name.append(name[0])
        bursttime.append(bursttime[0])
        finishtime.append(arrivaltime[0]+quantum)
        IOtimearr.append(IOtime)
        process=process+1
    else:
        finishtime.append(arrivaltime[0]+bursttime[0])
        print("The process ", name[0], " started at ", arrivaltime[0], " and ended at ", arrivaltime[0] + bursttime[0])
    i=0
    while i<process:
        i=i+1

        if returntime:
            for j in range(count1):
                if finishtime[i-1]>=returntime[j]:
                    name.append(name[returnindex[j]])
                    bursttime.append(bursttime[returnindex[j]])
                    IOtimearr.append(IOtime)
                    count=count-1
                    returntime[j]=[]
                    returnindex[j]=[]


        count1=count



        if i==0 or i%2==0:
            if bursttime[i]>quantum:
                starttime.append(finishtime[i-1])
                bursttime[i] = bursttime[i] - quantum
                name.append(name[i])
                bursttime.append(bursttime[i])
                IOtimearr.append(IOtime)
                finishtime.append(finishtime[i-1]+quantum)
                process=process+1
            else:
                starttime.append(finishtime[i-1])
                finishtime.append(finishtime[i-1] + bursttime[i] )
                print("The process ", name[i], " started at ", starttime[i], " and ended at ",
                      finishtime[i])

        else:
            if IOtimearr[i]>quantum and bursttime[i]>quantum:
                starttime.append(finishtime[i-1])
                bursttime[i ] = bursttime[i ] - quantum
                name.append(name[i])
                bursttime.append(bursttime[i])
                IOtimearr.append(IOtime)
                finishtime.append(finishtime[i-1] + quantum)
                process = process + 1
                IOtimearr[i]=IOtimearr[i]-quantum

            elif IOtimearr[i]>bursttime[i] and bursttime[i]<quantum:
                starttime.append(finishtime[i-1])
                finishtime.append(finishtime[i-1] + bursttime[i])
                print("The process ", name[i], " started at ", starttime[i], " and ended at ",
                      finishtime[i])

            elif IOtimearr[i]<bursttime[i] and IOtimearr[i]<quantum:
                starttime.append(finishtime[i-1])
                finishtime.append(finishtime[i-1] + IOtimearr[i])
                returntime.append(finishtime[i]+IOwaiting)
                returnindex.append(i)
                count=count+1
                count1=count













elif IO=='odd':
    starttime.append(arrivaltime[0])


    if IOtimearr[0] > quantum and bursttime[0] > quantum:
        starttime.append(arrivaltime[0])
        bursttime[0] = bursttime[0] - quantum
        name.append(name[0])
        IOtimearr.append(IOtime)
        bursttime.append(bursttime[0])
        finishtime.append(arrivaltime[0] + quantum)
        IOtimearr[0] = IOtimearr[0] - quantum

    elif IOtimearr[0] > bursttime[0] and bursttime[0] < quantum:
        starttime.append(arrivaltime[0])
        finishtime.append(arrivaltime[0] + bursttime[i])
        print("The process ", name[0], " started at ", starttime[0], " and ended at ",
              finishtime[0])

    elif IOtime[0] < bursttime[i] and IOtime[0] < quantum:
        starttime.append(arrivaltime[0])
        finishtime.append(arrivaltime[0] + IOtime[0])
        returntime.append(IOtime[0] + IOwaiting)
        returnindex.append(0)


    while i<process:
        i=i+1

        if returntime:
            for j in range(count1):
                if finishtime[i-1]>=returntime[j]:
                    name.append(name[returnindex[j]])
                    IOtimearr.append(IOtime)
                    bursttime.append(bursttime[returnindex[j]])
                    count=count-1
                    returntime[j]=[]
                    returnindex[j]=[]


        count1=count



        if i==0 or i%2==0:
            if IOtime[i]>quantum and bursttime[i]>quantum:
                starttime.append(finishtime[i-1])
                bursttime[i ] = bursttime[i ] - quantum
                name.append(name[i])
                IOtimearr.append(IOtime)
                bursttime.append(bursttime[i])
                finishtime.append(finishtime[i-1] + quantum)
                process = process + 1
                IOtime[i]=IOtime[i]-quantum

            elif IOtime[i]>bursttime[i] and bursttime[i]<quantum:
                starttime.append(finishtime[i-1])
                finishtime.append(finishtime[i-1] + bursttime[i])
                print("The process ", name[i], " started at ", starttime[i], " and ended at ",
                      finishtime[i])

            elif IOtime[i]<bursttime[i] and IOtime[i]<quantum:
                starttime.append(finishtime[i-1])
                finishtime.append(finishtime[i-1] + IOtime[i])
                returntime.append(finishtime[i]+IOwaiting)
                returnindex.append(i)
                count=count+1
                count1=count


        else:
            if bursttime[i]>quantum:
                starttime.append(finishtime[i-1])
                bursttime[i] = bursttime[i] - quantum
                name.append(name[i])
                IOtimearr.append(IOtime)
                bursttime.append(bursttime[i])
                finishtime.append(finishtime[i-1]+quantum)
                process=process+1
            else:
                starttime.append(finishtime[i-1])
                finishtime.append(finishtime[i-1] + bursttime[i] )
                print("The process ", name[i], " started at ", starttime[i], " and ended at ",
                      finishtime[i])



else:
    print("Select either even or odd")
