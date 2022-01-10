class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return "".join(nodes)

    def add_to_tail(self, node):
        if self.head == None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.set_next(node)

    def remove_from_head(self):
        if self.head == None:
            return None
        temp = self.head
        self.head = self.head.next
        return temp


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node

    def __repr__(self):
        return self.val
        
 
'''linked_list = LinkedList()
linked_list.add_to_tail(Node('8'))
linked_list.add_to_tail(Node('7'))
linked_list.add_to_tail(Node('8'))
print("ll:", linked_list)
first = linked_list.remove_from_head()
print("removed:", first, type(first))
print("ll:", linked_list)'''

#input number 1 and 2
num_1 = input('Enter Number: ')
num_2 = input('Enter Number: ')

#lit number 1
L_1 = []
for i in num_1:
	L_1.append(int(i))
print('num_1:  ', num_1)
print('L_1: ', L_1)

#list number 2
L_2 = []
for i in num_2:
	L_2.append(int(i))
print('num_2: ', num_2)
print('L_2: ', L_2)

#add tow long numbers
r = [] #save result
n_r = 0 #save The rest of the combination

x = len(L_1)
y = len(L_2)
if x > y:
	print(x, y)
	l = x - y
	for i in range(l):
		L_2.insert(0, 0)
	print(f'List_2: {L_2}')
	
if y > x:
	print(x, y)
	l = y - x
	for i in range(l):
		L_1.insert(0, 0)
	print(f'List_1: {L_1}')
	


list1 = LinkedList()
for i in L_1:
	list1.add_to_tail(Node(str(i)))
	
print('linked list one: ', list1)


list2 = LinkedList()
for i in L_2:
	list2.add_to_tail(Node(str(i)))
	
print('linked list two: ', list2)

c_f = 0
c_l = len(list2.__repr__())
i = len(list1.__repr__()) - 1


#========== add numbers ==========#
while i >= 0:
	c_f += 1
	add = int(list1.__repr__()[i]) + int(list2.__repr__()[i]) + n_r
	s_add = str(add)
	if c_f == c_l:
		r.insert(0, add)
	elif len(s_add) > 1:
		r.insert(0, int(s_add[1]))
		n_r = int(s_add[0])
	else:
		r.insert(0, add)
	print(f"\nNumber_1 = {L_1[i]}, Number_2 = {L_2[i]}, Rest = {n_r}, Result  Add = {add}, Index Add= {i}")
	i -= 1	

s = ""
for i in r:
	s += str(i)

n = int(s)
print(f"result: {n}")

list3 = LinkedList()
for i in s:
	list3.add_to_tail(Node(str(i)))
	
print('linked list result: ', list3)
