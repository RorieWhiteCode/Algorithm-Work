

																		"""
===============================
TEMPLATES
===============================
						
																		"""

#Constructing a Tree
def __init__(self.val=None):

	self.val = val
	if self.value:
		self.left = Tree()
		self.right = Tree()
	else:
		self.left = None
		self.right = None

def isempty(self):
	return (self.value==None)

def insert(self, data):
	if self.isempty():
		self.value = data
		self.left = Tree()
		self.right = Tree()
		print(" {} Sucessfully inserted".format(self.value))
	elif data < self.value:	
		self.left.insert(data)
		return
	elif data > self.value:
		self.right.insert(data)
	elif data == self.values
		return
t = Tree(15)
t.insert(5)
#=====================================================================================================================================
#Constructing a Linked-List
class Node:
    def __init__(self, data):
        self.data = data  # Data stored in the node
        self.next = None  # Pointer to the next node (initially None)
        
class LinkedList:
    def __init__(self):
        self.head = None  # Head pointer, initially empty (None)

    # Add a node at the end
    def append(self, data):
        new_node = Node(data)  # Create a new node
        if self.head is None:
            self.head = new_node  # If the list is empty, set head to the new node
            return
        current = self.head
        while current.next:
            current = current.next  # Traverse to the last node
        current.next = new_node  # Point the last node to the new node

    # Display the linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
#=====================================================================================================================================

																			"""
===============================
Python Leet-code Array Question
===============================
																			"""
#=====================================================================================================================================
#Remove Duplicates In-Place
nums = [1,2,2]
if not nums:
	return 0
i = 0
for j in range(1, len(nums)):
	if nums[j] != nums[i]:
		i+=1
		nums[i] = nums[j]
return i + 1
#=====================================================================================================================================
#Remove Element In-Place
k = 0
val = 2 
nums = [1,2,2]
for i in range(len(nums)):
	if nums[i] != val:
		nums[k] = nums[i]
		k+=1
del nums[k:]
return k

#Remove Using List Comprehension
k = 0
val = 2 
nums = [1,2,2]
a = [x for x in nums if x != val]
return a

#Best Memory Solution:
i = len(nums)
for j in range(len(nums)-1, -1, -1):
    if nums[j] == val:
        i -= 1
        nums[j], nums[i] = nums[i], nums[j]
return i
#=====================================================================================================================================
#3SUM: nums[i] + nums[j] + nums[k], avoid n^3 by using two pointer method reducing to n^2
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1 
            right = len(nums) - 1
            while left < right:
                a = nums[i] + nums[left] + nums[right]
                if a == 0:
                    triplets.append((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left +=1
                    while left < right and nums[right] == nums[right+1]:
                        right -=1
                elif a < 0:
                    left += 1
                else: 
                    right -= 1
        return triplets
#=====================================================================================================================================
#4SUM: nums[a] + nums[b] + nums[c] + nums[d] == target. Same method as 3SUM
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        quad = []
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i+1, len(nums)-2):
                if j > i+1 and nums[j] == nums[j - 1]:
                    continue
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    a = nums[i] + nums[j] + nums[right] + nums[left]
                    if a == target:
                        quad.append([nums[i], nums[j], nums[right], nums[left]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left-1]:
                            left +=1
                        while left < right and nums[right] == nums[right+1]:
                            right -=1
                    elif a < target:
                        left+=1
                    else:
                        right-=1
        return quad
#Can we do 5SUM, would the core logic apply?
#=====================================================================================================================================
#Majority element, i.e. [3,2,3] => 3, ideally linear time and O(1) space, however my solution is lazy and O(k) space
from collections import Counter
nums = [3,2,3]
c = Counter(nums)
return c.most_common(1)[0][0] #most_common(1) Returns a list of tuples containing the top 1 most frequent element and its count. 
#By adding [0], you're extracting the first tuple from the list. 
#The [0] of the tuple extracts the first item of the tuple, which is the element itself.
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
		res = maj = 0
		        for n in nums:
		            if maj == 0:
		                res = n
		            
		            maj += 1 if n == res else -1
		        
		        return res
#=====================================================================================================================================


																				"""

===============================
Python Leet-code Binary Search Question's
===============================
																				"""
#=====================================================================================================================================
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2  # Find the middle index
        if arr[mid] == target:
            return mid  # Target found, return the index
        elif arr[mid] < target:
            left = mid + 1  # Move to the right half
        else:
            right = mid - 1  # Move to the left half
    return -1  # Target not found
sorted_list = [1, 3, 5, 7, 9, 11, 13]
target = 7
result = binary_search(sorted_list, target)
if result != -1:
    print(f"Target {target} found at index {result}.")
else:
    print(f"Target {target} not found in the list.")
#=====================================================================================================================================
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
#=====================================================================================================================================
def binary_search_leftmost(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid  # Record the position
            right = mid - 1  # Keep searching left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result
#=====================================================================================================================================
def binary_search_rightmost(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid  # Record the position
            left = mid + 1  # Keep searching right
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result
#=====================================================================================================================================
#Search Insert Position
nums = [1,2,3,4]
target = 5
left = 0
right = len(nums) - 1
while left <= right:
	mid = (left+right) // 2
	if nums[mid] == target:
		print(target)
		break
	elif nums[mid] < target:
		left = mid + 1
	else:
		right = mid - 1
print(left)
#left = 0, right = 3
#mid = 1 → nums[mid] = 3 → left = mid + 1 (2)
#mid = 2 → nums[mid] = 5 → right = mid - 1 (1)
#=====================================================================================================================================
																							"""
===============================
Python Leet-code Math Question's
===============================
																							"""
#=====================================================================================================================================
#Square Root Without Built-In Functions: Isacc's Newtons approximation for real valued funcntions
x = 9
n = x
y = 1.0000000
e = 0.0000001
	while (x-y) > e:
    	x = (x+y) / 2
    	y = n / x
    return int(x)
 #With Binary Search:
 def mySqrt(self, x: int) -> int:
    left = 0
    right = x
    while left < right:
        mid = (left+right) // 2
        if mid * mid == x:
            return mid
         if mid * mid > x:
            right = mid -1
          else:
            left = mid + 1
    print(f"left: {left}")
    print(f"right: {right}")
    return left if left*left <= x else left -1
#=====================================================================================================================================
#Climbing Stairs Distinct 1 or 2 Step
#My attempt with Fibonacci Sequences halts at n = 45 => because fib is 2^n
#A recursive approach is the worst, second best memorization (DP) and iterative (DP) with space complexity in the latter being O(1) being best
class Solution:
    def fib(self, n: int) -> int:
        if n <=1:
            return n
        else:
            return self.fib(n-1) + self.fib(n-2)

    def climbStairs(self, n: int) -> int:
        return self.fib(n + 1)
#A better solution: prev2 represents the number of ways to climb 0 stairs (f(0) = 1).
#prev1 represents the number of ways to climb 1 stair (f(1) = 1).
"""
Start at i = 2
Why 2? Because f(0) and f(1) are already known.
Core Logic:
f(n)=f(n−1)+f(n−2)
current = prev1 + prev2: The current number of ways is the sum of the previous two numbers.
Update Variables:
prev2 = prev1: Shift prev2 to the previous prev1.
prev1 = current: Update prev1 to the current value.
This shifting allows us to save space instead of using an array to store all Fibonacci numbers.
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 1
        prev2 = 1  # f(0)
        prev1 = 1  # f(1)
        for i in range(2, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
        return prev1
#=====================================================================================================================================
																				"""
===============================
Python Leet-code Linked List Question's
===============================
																				"""
#=====================================================================================================================================
#Remove Duplicates, tranversing and missing automatically deletes it
class ListNode:
     def __init__(self, val=0, next=None):
       self.val = val
       self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        c = head 
        while c and c.next:
            if c.val == c.next.val:
                c.next = c.next.next
            else:
                c = c.next
        return head
#=============================================================================================================================
#Add Two numbers Linked-List: I need to review this because it does not work.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode(0)
        current = l3
        c = 0 
        while l1 or l2 or c:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            total = a + b + c
            c, digit = divmod(total, 10)
            current.next = ListNode(digit)
            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return l3.next
#=====================================================================================================================================

																		"""

===============================
Python Leet-code String Question's
===============================
																		"""


#=====================================================================================================================================
#Longest Substring Without Repeating Characters
from itertools import combinations
s = "abcabcabb"
res = [s[x:y] for x, y in combinations(range(len(s)+ 1), r = 2)]
print("All sub-strings:", res)
#Note the dumb O(n^3) solution, and not reading the question properly, we're only returning unique character len ints => O(n) with sliding window
def length_of_longest_substring(s: str) -> int:
    char_set = set()    # Track distinct characters in the current window
    max_len = 0
    start = 0
    for end in range(len(s)):
        # If the character s[end] is already in the set,
        # move the start pointer until that duplicate is removed
        while s[end] in char_set:
            char_set.remove(s[start])
            start += 1        
        # Add the new character and update max_len
        char_set.add(s[end])
        max_len = max(max_len, end - start + 1)
    return max_len
# Example Usage:
s = "abcabcabb"
result = length_of_longest_substring(s)
print("Longest substring length with distinct characters:", result)




