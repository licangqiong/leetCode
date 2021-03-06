"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """
    def rehashing(self, hashTable):
        # write your code here
        N = len(hashTable)
        count=0
        
        result = [None]*(N*2)
        N= len(result)
        for node in hashTable:
            while node:
                val = node.val
                newNode = ListNode(val)
                target = result[val%N]
                if not target:
                    result[val%N] = newNode
                else:
                    while target:
                        prev = target
                        target = target.next
                    prev.next = newNode
                node = node.next
        return result
