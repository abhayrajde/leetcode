class Solution(object):
    def calculate(self, s):
        stack = []
        i = 0
        while i<len(s):
            cur = 0
            if(s[i].isdigit()):
                while i < len(s) and s[i].isdigit():
                    cur = cur*10 + int(s[i])
                    i+=1
                # i-=1
                if(stack and (stack[-1] == "*" or stack[-1] == "/")):
                    mid = stack.pop()
                    first = stack.pop()
                    if(mid == "*"):
                        cur = first * cur
                        # stack.append(first)
                    else:
                        cur = int(first/cur)
                        # stack.append(first)
                # i+=1
                stack.append(cur)
            elif(s[i] == "+" or s[i] == "/" or s[i] == "*" or s[i] == "-"):
                stack.append(s[i])
                i+=1
             
            elif(s[i] == " "):
                i+=1
                continue
            # print stack
            
        cur = stack.pop(0)
        while stack:
            # first = stack.pop(0)
            operator = stack.pop(0)
            second = stack.pop(0)
            if(operator == "-"):
                cur = cur-second
                # stack.insert(0,cur)
            else:
                cur = cur+second
                # stack.insert(0,cur)
        return cur
            
                
        """
        :type s: str
        :rtype: int
        """
        