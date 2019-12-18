f = open('data.txt', 'r')
data = f.read().replace('\n', '#')
f.close()
dataArr = data.split('#')
#print(dataArr)

class Staff:
    def __init__(self, ID='', name='', position='', salary=0):    
        self.ID = ID
        self.name = name
        self.position = position
        self.salary = salary 
    
    def newStaff(self):
        newID = input('input staff ID[SXXXX]: ')
        self.ID = newID
        newName = input('input staff Name[0...20]: ')
        self.name = newName
        newPosition = input('input staff Position[Staff|Officer|Manager]: ')
        self.position = newPosition
        newSalary = input('input staff Salary: ')
        self.salary = newSalary



staff1 = Staff(dataArr[0], dataArr[1], dataArr[2], dataArr[3])
staff2 = Staff(dataArr[4], dataArr[5], dataArr[6], dataArr[7])
staff3 = Staff(dataArr[8], dataArr[9], dataArr[10], dataArr[11])
staff4 = Staff(dataArr[12], dataArr[13], dataArr[14], dataArr[15])


staffs: Staff()
staffs = [staff1, staff2, staff3, staff4]
staffIDs = [staff1.ID, staff2.ID, staff3.ID, staff4.ID]


def printStaffs():
    print('|' + 'ID' + '|' + 'name'  + '|' + 'position' + '|' + 'salary')
    for i in range(len(staffs)):
        print('|' + staffs[i].ID  + '|' + staffs[i].name  + '|' + staffs[i].position + '|' + staffs[i].salary)

exitprogram = False
while exitprogram == False:

    printStaffs()

    print('1. New Staff')
    print('2. Delete Staff')
    print('3. View Summary Data')
    print('4. Save and Exit')


    inputChoice = input('Enter an input: ')
    if inputChoice == '1':
        newPerson = Staff()
        newPerson.newStaff()
        staffs.append(newPerson)
        staffIDs.append(newPerson.ID)
    elif inputChoice == '2':
        userID = input('ID: ')
        if userID in staffIDs:
            pos = staffIDs.index(userID)
            del staffs[pos]
    elif inputChoice == '4':
        exitprogram = True
    else:
        print('Error')

