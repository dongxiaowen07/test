#!/usr/bin/python3
#coding=utf-8

from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # 两数之和 哈希表
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        在数组中找到两个数，使得它们的和等于一个特定目标数，并返回它们的数组下标。

        参数：
        nums：一个整数列表，表示输入的数组。
        target：一个整数，表示目标和。

        返回值：
        一个整数列表，包含两个整数，它们是数组中两个数的下标，使得它们的和等于目标和。
        如果没有找到满足条件的两个数，则返回空列表。
        """
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # 使用字典存储数组元素及其索引，以加快查找速度
        map = dict()
        for i, item in enumerate(nums):
            if target - item in map:
                return [i, map.get(target - item)]
            else:
                map[item] = i
        return []

    # 无重复字符的最长子串 滑动窗口

    def lengthOfLongestSubstring(self, s: str) -> int:
        occ = set()
        n = len(s)
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                occ.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in occ:
                occ.add(s[rk + 1])
                rk += 1
            ans = max(ans, rk - i + 1)
        return ans
        
    # 回文数
    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        ans = 0
        while x > ans:
            ans = ans*10 + x % 10
            x //= 10
        return x == ans or x == (ans//10)

    # 翻转链表
    def reverseList(self, head: ListNode) -> ListNode:
        # 迭代
        pre, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre
        # 递归
        # if not head or not head.next:
        #     return head
        # newHead = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return newHead


    # 快排
    # def fast_sort(list_):
#     # if len(list_) == 1:
#     #     return list_
#     mid_value = list_[0]
#     low = 0
#     high = len(list_) - 1
#
#     while low < high:
#         while low < high and list_[high] >= mid_value:
#             high -= 1
#         list_[low] = list_[high]
#         while low < high and list_[low] < mid_value:
#             low += 1
#         list_[high] = list_[low]
#     # print(low, high)
#     list_[low] = mid_value
#
#     if low > 0:
#         list_[0:low] = fast_sort(list_[0:low])
#     if low < len(list_) - 1:
#         list_[low + 1:] = fast_sort(list_[low + 1:])
#
#     return list_

    # 快排
    def fast_sort(self, list_, first, last):
        if first >= last:
            return
        mid_value = list_[first]
        low = first
        high = last

        while low < high:
            while low < high and list_[high] >= mid_value:
                high -= 1
            list_[low] = list_[high]
            while low < high and list_[low] < mid_value:
                low += 1
            list_[high] = list_[low]
        # print(low, high)
        list_[low] = mid_value

        self.fast_sort(list_, first, low - 1)
        self.fast_sort(list_, low + 1, last)

    # 合并有序链表 递归
    def mergeTwoLists_recur(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
    # 合并有序链表 迭代
    def mergeTwoLists_iter(self, l1, l2):
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next            
            prev = prev.next

        # 合并后 l1 和 l2 最多只有一个还未被合并完，我们直接将链表末尾指向未合并完的链表即可
        prev.next = l1 if l1 is not None else l2

        return prehead.next
    
    # 最大回文串 贪心
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        counter_map = collections.Counter(s)
        for v in counter_map.values():
            ans += v // 2 * 2
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        return ans

    

if __name__ == '__main__':
    mysolution = Solution()
    nums = [4, 5, 7, 1]
    target = 8
    print(mysolution.twoSum(nums, target))
    mys = "abcabcbb"
    print(mysolution.lengthOfLongestSubstring(mys))
    num_1 = 123321
    num_2 = 12321
    num_3 = 123456
    print(mysolution.isPalindrome(num_1))
    print(mysolution.isPalindrome(num_2))
    print(mysolution.isPalindrome(num_3))
    list_ = [38, 67, 11, 26, 20, 99, 45, 54]
    print(list_)
    mysolution.fast_sort(list_, 0, len(list_) - 1)
    # fast_sort(list_)
    print(list_)
