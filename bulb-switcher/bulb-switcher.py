import math
class Solution(object):
    def bulbSwitch(self, n):
        # we will consider 0 = off and 1 = on
        #We will create one list of initial state where all the bulbes are off
        #for the second round we will keep even nos. on and odd no. off(bec index start from 0)
        '''
        if(n == 0):
            return 0
        elif(n == 1):
            return(1)
        else:
            # Initial state
            list1 = []
            for i in range(n):
                list1.append(0)

            # SECOND ROUND
            count = 0
            if(n>=2):
                for i in range(0,n,2):
                    list1[i] = 1
                    count+=1


            # ONWARDS 3RD ROUND
            if(n>=3):
                # rem_rounds = n-2
                for i in range(2,n):
                    for j in range(i,n,i+1):
                        if(list1[j]==0):
                            list1[j]=1
                            count+=1
                        else:
                            list1[j]=0
                            count-=1

            # count = 0
            # for i in list1:
            #     if(i == 1):
            #         count+=1
            return count
        '''
        # THE ABOVE CODE IS RUNNING COMPLETELY FINE BUT TIME LIMIT IS EXCEEDING
        
        # SECOND SOLUTION
        return(int(sqrt(n)))
        """
        :type n: int
        :rtype: int
        """