class Solution(object):
    def knightDialer(self, n):
#         dir_map = {1:[6,8], 2:[7,9], 3:[4,8], 4:[0,3,9], 5:[], 6:[7,1,0], 7:[2,6], 8:[1,3], 9:[4,2], 0:[4,6]}
        
#         count = 0
        
#         q = deque()
#         for i in range(10):
#             q.append([i,[i]])
        
#         while(q):
#             curr, curr_path = q.popleft()
#             if len(curr_path) == n:
#                 count+=1    
#             else:
#                 for i in dir_map[curr]:
#                     q.append([i,curr_path+[i]])
#         return count % (10**9 + 7)
    
        # Neighbors maps K: starting_key -> V: list of possible destination_keys
        neighbors = {
            0:(4,6),
            1:(6,8),
            2:(7,9),
            3:(4,8),
            4:(0,3,9),
            5:(),
            6:(0,1,7),
            7:(2,6),
            8:(1,3),
            9:(2,4)
        }
        current_counts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        for _ in range(n-1):
            next_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for src_key in range(10):
                for dst_key in neighbors[src_key]:
                    next_counts[dst_key] = (next_counts[dst_key] + current_counts[src_key]) % (10**9 + 7)
            current_counts = next_counts
        return sum(current_counts) % (10**9 + 7)
                
        """
        :type n: int
        :rtype: int
        """
        