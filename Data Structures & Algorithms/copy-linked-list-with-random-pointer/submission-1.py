"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        otn={None:None}

        cur=head
        while cur:
            copy=Node(cur.val)
            otn[cur]=copy
            cur=cur.next
        cur=head
        while cur:
            copy=otn[cur]
            copy.next=otn[cur.next]
            copy.random=otn[cur.random]
            cur=cur.next
        return otn[head]
