#!/usr/bin/env python

#https://leetcode.com/problems/merge-k-sorted-lists/


'''

 Merge k Sorted Lists
Hard

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.



Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:

Input: lists = []
Output: []

Example 3:

Input: lists = [[]]
Output: []



Constraints:

    k == lists.length
    0 <= k <= 104
    0 <= lists[i].length <= 500
    -104 <= lists[i][j] <= 104
    lists[i] is sorted in ascending order.
    The sum of lists[i].length will not exceed 104.

Accepted
1,273,756
Submissions
2,697,355

Runtime: 205 ms, faster than 26.69% of Python3 online submissions for Merge k Sorted Lists.
Memory Usage: 18.2 MB, less than 39.84% of Python3 online submissions for Merge k Sorted Lists.
'''

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def addToLinkedList(l0: ListNode, num : int):

    if l0 == None :
        l0 = ListNode()
        l0.val = num

    else :
        #search for the end of the list...
        curr = l0
        while True:
            if curr.next != None :
                curr = curr.next
            else :
                tmp = ListNode()
                tmp.val = num
                curr.next = tmp
                break

    return l0



def strLinkedList(l0: ListNode) :

    if l0 == None:
        return "[]"
    s = "["
    curr = l0
    while curr != None :
        s += str(curr.val) + ", "
        curr = curr.next
    s = s[:-2]+"]"
    return s

def makeLinkedList(list:List[int]):
    l0=None
    ptr=None
    for num in list:
        if ptr == None:
            ptr = ListNode()
            ptr.val = num
            l0 = ptr
        else:
            ptr.next = ListNode()
            ptr = ptr.next
            ptr.val = num

    return l0

def mergeLists(l0: Optional[ListNode], l1 : Optional[ListNode]) -> Optional[ListNode]:

    ll  = None
    ptr = None

    while l0 != None or l1 != None :
        val = 0
        if l0 == None:
            val = l1.val
            l1  = l1.next
        elif l1 == None:
            val = l0.val
            l0  = l0.next
        elif l0.val <= l1.val:
            val = l0.val
            l0 = l0.next
        else:
            val = l1.val
            l1 = l1.next

        if ptr == None :
            ptr = ListNode()
            ll=ptr
        else:
            ptr.next = ListNode()
            ptr = ptr.next

        ptr.val = val

    return ll

class Solution:

    #attempt 1 two slow
    def mergeKLists_1(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        ll = None

        for list in lists:
            if ll == None:
                ll = list
            else:
                ll = mergeLists(ll, list)

        return ll

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        while len(lists) > 1:
            ll = []
            while True:
                #1 element
                if len(lists) == 1:
                    l0 = lists.pop()
                    ll.append(l0)
                # 2 elements
                else:
                    l0 = lists.pop()
                    l1 = lists.pop()
                    ll.append(mergeLists(l0, l1))

                #no elements
                if len(lists) == 0:
                    break

            lists = ll

        if len(lists) == 0:
            return None

        return lists[0]


obj = Solution()

l0 = [makeLinkedList([1,4,5]), makeLinkedList([1,3,4]), makeLinkedList([2,6])]

for l in l0:
    print(strLinkedList(l))

rslt = obj.mergeKLists(l0)

print(strLinkedList(rslt))

l0 = [makeLinkedList([])]

for l in l0:
    print(strLinkedList(l))

rslt = obj.mergeKLists(l0)

print(strLinkedList(rslt))