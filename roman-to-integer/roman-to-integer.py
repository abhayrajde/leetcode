class Solution(object):
    def romanToInt(self, s):
        count = 0
        # Here we are calculating till secondlast element, will add last element later
        for i in range(len(s)-1):
            
            if(s[i] == 'I'):
                if(s[i+1] == 'V' or s[i+1] == 'X'):
                    count-=1
                else:
                    count+=1
            
            elif(s[i] == 'X'):
                if(s[i+1] == 'L' or s[i+1] == 'C'):
                    count-=10
                else:
                    count+=10
            
            elif(s[i] == 'C'):
                if(s[i+1] == 'D' or s[i+1] == 'M'):
                    count-=100
                else:
                    count+=100
            
            elif(s[i] == 'V'):
                count+=5
            elif(s[i] == 'L'):
                count+=50
            elif(s[i] == 'D'):
                count+=500
            elif(s[i] == 'M'):
                count+=1000
        # Adding for the last term
        if(s[-1] == 'I'):
            count+=1
        elif(s[-1] == 'V'):
            count+=5
        elif(s[-1] == 'X'):
            count+=10
        elif(s[-1] == 'L'):
            count+=50
        elif(s[-1] == 'C'):
            count+=100
        elif(s[-1] == 'D'):
            count+=500
        elif(s[-1] == 'M'):
            count+=1000
            
        return (count)
                       
            
        """
        for i in range (0,len(s)):
            if(s[i] == 'I'):
                count+=1
            elif(s[i] == 'V'):
                count+=5
            elif(s[i] == 'X'):
                count+=10
            elif(s[i] == 'L'):
                count+=50
            elif(s[i] == 'C'):
                count+=100
            elif(s[i] == 'D'):
                count+=500
            elif(s[i] == 'M'):
                count+=1000
        return (count)
        """
        """
        :type s: str
        :rtype: int
        """
        