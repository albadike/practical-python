# portfolio.py

class Portfolio:
    # stock_holdings is a list of Stock objects
    def __init__(self, stock_holdings):
        self._stock_holdings = stock_holdings       # Why is self.stock_holdings causing an error? 

    def __iter__(self):
        return self._stock_holdings.__iter__()

    def __len__(self):
        return len(self._stock_holdings)

    def __getitem__(self, index):
        return self._stock_holdings[index]

    def __contains__(self, name):
        # 'return name in self._stock_holdings' does not work for objects that are not hashable
        return any(stock_obj.name == name for stock_obj in self._stock_holdings)    

    @property
    def total_cost(self):
        return sum(stock_obj.cost for stock_obj in self._stock_holdings)  # notice _total_cost is not included in __init__, yet still works

    def tabulate_shares(self):
        from collections import Counter
        shares_counter_dict = Counter()
        for stock_obj in self._stock_holdings:
            shares_counter_dict[stock_obj.name] += stock_obj.shares
        
        # print(f"\nTotal Shares: {shares_counter_dict}")
        # for name, shares in shares_counter_dict.items():
        #     print(f"{name}: {shares}")
        
        return shares_counter_dict