 # Seat Arrangement – Tree Implementation
from collections import deque

class SeatNode:
    def __init__(self, seat_no):
        self.seat_no = seat_no
        self.booked = False
        self.left = None
        self.right = None

class SeatTree:
    def __init__(self):
        self.root = None

    def insert(self, seat_no):
        new_node = SeatNode(seat_no)
        if not self.root:
            self.root = new_node
            return

        q = deque([self.root])
        while q:
            node = q.popleft()
            if not node.left:
                node.left = new_node
                return
            else:
                q.append(node.left)

            if not node.right:
                node.right = new_node
                return
            else:
                q.append(node.right)

    def get_available_seat(self):
        if not self.root:
            return None

        q = deque([self.root])
        while q:
            node = q.popleft()
            if not node.booked:
                return node
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return None

# Ticket Booking Requests – Queue
class BookingSystem:
    def __init__(self):
        self.booking_queue = deque()
        self.waiting_list = deque()
        self.booking_stack = []

    def book_ticket(self, passenger, seat_tree):
        seat = seat_tree.get_available_seat()
        if seat:
            seat.booked = True
            self.booking_stack.append((passenger, seat.seat_no))
            print(f"{passenger} → Seat {seat.seat_no}")
        else:
            self.waiting_list.append(passenger)
            print(f"{passenger} → Waiting List")

# Waiting List Management – Deque
    def add_waiting(self, passenger, tatkal=False):
        if tatkal:
            self.waiting_list.appendleft(passenger)
        else:
            self.waiting_list.append(passenger)

    def allocate_from_waiting(self, freed_seat):
        if self.waiting_list:
            passenger = self.waiting_list.popleft()
            self.booking_stack.append((passenger, freed_seat))
            print(f"{passenger} allocated Seat {freed_seat}")

# Ticket Cancellation – Stack
    def cancel_ticket(self, seat_tree):
        if not self.booking_stack:
            print("No bookings to cancel")
            return

        passenger, seat_no = self.booking_stack.pop()
        print(f"{passenger}'s ticket cancelled")

        # Free the seat
        q = deque([seat_tree.root])
        while q:
            node = q.popleft()
            if node.seat_no == seat_no:
                node.booked = False
                self.allocate_from_waiting(seat_no)
                return
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

# Seat Rearrangement – Deque Rotation
def rotate_seats(seats, k, direction="left"):
    dq = deque(seats)
    if not dq:
        return seats

    if direction == "left":
        dq.rotate(-k)
    else:
        dq.rotate(k)

    return list(dq)

# Admin Reports – Tree Traversals (DFS & BFS)
class Traversals:
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.seat_no, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.seat_no, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.seat_no, end=" ")

    def level_order(self, root):
        if not root:
            return
        q = deque([root])
        while q:
            node = q.popleft()
            print(node.seat_no, end=" ")
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

# # Create Seat Tree
seat_tree = SeatTree()
for seat in [1, 2, 3, 4]:
    seat_tree.insert(seat)

# Booking System
system = BookingSystem()

system.book_ticket("A", seat_tree)
system.book_ticket("B", seat_tree)
system.book_ticket("C", seat_tree)

# Tatkal passenger
system.add_waiting("D", tatkal=True)

# Cancellation
system.cancel_ticket(seat_tree)

# Seat Rotation
print("\nRotated Seats:", rotate_seats([1,2,3,4], 1, "left"))

# Traversals
t = Traversals()
print("\nInorder:")
t.inorder(seat_tree.root)
print("\nLevel Order:")
t.level_order(seat_tree.root)
