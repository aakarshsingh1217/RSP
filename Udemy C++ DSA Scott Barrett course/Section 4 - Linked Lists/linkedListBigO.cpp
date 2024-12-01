// adding a node to end of LL
// HEAD->11->3->23->7(<-TAIL) then 7 points to null pointer (nullptr)
// becomes HEAD->11->3->23->7->4-<(TAIL) then 4 points to null pointer (nullptr)
// for Big O, N is going to be the number of nodes in the linked list
// doesn't matter if LL had 4 items, or a million, it's going to be the same num
// of operations to add a node to the end, which means it's constant time, and
// constant time is O(1)

// removing item from end of LL
// HEAD->11->3->23->7->4-<(TAIL) then 4 points to null pointer (nullptr)
// can't just remove node and remove tail back to previous node and have 7 point to
// nullptr
// to set the tail pointer to point to the 7 node, we have to set it equal to another
// pointer that's pointing to the 7 node, only one pointer that's pointing at that node
// and that's the 23 pointer pointing to 7, so we have to set tail to be equal to that
// pointer
// therefore, we have to start at the head pointer and iterate through the linked list
// until we get to the pointer that points to 7 from 23, and set tail to equal to that
// since we have to iterate through the entire linked list, that makes the operation
// O(n)

// adding from start of LL
// HEAD->11->3->23->7(<-TAIL) then 7 points to null pointer (nullptr)
// adding an item 4 to the start, in order to point that 4 node at the 11 node (start),
// we can set that pointer from the four node to be equal to head and that'll point
// it at that 11 node, and we move head over to the new node and that adds that
// into the linked list
// becomes HEAD->4->11->3->23->7(<-TAIL) then 7 points to null pointer (nullptr)
// this'll be the same number of operations regardless of the number of nodes already
// in linked list, which means it's o(1)

// removing from start of LL
// HEAD->4->11->3->23->7(<-TAIL) then 7 points to null pointer (nullptr)
// move head over to the node to the right (11), equate it to head.next, then remove
// 4 node
// this'll be the same number of operations regardless of the number of nodes already
// in linked list, which means it's o(1)
// HEAD->11->3->23->7(<-TAIL) then 7 points to null pointer (nullptr)

// adding node somewhere in the middle
// let say we're going to add 4 node right after 23 node
// so HEAD->11->3->23->4->7(<-TAIL) then 7 points to null pointer (nullptr)
// we have to start at the head and iterate through the linked list until we get
// to the 23 node
// first thing is to have 4 node point to the same node that the 23 is pointing to,
// by taking pointer that is pointing to 7 node (23 node pointer) and setting
// pointer from 4 node equal to it, then 23 node point to 4 node and now it's
// added into LL
// because we had to iterate, it's O(n)

// removing somewhere in middle
// we have to start at the head and iterate through the linked list until we get
// to the 4 node (node we're going to remove). we'll set pointer from 23 node
// to be equal to pointer frmo 4 node (to 7), then remove 4 node and return it
// becuase we had to iterate through the list this is o(n)

// return val of node at index 2
// linked lists dont have indexes built into nodes, we have to start at the head and
// count over to 23 node
// HEAD->11->3->23(here)->7(<-TAIL) then 7 points to null pointer (nullptr)
// then return that val
// since we have to iterate through to get to a particular index, likewise if we want
// to find a value e.g. the value of 23 to see if its in there, have to start at 
// head, check to see if thats 23 and so on until we get to the value that 
// gets to 23 and return true
// therefore in a linked list its O(n) whether we're looking up by index or by value