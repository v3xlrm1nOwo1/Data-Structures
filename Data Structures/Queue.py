"""
===============================================Queue Data Structure===========================================
** A queue is a useful data structure in programming. It is similar to the ticket queue outside a cinema hall,
where the first person entering the queue is the first person who gets the ticket.
** Queue follows the First In First Out (FIFO) rule - the item that goes in first is the item that comes out first.
"""
class Queue:
    def __init__(self, is_full):
        self.is_full = is_full
        self.list = list()

    #Queue is full?
    def full(self):
        if len(self.list) == self.is_full:
            return f"List Is Full :(\nCount Element In List: {len(self.list)}\n"
        else:
            return f"List Is Not Full\nCount Element In List: {len(self.list)}"

    #add element to list
    def add(self, elem):
        if len(self.list) == self.is_full:
            return f"I can't add element to list, List is Full :(\nCount Element In List: {len(self.list)}\n"
        else:
            self.list.append(elem)
            return f"Ok, add this element: {elem} in list"

    #remove element from list
    def remove(self):
        if len(self.list) == 0:
            return f"I can't remove element from list, list is Empty"
        else:
            self.list.pop(0)
            return f"Ok, remove this element from list"
