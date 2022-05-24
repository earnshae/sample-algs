#!/usr/bin/env python

#https://leetcode.com/problems/two-sum/

from typing import Optional

'''
2. Add Two Numbers
Medium

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 
Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


'''

#add to list


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
    s = "["
    curr = l0
    while curr != None :
        s += str(curr.val) + ", "
        curr = curr.next
    s = s[:-2]+"]"
    return s

class Solution:
    #THE EASY SOLUTION O(N^2)
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        rslt = l1

        #FIRST ADD ALL THE NUMBERS FROM L1 TO THE RSLT
        #curr1 = l1
        #while curr1 != None:
        #    rslt = addToLinkedList(rslt, curr1.val)
        #    curr1 = curr1.next

        carry = 0

        curr2 = l2
        curr_rslt = rslt

        i = 0
        while curr2 != None:
            print(i)
            curr_rslt.val += curr2.val + carry
            carry = 0
            i += 1
            #carry math
            if curr_rslt.val > 9:
                carry = 1
                curr_rslt.val -= 10

            #DO WE NEED A NEW NODE
            if curr_rslt.next == None:
                if carry == 1 or curr2.next != None:
                    curr_rslt.next = ListNode()
                    curr_rslt.next.val = carry
                    carry = 0

            #DO THE POINTERS
            curr2 = curr2.next
            curr_rslt = curr_rslt.next

        while carry == 1 and curr_rslt != None:
            curr_rslt.val += carry
            carry = 0
            if curr_rslt.val > 9:
                carry = 1
                curr_rslt.val -= 10
            if curr_rslt.next == None and carry == 1 :
                curr_rslt.next = ListNode()
                curr_rslt.next.val = carry
                carry = 0
            curr_rslt = curr_rslt.next

        return rslt




l1 = None
l1 = addToLinkedList(l1, 2)
l1 = addToLinkedList(l1, 4)
l1 = addToLinkedList(l1, 3)

print(strLinkedList(l1))

l2 = None
l2 = addToLinkedList(l2, 5)
l2 = addToLinkedList(l2, 6)
l2 = addToLinkedList(l2, 4)
print(strLinkedList(l2))

obj = Solution()

rslt = obj.addTwoNumbers(l1, l2)

print(strLinkedList(rslt))

l1 = None
l1 = addToLinkedList(l1, 0)
print(strLinkedList(l1))
l2 = None
l2 = addToLinkedList(l2, 0)
print(strLinkedList(l1))
rslt = obj.addTwoNumbers(l1, l2)

print(strLinkedList(rslt))

l1 = None
for n in [9,9,9,9,9,9,9] :
    l1 = addToLinkedList(l1, n)
print(strLinkedList(l1))

l2 = None
for n in [9,9,9,9] :
    l2 = addToLinkedList(l2, n)

print(strLinkedList(l2))

rslt = obj.addTwoNumbers(l1, l2)

print(strLinkedList(rslt))