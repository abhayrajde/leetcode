class Solution(object):
    
    
    def invalidTransactions(self, transactions):
        transaction_map = defaultdict(set)

        invalid = []
        for transaction in transactions:
            name, time, amount, city = transaction.split(",")
            time = int(time)            
            transaction_map[(time, name)].add(city)


        for transaction in transactions:
            name, time, amount, city = transaction.split(",")
            time = int(time)
            amount = int(amount)

            if amount > 1000:
                invalid.append(transaction)
                continue

            # check to see if there is a time within 60 minutes of this transaction
            for time in range(time-60, time+61):
                if (time, name) not in transaction_map:
                    continue
                sus_transaction = transaction_map[(time, name)]

                # check to see if there is another transaction from a diff city if so its invalid
                if city in sus_transaction:
                    sus_transaction.remove(city)
                    if len(sus_transaction) >= 1:
                        invalid.append(transaction)
                        break
                    sus_transaction.add(city)
                else:
                    invalid.append(transaction)
                    break

        return invalid 
#     def time_error(self,):
#         return
    
    
    
#     def amount_error(self, t_amount):
#         if t_amount > 1000:
#             return True
#         return False
        
        
#     def invalidTransactions(self, transactions):
#         t_dict = defaultdict(list)
#         invalid = []
#         for i,trans in enumerate(transactions):
#             name, time, amount, city = list(trans.split(","))
#             time = int(time)
#             amount = int(amount)
            
#             #Amount Error check
#             if self.amount_error(amount):
#                 invalid.append(trans)
                
            
#             #Time Error Check
#             if t_dict[name]:
#                 check = False
#                 for j, t2 in enumerate(t_dict[name]):
#                     if t2[0] in range(time-60, time+61):
#                         if city != t2[1]:
#                             check = True
#                             invalid.append(transactions[t2[-1]])
#                             # del t_dict[name][j]
                            
#                 if check:
#                     invalid.append(trans)
#             t_dict[name].append([time, city, i])
            
            
#         # print(t_dict)
#         return invalid
        
            
                
    

        
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        