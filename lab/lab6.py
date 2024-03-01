class Node: #create Node
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class UnorderedList:
    def __init__(self): #initialize
        self.head = None

    def add(self,item): #add node to list
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def removeN(self):
        temp = self.head #hold temp value

        slow, fast = temp, self.head #initialize 2 pointers

        while fast:
            fast = fast.next.next #move fast pointer 2 pace at a time
            slow = slow.next #move slow pointer 1 pace at the time
            if fast == None: #when fast pointer reach Null
                slow.next = slow.next.next #point the next node of slow pointer to the other next node
    def printList(self): #print list
        temp = self.head
        while (temp):
            print(temp.data, " ", end='')
            temp = temp.next
        print("")

mylist = UnorderedList()
mylist.add(71)
mylist.add(40)
mylist.add(21)
mylist.add(33)
mylist.add(11)
mylist.add(50)


mylist.printList()
mylist.removeN()
mylist.printList()
'''
#test 1: input is Null
test1 = UnorderedList()
test1.add()
test1.add()
test1.add()
test1.add()
test1.add()
test1.printList()
test1.removeN()
test1.printList()

#test 2: input has length of 1
test2 = UnorderedList()
test2.add(1)
test2.printList()
test2.removeN()
test2.printList()

#test 3: intput is string
test3 = UnorderedList()
test3.add(a)
test3.add(d)
test3.add(f)
test3.add(g)
test3.add(s)
test3.printList()
test3.removeN()
test3.printList()

#test 4: inputs have the same values
test4 = UnorderedList()
test4.add(5)
test4.add(5)
test4.add(5)
test4.add(5)
test4.add(5)
test4.printList()
test4.removeN()
test4.printList()'''