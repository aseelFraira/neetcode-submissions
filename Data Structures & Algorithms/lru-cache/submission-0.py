class Node:
    def __init__(self, key, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.head = Node(-1)
        self.tail = Node(-1)

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove_node(self, node_to_remove):
        self.size -= 1
        node_to_remove.prev.next = node_to_remove.next
        node_to_remove.next.prev = node_to_remove.prev

    def insert_node(self, key, val):
        self.size += 1
        new_node = Node(key, val, self.head.next, self.head)
        self.head.next = new_node
        new_node.next.prev = new_node
        return new_node

    def remove_tail(self):
        node_to_remove = self.tail.prev
        self.remove_node(node_to_remove)
        return node_to_remove


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = LinkedList(capacity)
        self.capacity = capacity
        self.seen = {}

    def get(self, key: int) -> int:
        if key not in self.seen:
            return -1

        node = self.seen[key]
        value = node.val
        self.cache.remove_node(node)
        self.seen[key] = self.cache.insert_node(key, value)
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.seen:
            self.cache.remove_node(self.seen[key])

        self.seen[key] = self.cache.insert_node(key, value)

        if self.cache.size > self.capacity:
            tail_node = self.cache.remove_tail()
            del self.seen[tail_node.key]