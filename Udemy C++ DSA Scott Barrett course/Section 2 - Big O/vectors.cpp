// Big O for vectors also applied to arrays.
// vector/array usually looks like this -> [11, 3, 23, 7].
// vector.push_back(17) adds 17 to the end -> [11, 3, 23, 7, 17].
// from a big o perspective with vectors/arrays, n is num of items in data struct,
// & to add something to end we don't have to touch any of other vect items.
// likeweise, when removing 17 with myVect.pop_back(), we don't have to touch
// anything else in the vect. therefore adding or removing anything for a vector
// is o(1).
// removing an item from the other end (front) of a vector using
// myVect.erase(myVect.begin()), the problem we have is that the vector becomes
// [3, 23, 7] and the index for the number 3 gets changed from 1 to 0 and the
// other number's indexes are also decremented. Likewise, if you add that item
// back in with myVect.insert(myVect.begin(), 11), in order to do that we have
// to change all numbers indexes by incrementing them to put 11 in. It doesn't
// matter if you're adding or removing from the beginning because you have to
// touch every item in the vector, therefore doing that from the start of
// the vector is o(n).
// if youre adding or removing from the end, its o(1), but if youre doing it from
// the beginning, due to reindexing, its o(n).
// now, for adding a vector somewhere in the middle with 
// myVect.insert(myVect.begin()+1, 99) (adding to the index after the first element),
// now the indexes after index 1 are incorrect e.g. 3 needs to be index 2, and also
// the indexes before the inserted items, thefore all index are touched and this
// operation is O(n). it's not o((1/2)n) because big O is worst case not average
// case and 1/2 is a constant, which is dropped to become o(n). likewise for
// removing a element int he middle of a vector, we have to change indexes before
// and after so its o(n).
// for finding an item by value (e.g. 7 in the vector [11, 3, 23, 7]), we
// first check if the first item has a value of 7 and then iterate through the
// vector until we find the value of 7, looking up by value is o(n), but looking
// up by index means we go directly to that place in memory in one step, which
// means it's o(1).