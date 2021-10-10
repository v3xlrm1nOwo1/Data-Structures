class Stack:
    def __init__(self, full):
        self.full = full
        self.list = list()

    ##list is full
    def Full(self):
        if len(self.list) == self.full:
            return f"List Is Full\nlist: {self.list}\ncount element are list: {self.full}"
        else:
            return f"list is not full, len list is: {len(self.list)}"

    #add element
    def add(self, elem):
        if len(self.list) == self.full:
            return f"List Is Full\nlist: {self.list}\ncount element are list: {self.full}"
        else:
            self.list.append(elem)
            return f"add one element: {elem}, list now: {self.list}"

    #remove one elment from list
    def remove(self):
        if len(self.list) == 0:
            return f"I don't remove from this list: {self.list} "
        else:
            return f"remove this element: {self.list[-1]}, index: {self.list.index(self.list[-1])} from this list: {self.list}", self.list.pop()
            
            
