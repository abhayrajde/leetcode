class Solution(object):
    def removeDuplicates(self, s, k):
        stack = []
        for i in range(len(s)):
            if stack and stack[-1][0] == s[i]:
                stack.append((s[i], stack[-1][1] + 1))
                if stack[-1][1] == k:
                    for _ in range(k):
                        stack.pop()
                        
            else:
                stack.append((s[i], 1))
        res = ""
        for i in stack:
            res+=i[0]
        return res
    
    
    
    def candycrush(s):
        stack = []
        for i in range(len(s)):

            # check the occurance of the element
            if stack and stack[-1][0] != s[i] and stack[-1][1] >= 3:
                for _ in range(stack[-1][1]):
                    stack.pop()

            # if same element append the element and prev_count +1 in the stack
            if stack and stack[-1][0] == s[i]:
                stack.append((s[i], stack[-1][1] + 1))

            #this element is new so append element and count = 1
            else:
                stack.append((s[i],1))

        # in the end if the last element on the stack has occurance more then 3 then remove it
        if stack[-1][1]>=3:
            for _ in range(stack[-1][1]):
                stack.pop()
        res = ""
        for i in stack:
            res+=i[0]
        return res

    # result = candycrush("baaabbcd")
    # print(result)
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        