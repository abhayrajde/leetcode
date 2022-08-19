class Solution(object):
    def suggestedProducts(self, products, searchWord):
        res = []
        products.sort()
        l = 0
        r = len(products)-1
        
        for i in range(len(searchWord)):
            curr = searchWord[i]
            
            while(l<=r and (len(products[l]) <= i or products[l][i] != curr)):
                l+=1
            
            while(l<=r and (len(products[r]) <= i or products[r][i] != curr)):
                r-=1
                
            res.append([])
            
            remain = r-l+1
            
            for j in range(min(3,remain)):
                res[-1].append(products[l + j])
        return res
                
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        