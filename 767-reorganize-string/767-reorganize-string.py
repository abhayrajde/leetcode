class Solution(object):
    def reorganizeString(self, s):
        hm = collections.Counter(s)
        
        # for i in s:
        #     hm[i]+=1
        print hm
        heap = [(-value,letter) for letter, value in hm.items()]
        
        heapq.heapify(heap)
        
        res = []
        
        while(len(heap)>=2):
            
            top_count, top_letter = heapq.heappop(heap)
            next_count, next_letter = heapq.heappop(heap)
            
            res.append(top_letter)
            res.append(next_letter)
            
            if(top_count + 1):
                heapq.heappush(heap, (top_count+1, top_letter))
            
            if(next_count + 1):
                heapq.heappush(heap, (next_count+1, next_letter))
            
        if heap:
            top_count, top_letter = heapq.heappop(heap)
            
            if top_count != -1 or (res and top_letter == res[-1]):
                return ""
            else:
                res.append(top_letter)
        return "".join(res)
        """
        :type s: str
        :rtype: str
        """
        