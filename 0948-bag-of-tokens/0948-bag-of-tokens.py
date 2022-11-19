class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        
        start = 0
        end = len(tokens) - 1
        tokens = sorted(tokens)
        # print(tokens)
        
        score = 0
        while(start <= end):
            if power >= tokens[start]:
                power = power - tokens[start]
                start += 1
                score += 1
                
            elif score and start != end:
                power += tokens[end]
                end -= 1
                score -= 1
            # print(score)
            else:
                break
        return score
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """
        