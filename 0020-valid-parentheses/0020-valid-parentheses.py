# create dict where key are the closing brackets and there values are opening brackets
    # if we encounter the closing bracket and at the same time
    # if the stack is empty or the last element in the stack is not dict[curr_ele]
        #then return False
class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        dict1 = {"]":"[", "}":"{", ")":"("}
        for c in s:
            if c in dict1:
                if not stack or stack[-1] != dict1[c]:
                    return False
                    
                else:
                    stack.pop()
            else:
                stack.append(c)
                
        return (True) if not stack else False
        
    
    
# class Solution(object):
#     def isValid(self, s):
#         stack = []
#         for i in s:
#             if(i == "(" or i == "{" or i == "["):
#                 stack.insert(0,i)
#             elif(i == ")"):
#                 if(stack == []):
#                     return(False)
#                 elif(stack[0] == "("):
#                     stack.pop(0)
#                 else:
#                     return(False)
#             elif(i == "}"):
#                 if(stack == []):
#                     return(False)
#                 elif(stack[0] == "{"):
#                     stack.pop(0)
#                 else:
#                     return(False)
#             elif(i == "]"):
#                 if(stack == []):
#                     return(False)
#                 elif(stack[0] == "["):
#                     stack.pop(0)
#                 else:
#                     return(False)
#         if(stack == []):
#             return(True)
#         else:
#             return(False)
            
                
#         """
#         :type s: str
#         :rtype: bool
#         """
        