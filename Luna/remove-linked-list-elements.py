#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head, val):
        if head == None:
            return None

        # 재귀함수 풀이
        if head.val == val: # 내가 6이라면 나를 삭제하고
            # return head.next 내 뒤를 그대로 넘기는 것이 아니라
            return self.removeElements(head.next, val) # 6이 제거된 리스트를 반환해야 하므로 재귀 돌린 결과를 반환한다
        else: # 내가 6이 아니라면?
            head.next = self.removeElements(head.next, val)
            return head
## sol2)        
class Solution:
    def removeElements(self, head, val):
        if head == None:
            return None
        iter = head #반복을 위해 변수를 만들기

        while iter.next !=None:
            if iter.next.val == val:
                iter.next = iter.next.next
            else:
                iter = iter.next
        ## 리턴시에는 전체리스트 원소에 접근할수 있도록 head 반환해야함
        # 리스트의 맨처음에 있을 경우 - 나머지 부분을 새헤드로 반환
        if head.val == val:
            return head.next
        # 그렇지 않은 경우 - 원본 반환
        else:
            return head