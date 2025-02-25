from typing import List


class Node():
    def __init__(self, value: int):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self):
        self.size = 0
        self.head = None

    def insert(self, value : int):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        self.size += 1
    
    def delete(self, value : int):
        if not self.head:
            print("Empty list")
            return
        if self.head.value == value:
            self.head = self.head.next
            self.size -= 1
            return
        prev = self.head
        curr = self.head.next
        while curr:
            if curr.value == value:
                prev.next = curr.next
                self.size -= 1
                return
            prev = curr
            curr = curr.next

    def search(self, value : int) -> bool:
        if not self.head:
            print("Empty list")
            return False
        if self.head.value == value:
            return True
        curr = self.head
        while curr:
            if curr.value == value:
                return True
            curr = curr.next
        return False

    def sort(self):
        if not self.head or not self.head.next:
            print("Empty list or single element list")
            return

        swapped = True
        while swapped:
            swapped = False
            curr = self.head
            while curr.next:
                if curr.value > curr.next.value:
                    curr.value, curr.next.value = curr.next.value, curr.value
                    swapped = True
                curr = curr.next

    def traverse(self) -> List[Node]:
        ll = []
        curr = self.head
        while curr:
            ll.append(curr.value)
            curr = curr.next
        return ll


if __name__ == "__main__":
    ll = LinkedList()
    for i in [3, 2, 1, 5, 1]:
        ll.insert(i)
        print("inserted", i)
    print("Original list:", ll.traverse())
    ll.sort()
    print("Sorted list:", ll.traverse())
