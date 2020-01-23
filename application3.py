f = open('data.txt', 'r')
data = f.read()
f.close()
data2 = data.split('\n')
#print(data2)
dataArr = []
for i in data2:
    dataArr.append(i.split('#'))
#print(dataArr)
numList = [0,1,2,3,4,5,6,7,8,9]

class Staff():
    def __init__(self, ID='', name='', position='', salary=0):
        self.ID = ID
        self.name = name
        self.position = position
        self.salary = salary
    
    def new_staff(self):
        self.ID = input('Input Staff ID[SXXXX]: ')
        self.name = input('Input Staff name[0...20]: ')
        self.position = input('Input Staff position[Staff|Officer|Manager]: ')
        self.salary = input('Input salary: ')

staff1 = Staff(dataArr[0][0], dataArr[0][1], dataArr[0][2], dataArr[0][3])
staff2 = Staff(dataArr[1][0], dataArr[1][1], dataArr[1][2], dataArr[1][3])
staff3 = Staff(dataArr[2][0], dataArr[2][1], dataArr[2][2], dataArr[2][3])
staff4 = Staff(dataArr[3][0], dataArr[3][1], dataArr[3][2], dataArr[3][3])
staff_list = [staff1, staff2, staff3, staff4]

def printStaffs():
    print('|' + 'ID' + '|' + 'name'  + '|' + 'position' + '|' + 'salary' + '|')
    for i in range(len(staff_list)):
        print('|' + staff_list[i].ID  + '|' + staff_list[i].name  + '|' + staff_list[i].position 
                + '|' + staff_list[i].salary + '|')

def newStaff():
    new_person = Staff()
    new_person.new_staff()
    staff_list.append(new_person)
    dataArr.append([new_person.ID, new_person.name, new_person.position, new_person.salary])

def deleteStaff():
    del_ID = input('Input ID: ')
    for i in range(len(staff_list)):
        if del_ID == staff_list[i].ID:
            3
            print('yes')

exitprogram = False
while exitprogram == False:

    printStaffs()

    print('1. New Staff')
    print('2. Delete Staff')
    print('3. View Summary Data')
    print('4. Save and Exit')


    inputChoice = input('Enter an input: ')
    if inputChoice == '1':
        newStaff()
    elif inputChoice == '2':
        deleteStaff()
    elif inputChoice == '4':
        exitprogram = True
    else:
        print('Error')