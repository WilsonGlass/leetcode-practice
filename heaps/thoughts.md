<b>Heaps</b>

Also known as priority queues, is a special kind of queue
where elements are removed in order of priority, not just in the order they were added

Under the hood, priority queues are usually implemented as binary heaps
which are just binary trees stored in arrays.

There are two main kinds:

Min Heap:
every parent is smaller than its children

Max Heap:
Every parent is bigger than its children

Use Heaps/Priority queues when:
* Repeatedly extracting the smallest/largest item
* Maintaining a top-k or bottom-k set of values
* Real-time ranking, greedy selection, etc.
* Need to sort on the fly, faster than O(nlogn)