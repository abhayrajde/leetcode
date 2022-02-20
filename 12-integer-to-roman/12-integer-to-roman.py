class Solution(object):
    def intToRoman(self, num):
        nums = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        rom = ["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
        i = 12
        op = ""
        while(num!=0):
            if(nums[i]<=num):
                op += rom[i]
                num -= nums[i]
            else:
                i-=1
        return(op)
        
        """
        :type num: int
        :rtype: str
        """
        