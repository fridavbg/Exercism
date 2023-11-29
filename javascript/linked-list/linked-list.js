// Node class represents each element in the linked list
class Node {
    constructor(data) {
        this.data = data; // Data stored in the node
        this.next = null; // Reference to the next node
        this.prev = null; // Reference to the previous node (for doubly linked list)
    }
}

// LinkedList class represents the entire linked list
export class LinkedList {
    constructor() {
        this.head = null; // First element of the list
        this.tail = null; // Last element of the list
        this.size = 0; // Total number of elements in the list
    }

    // Adds a new element to the end of the list
    push(element) {
        const node = new Node(element);
        if (this.head == null) {
            // If list is empty, set both head and tail to the new node
            this.head = node;
            this.tail = node;
        } else {
            // If list is not empty, append the new node after the tail and update the tail
            this.tail.next = node;
            node.prev = this.tail;
            this.tail = node;
        }
        this.size++;
    }

    // Removes and returns the last element from the list
    pop() {
        if (this.head == null) {
            return null; // Return null if list is empty
        }
        const poppedValue = this.tail.data;
        this.tail = this.tail.prev;
        if (this.tail) {
            this.tail.next = null;
        } else {
            // If list becomes empty after pop, reset the head as well
            this.head = null;
        }
        this.size--;
        return poppedValue;
    }

    // Removes and returns the first element from the list
    shift() {
        if (this.head == null) {
            return null; // Return null if list is empty
        }
        const shiftedValue = this.head.data;
        this.head = this.head.next;
        if (this.head != null) {
            this.head.prev = null;
        }
        this.size--;
        return shiftedValue;
    }

    // Adds a new element to the start of the list
    unshift(element) {
        const node = new Node(element);
        if (this.head == null) {
            // If list is empty, set both head and tail to the new node
            this.head = node;
            this.tail = node;
        } else {
            // If list is not empty, insert the new node before the head and update the head
            node.next = this.head;
            this.head.prev = node;
            this.head = node;
        }
        this.size++;
        return this.head;
    }

    // Deletes the first occurrence of a specific value from the list
    delete(value) {
        if (this.head == null) {
            return false; // Return false if list is empty
        }
        let current = this.head;

        // If the value is at the head of the list
        if (current.data === value) {
            if (current.next) {
                this.head = current.next;
                this.head.prev = null;
            } else {
                // If the list only contains one node with the value
                this.head = null;
                this.tail = null;
            }
            this.size--;
            return true;
        }

        // Traverse the list to find the value
        while (current.next !== null && current.next.data !== value) {
            current = current.next;
        }

        // Delete the node if the value is found
        if (current.next !== null) {
            if (current.next.next) {
                current.next.next.prev = current;
            } else {
                this.tail = current; // Update the tail if the last element is removed
            }
            current.next = current.next.next;
            this.size--;
            return true;
        }

        return false; // Return false if the value was not found
    }

    // Returns the size of the list
    count() {
        return this.size;
    }
}
