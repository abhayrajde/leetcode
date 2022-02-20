class Solution(object):
    def intToRoman(self, num):
        num_list = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        rom = ["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
        i = 12
        op = ""
        while(num!=0):
            if(num_list[i]<=num):
                op += rom[i]
                num -= num_list[i]
            else:
                i-=1
        return(op)
        
        """
        :type num: int
        :rtype: str
        """
        