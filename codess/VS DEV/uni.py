# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None


# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None

#     # Insert at the beginning
#     def insert_at_beginning(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             new_node.next = self.head
#             self.head.prev = new_node
#             self.head = new_node

#     # Insert at the end
#     def insert_at_end(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = new_node
#             new_node.prev = current

#     # Delete a node by value
#     def delete_by_value(self, value):
#         if self.head is None:
#             print("The list is empty.")
#             return

#         # If the node to be deleted is the head
#         if self.head.data == value:
#             if self.head.next is None:  # If there's only one node
#                 self.head = None
#             else:
#                 self.head = self.head.next
#                 self.head.prev = None
#             return

#         # Traverse to find the node to delete
#         current = self.head
#         while current and current.data != value:
#             current = current.next

#         if current is None:
#             print(f"Value {value} not found in the list.")
#             return

#         # Update pointers to remove the node
#         if current.next:  # If it's not the last node
#             current.next.prev = current.prev
#         if current.prev:  # If it's not the first node
#             current.prev.next = current.next

#     # Display the list
#     def display(self):
#         if self.head is None:
#             print("The list is empty.")
#             return

#         current = self.head
#         while current:
#             print(current.data, end=" <-> " if current.next else "")
#             current = current.next
#         print()


# # Example Usage
# dll = DoublyLinkedList()
# dll.insert_at_beginning(10)
# dll.insert_at_beginning(20)
# dll.insert_at_end(30)
# dll.insert_at_end(40)

# print("Doubly Linked List after insertions:")
# dll.display()

# dll.delete_by_value(20)
# print("Doubly Linked List after deleting 20:")
# dll.display()

# dll.delete_by_value(40)
# print("Doubly Linked List after deleting 40:")
# dll.display()


def symbol(a):
    d={"[":"]","{":"}","(":")"}
    return(d[a])
print(symbol("["))