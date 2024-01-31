from collections import deque
class Solution(object):
    def levelOrder(self, root):
        if root is None: return []
        queue = deque()
        queue.append(root) #첫번째요소 넣음 3
        result = []
        while len(queue) !=0:
            level_size = len(queue)
            current_level = [] # 현재 요소를 넣을 리스트
            for i in range(level_size):
                node = queue.popleft() #가장 첫번째 원소 3 을 빼냄
                if node: 
                    current_level.append(node.val)
                    if node.left: 
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            result.append(current_level)

        return result