import random
import math


class OneBasedList:
    """
    A list that uses a one-based index. This is how the book's arrays work. Useful for debugging when converting to a
    zero-based index.
    """

    def __init__(self, collection, auto_append=False):
        """
        Initializes a new instance of the OneBasedList class.
        :param collection: The initial collection to wrapper.
        :param auto_append: True if calls to __setitem__ should increase the collection's size when the index is
                            one index greater than the length of the one based collection, false otherwise.
        """
        if collection is not None:
            self.list = list(collection)
        else:
            self.list = []
        self.auto_append = auto_append

    def __getitem__(self, item):
        if item < 1:
            raise Exception("Index out of range: " + item)
        elif item > len(self.list):
            raise Exception("Index out of range: " + item)

        return self.list[item - 1]

    def __setitem__(self, key, value):
        key = key - 1
        if key < 0:
            raise Exception("Index out of range: " + value)
        elif key == len(self.list):
            if self.auto_append and key == len(self.list):
                self.list.append(value)
                return
            else:
                raise Exception("Index out of range: " + str(value))

        self.list[key] = value

    def __len__(self):
        return len(self.list)

    def __str__(self):
        return str(self.list)


class Stack(OneBasedList):
    """
    Chapter 10: A LIFO stack. Grows dynamically if the initial collection is not large enough to hold a push.
    """

    def __init__(self, collection=None):
        OneBasedList.__init__(self, collection, True)
        self.top = len(self.list)

    def stack_empty(self):
        """
        Chapter 10: Determines if the stack is currently empty.
        :return: True if empty, false otherwise.
        """
        if self.top == 0:
            return True
        return False

    def push(self, x):
        """
        Chapter 10: Adds a value to the top of the stack.
        :param x: The new value to add.
        """
        self.top = self.top + 1
        self[self.top] = x

    def pop(self):
        """
        Chapter 10: Removes the element from the top of the stack.
        :return: The element at the top of the collection.
        """
        if self.stack_empty():
            raise Exception("underflow: Stack empty")
        else:
            self.top = self.top - 1
            return self[self.top + 1]


class Queue(OneBasedList):
    """
    Chapter 10: A FIFO queue. Does not resize to accommodate enqueues that exceed the collection's size.
    """

    def __init__(self, collection):
        OneBasedList.__init__(self, collection, False)
        self.head = 1
        self.tail = len(self) + 1

    def enqueue(self, x):
        """
        Chapter 10: Adds a value to the end of the queue.
        :param x: The new value to add.
        """
        if self.head == self.tail + 1:
            raise Exception("overflow: Queue full.")

        self[self.tail] = x
        if self.tail == len(self):
            self.tail = 1
        else:
            self.tail = self.tail + 1

    def dequeue(self):
        """
        Chapter 10: Removes a element from the beginning of the queue.
        :return: The element at the beginning of the queue.
        """
        if self.head == self.tail:
            raise Exception("underflow: Queue empty.")

        x = self[self.head]
        if self.head == len(self):
            self.head = 1
        else:
            self.head = self.head + 1
        return x


class LinkedList:
    """
    Chapter 10: A linked list class.
    """

    class LinkedListNode:
        """
        Represents all of the values of a linked list node.
        """

        def __init__(self, key, prev_node=None, next_node=None):
            """
            Initializes a new instance of the linked list class.
            :param key: The value to store in the linked list node.
            :param prev_node: A reference to the previous element in the list.
            :param next_node: A reference to the next_node element in the list.
            """
            self.key = key
            self.prev_node = prev_node
            self.next_node = next_node

        def __str__(self):
            return str(self.key)

    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        value = '['
        node = self.head
        if node is not None:
            while True:
                node_value = node.key

                if node.next_node is not None:
                    value += str(node_value) + ', '
                else:
                    value += str(node_value)
                    break

                node = node.next_node

        value += ']'
        return value

    def __len__(self):
        i = 0
        node = self.head
        while node is not None:
            i += 1
            node = node.next_node

        return i

    def list_search(self, k):
        """
        Chapter 10: Searches for the first occurrence of the supplied key.
        :param k: The key to search for.
        :return: The node of the key if found, None otherwise.
        """
        x = self.head
        while x is not None and x.key != k:
            x = x.next_node
        return x

    def list_insert(self, x):
        """
        Chapter 10: Inserts the provided key into the head of the list.
        :param x: The key to insert into the collection.
        """
        x = LinkedList.LinkedListNode(x, next_node=self.head)
        if self.head is not None:
            self.head.prev_node = x
        self.head = x
        x.prev_node = None

    def list_delete(self, x):
        """
        Chapter 10: Removes the provided key from the collection.
        :param x: The key to remove.
        """
        # Not in the original code, just here for convenience.
        if x is not LinkedList.LinkedListNode:
            x = self.list_search(x)

        if x.prev_node is not None:
            x.prev_node.next_node = x.next_node
        else:
            self.head = x.next_node

        if x.next_node is not None:
            x.next_node.prev_node = x.prev_node


class LinkedListSentinel:
    """
    Chapter 10: A linked list class that uses sentinels. A sentinel is a dummy value that allows us to avoid some
    complexity when performing operations by avoiding boundary conditions. A sentinel value can also reduce running time
    when a significant amount of time is spent checking boundary conditions in loops. The sentinel while empty and
    meaningless contains all of the methods of a valid value being understood to be the end of the list. A sentinel
    should not be used when there are a large number of small lists since the sentinel wastes memory.
    """

    class LinkedListNode:
        """
        Represents all of the values of a linked list node.
        """

        def __init__(self, key, prev_node=None, next_node=None):
            """
            Initializes a new instance of the linked list class.
            :param key: The value to store in the linked list node.
            :param prev_node: A reference to the previous element in the list.
            :param next_node: A reference to the next_node element in the list.
            """
            self.key = key
            self.prev_node = prev_node
            self.next_node = next_node

        def __str__(self):
            return str(self.key)

    def __init__(self):
        self.sentinel = LinkedListSentinel.LinkedListNode(None)
        self.sentinel.next_node = self.sentinel
        self.sentinel.prev_node = self.sentinel

    def __str__(self):
        value = '['
        node = self.sentinel.next_node
        if node != self.sentinel:
            while True:
                node_value = node.key

                if node.next_node != self.sentinel:
                    value += str(node_value) + ', '
                else:
                    value += str(node_value)
                    break

                node = node.next_node

        value += ']'
        return value

    def __len__(self):
        i = 0
        node = self.sentinel.next_node
        while node != self.sentinel:
            i += 1
            node = node.next_node

        return i

    def list_search(self, k):
        """
        Chapter 10: Searches for the first occurrence of the supplied key.
        :param k: The key to search for.
        :return: The node of the key if found, None otherwise.
        """
        x = self.sentinel.next_node
        while x != self.sentinel and x.key != k:
            x = x.next_node
        return x

    def list_insert(self, x):
        """
        Chapter 10: Inserts the provided key into the head of the list.
        :param x: The key to insert into the collection.
        """
        x = LinkedListSentinel.LinkedListNode(x, next_node=self.sentinel.next_node)
        self.sentinel.next_node.prev_node = x
        self.sentinel.next_node = x
        x.prev_node = self.sentinel

    def list_delete(self, x):
        """
        Chapter 10: Removes the provided key from the collection.
        :param x: The key to remove.
        """
        # Not in the original code, just here for convenience.
        if x is not LinkedListSentinel.LinkedListNode:
            x = self.list_search(x)

        x.prev_node.next_node = x.next_node
        x.next_node.prev_node = x.prev_node


class BinaryTreePointers:
    """
    Chapter 10: A representation of a tree using pointers. Each node has a pointer to a left child, a right child, and its parent.
    """

    class TreeNode:
        """
        A tree node. If the parent node is None the node is assumed to be the root node.
        """

        def __init__(self, key, p=None, left=None, right=None):
            """
            Initializes a new instance of the TreeNode class.
            :param key: The key value of the node.
            :param p: The parent node.
            :param left: The left child node.
            :param right: The right child node.
            """
            self.p = p
            self.left = left
            self.right = right
            self.key = key

    def __init__(self):
        self.root = None


class RootedTree:
    """
    Chapter 10: A tree with an unbounded number of child nodes. Nodes have a pointer to the parent, left child, and right sibling.
    This means that no node has a pointer to its right child. Instead the left child must be retrieved and its right
    sibling accessed. Right siblings do contain a reference to their parent.
    """

    class TreeNode:
        def __init__(self, key, p=None, left_child=None, right_sibling=None):
            """
            Initializes a new instance of the TreeNode class.
            :param key: The key value of the node.
            :param p: The parent node.
            :param left_child: The left child node.
            :param right_sibling: The right sibling node at the same level of the tree.
            """
            self.key = key
            self.p = p
            self.left_child = left_child
            self.right_sibling = right_sibling

    def __init__(self):
        self.root = None


class DirectAccessTable:
    """
    Chapter 11: A data structure that has very efficient searching capabilities when the number of keys is very small.
    """

    class Entry:
        """
        A entry in the table.
        """

        def __init__(self, key, satellite_data=None):
            self.key = key
            self.satellite_data = satellite_data

    def __init__(self, size):
        self.list = [None] * size

    def __getitem__(self, item):
        return self.list[item]

    def __setitem__(self, key, value):
        self.list[key] = value

    def direct_address_search(self, k):
        """
        Chapter 11: Returns the passed in key directly from the collection.
        :param k: The key to return the value of.
        :return: The value at key.
        """
        return self[k]

    def direct_address_insert(self, x, satellite_data=None):
        """
        Chapter 11: Inserts an entry directly into the DirectAccessTable's collection.
        :param x: The key value to insert or the DirectAccessTable.Entry to add.
        :param satellite_data: The satellite data to include. Will not be used if x is DirectAccessTable.Entry.
        """
        if x is not DirectAccessTable.Entry:
            x = DirectAccessTable.Entry(x, satellite_data)

        self[x.key] = x

    def direct_access_delete(self, x):
        """
        Chapter 11: Removes an entry from the DirectAccessTable.
        :param x: The key value or the DirectAccessTable.Entry to remove.
        """
        if x is not DirectAccessTable.Entry:
            x = DirectAccessTable.Entry(x)

        self[x.key] = None


class HashTable:
    """
    Chapter 11: A data structure optimized for searching. Works by passing entries through a hash function that converts search
    data into the index of the table of values.
    """

    def __init__(self, size):
        """
        Initializes a new instance of the hash table class.
        :param size: The size of the hash table to create.
        """
        self.hash_table = [None] * size

    def hash_division(self, k):
        """
        Chapter 11: Hash division is accomplished by taking the remainder of a division operation. If hash division is used
        the size of the collection should not be a power of 2. The reason being that if hash_table size equals 2^P then
        hash_division(k) will equal the lower p bits of k. Unless the keys passed in have an equally distributed pattern
        of lower p bits this will result in many collisions. Prime numbers that are not close to a power of 2 tend
        to be good sizes for this hashing algorithm.
        :param k: The key to computer the hash of.
        :return: The hash value.
        """
        return k % len(self.hash_table)

    def hash_multiplication(self, k):
        """
        Chapter 11: Hash multiplication is accomplished by plugging the key into a mathematical equation. This has the advantage of
        not placing enough emphasis on the size of the hash table.
        :param k: The key to hash.
        :return: The hash value.
        """
        if self.A is None:
            # A should be between 0 and 1
            self.A = random.random()

        return math.floor(len(self.hash_table) * ((k * self.A) % 1))

    def chained_hash_insert(self, x):
        """
        Chapter 11: Inserts a value into the linked list at a given hash table location.
        :param x: The value to insert into the hash table.
        """
        linked_list = self.hash_table[hash(x.key)]
        linked_list.list_insert(x)

    def chained_hash_search(self, k):
        """
        Chapter 11: Finds a value in the linked list at a given hash table location.
        :param k: The key to look up.
        :return: The element at the provided key location.
        """
        linked_list = self.hash_table[hash(k)]
        return linked_list.list_search(k)

    def chained_hash_delete(self, x):
        """
        Chapter 11: Removes a value from the linked list at a given hash table location.
        :param x: The value to remove from the hash table.
        """
        linked_list = self.hash_table[hash(x.key)]
        linked_list.list_delete(x)
