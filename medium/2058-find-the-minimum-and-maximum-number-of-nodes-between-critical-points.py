class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        curr = head.next
        index = 1

        first = -1
        last = -1
        minDistance = float('inf')

        while curr.next:
            if ((curr.val > prev.val and curr.val > curr.next.val) or
                (curr.val < prev.val and curr.val < curr.next.val)):

                if first == -1:
                    first = index
                else:
                    minDistance = min(minDistance, index - last)

                last = index

            prev = curr
            curr = curr.next
            index += 1

        if first == last:
            return [-1, -1]

        return [minDistance, last - first]
