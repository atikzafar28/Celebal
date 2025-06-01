# Node class 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Managing node
class LinkedList:
    def __init__(self):
        self.head = None

    # Here i have added node at the end 
    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # deleting node based on indexing
    def delete_nth_node(self, n):
        try:
            if self.head is None:
                raise Exception(" empty list")
            if n <= 0:
                raise Exception("Index is less than 0")
            if n == 1:
                self.head = self.head.next
                return
            current = self.head
            for i in range(n - 2):
                if current.next is None:
                    raise Exception("out of range.")
                current = current.next
            if current.next is None:
                raise Exception("out of range.")
            current.next = current.next.next
        except Exception as e:
            print("Error:", e)

    #   printing the list using string
    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.data))
            current = current.next
        return "- ".join(values) + "  None"

# test
ll = LinkedList()
ll.add_node(5)
ll.add_node(10)
ll.add_node(15)
ll.add_node(20)

print("Original list:")
print(ll)

print("\nDeleting 3rd node:")
ll.delete_nth_node(3)
print(ll)

print("\nDeleting 1st node:")
ll.delete_nth_node(1)
print(ll)

print("\ndeleting out of range node:")
ll.delete_nth_node(10)

print("\nDeleting left node:")
ll.delete_nth_node(1)
ll.delete_nth_node(1)
print(ll)

print("\ndeleting node from empty list:")
ll.delete_nth_node(1)
