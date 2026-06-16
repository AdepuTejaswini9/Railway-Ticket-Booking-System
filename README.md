# Railway-Ticket-Booking-System


## Overview

The Railway Ticket Booking System is a Python-based project that demonstrates the practical implementation of fundamental Data Structures and Algorithms (DSA) in a real-world reservation system scenario.

The system manages seat allocation, ticket booking, waiting lists, cancellations, and administrative reporting using various data structures such as Binary Trees, Queues, Stacks, and Deques.

This project was developed to strengthen problem-solving skills and showcase the application of DSA concepts in software development.

---

## Features

### Seat Management

* Organizes seats using a Binary Tree structure.
* Automatically allocates the first available seat using Breadth-First Search (BFS).

### Ticket Booking

* Processes passenger booking requests.
* Assigns available seats efficiently.

### Waiting List Management

* Maintains a waiting list when all seats are occupied.
* Supports Tatkal (priority) bookings using deque operations.

### Ticket Cancellation

* Handles ticket cancellations using a Stack.
* Automatically reallocates freed seats to waiting-list passengers.

### Seat Rearrangement

* Supports seat rotation using Deque operations.

### Administrative Reports

* Generates seat information using:

  * Inorder Traversal
  * Preorder Traversal
  * Postorder Traversal
  * Level Order Traversal (BFS)

---

## Data Structures Used

| Data Structure | Purpose                                   |
| -------------- | ----------------------------------------- |
| Binary Tree    | Seat organization and allocation          |
| Queue          | Booking request processing                |
| Deque          | Waiting list and Tatkal priority handling |
| Stack          | Ticket cancellation management            |
| BFS Traversal  | Available seat allocation                 |
| DFS Traversals | Administrative reporting                  |

---

## Technologies Used

* Python 3
* Object-Oriented Programming (OOP)
* Data Structures & Algorithms

---

## Project Structure

```text
Railway-Ticket-Booking-System/
│
├── project.py
├── README.md
└── screenshots/
```

---

## How It Works

1. Seats are stored in a Binary Tree.
2. Booking requests are processed sequentially.
3. Available seats are assigned using BFS traversal.
4. If seats are unavailable, passengers are moved to the waiting list.
5. Tatkal passengers receive higher priority.
6. Upon cancellation, the first passenger in the waiting list is automatically assigned the freed seat.
7. Administrators can view seat arrangements using different tree traversal techniques.

---

## Sample Output

```text
A → Seat 1
B → Seat 2
C → Seat 3

A's ticket cancelled

D allocated Seat 1

Rotated Seats: [2, 3, 4, 1]

Inorder:
4 2 1 3

Level Order:
1 2 3 4
```

---

## Learning Outcomes

Through this project, I gained hands-on experience with:

* Binary Trees
* Queues and Deques
* Stacks
* Breadth-First Search (BFS)
* Depth-First Search (DFS)
* Object-Oriented Programming
* Algorithm Design
* Real-world applications of Data Structures

---

## Future Enhancements

* Graphical User Interface (GUI)
* Database integration using SQLite/MySQL
* User authentication system
* Web-based deployment using Flask or FastAPI
* Real-time seat availability dashboard

---

## Author

**Adepu Tejaswini**

* LinkedIn: [www.linkedin.com/in/adeputejaswini](http://www.linkedin.com/in/adeputejaswini)
* GitHub: https://github.com/<your-github-username>
