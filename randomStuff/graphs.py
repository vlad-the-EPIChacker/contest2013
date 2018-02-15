boolTasks={}
boolTasks1={}
prnt=[]

def rgraphs(tasks):
    global boolTasks
    global prnt
    end=True
    for i in boolTasks.values():
        if not i:
            end=False
    if end:
        return True
    for i in tasks:
        if boolTasks[i[0]]:
            boolTasks[i[1]] = True
            if rgraphs([ii for ii in tasks if ii!=i]):
                prnt.append("Complete Task " + str(i[1]))
                return True
            boolTasks[i[1]]=False
    return False


def graphs(tasks):
    global boolTasks1
    global boolTasks
    global prnt
    tasks1=tasks
    boolTasks={}
    prnt=[]
    for i in tasks:
        boolTasks[i[1]]=False
    for i in tasks:
        if i[0] not in boolTasks.keys():
            print "Complete Task", i[0]
            boolTasks[i[0]]=True
    if not rgraphs(tasks1):
        print "Impossible to Complete\n"
    else:
        for i in range(len(prnt)-1,-1,-1):
            print prnt[i]
        print "Completed\n"

graphs([('A','B'),('B','C')])
graphs([('A','B'),('B','C'),('C','A')])
graphs([])
graphs([('A','B'),('C','D')])
graphs([('C','A'),('C','B'),('D','C'),('E','C')])