class Solution(object):
    def leastInterval(self, tasks, n):
        # print(tasks)
        count = {}
        for i in range(len(tasks)):
            if(tasks[i] not in count):
                count[tasks[i]] = 0
            count[tasks[i]]+=1
        # print(count)
        
        # maxheap = []
        # for i in range(len(count)):
        #     maxheap.apppend(-(count[i]))
        maxheap = [-cnt for cnt in count.values()]
        # print(maxheap)
        heapq.heapify(maxheap)
        # print(maxheap)
        
        time = 0 
        q = deque()     #pair of values[-cnt, idleTime(time at which the value it will be available to add to q)]
        
        while(maxheap or q):
            time+=1
            
            if(maxheap):
                cnt = 1 + heapq.heappop(maxheap)
                if(cnt):
                    q.append([cnt, time+n])
                
            if(q and q[0][1] == time):
                heapq.heappush(maxheap, q.popleft()[0])
        return(time)
                    
        
        
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        