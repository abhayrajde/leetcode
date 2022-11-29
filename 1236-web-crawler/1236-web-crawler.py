# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution(object):
#     def crawl(self, startUrl, htmlParser):
#         visited = set(startUrl)
#         start_link = startUrl[7:]
#         start_link = start_link.split("/")
#         hostname = start_link[0]
#         hostname_len = len(hostname)
#         # hostname = startUrl.split("http://")[1].split("/")[0]
#         res = [startUrl]
        
#         q = collections.deque([startUrl])
#         while q:
#             for _ in range(len(q)):
#                 links = htmlParser.getUrls(q.popleft())
#                 for i in links:
#                     if i in visited:
#                         continue
#                     if (i[:7+hostname_len] != startUrl[:7+hostname_len]):
#                         continue
#                     q.append(i)
#                     res.append(i)
#                     visited.add(i)
#         return res
            
        
    def crawl(self, startUrl, htmlParser):
        visited = {startUrl}
        domain = startUrl.split("http://")[1].split("/")[0]
        ans = [startUrl]
        queue = collections.deque([startUrl])
        while queue:
            for _ in range(len(queue)):
                url = queue.popleft()
                check = htmlParser.getUrls(url)
                for new_url in check:
                    if new_url in visited:
                        continue
                    if new_url.split("http://")[1].split("/")[0] != domain:
                        continue
                    ans.append(new_url)
                    visited.add(new_url)
                    queue.append(new_url)        
        return ans
            
        """
        :type startUrl: str
        :type htmlParser: HtmlParser
        :rtype: List[str]
        """
        