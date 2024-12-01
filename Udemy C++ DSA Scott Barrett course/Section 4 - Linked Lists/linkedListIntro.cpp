// ds that linked list is commonly compared to is array or vector, both vectors +
// linked lists are dynamic in length, array fixed
// vector has indexes where you can go directly to an index, LL doesn't have that.
// say linked list is 11, 3, 23, 7 , items spread in different places in memory
// instead of a contiguous location like vectors or arrays (nodes)
// LL has var that points to the first node called head, and a variable that points
// to the last node called tail, and each node will point to the next, to the next etc.
// HEAD->11->3->23->7(<-TAIL) then 7 points to null pointer (nullptr)
// vectors and arrays have contigous memory so you can go directly to indexes
// as O(1) operation