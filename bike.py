class Bicycle(object):
    def __init__(self, model, base_cost, qty):
        self.model = model
        # self.weight = weight
        self.cost = base_cost
        self.stock_quantity = qty
        
class Shop(object):
    def __init__(self, name, margin):
        self.name = name
        self.margin = margin
        self.profit = 0.00
    
    def reportStock(self, bikes):
        for b in bikes: 
            print "{} has {} {}s in stock.".format(self.name, b.stock_quantity, b.model)
    
    def reportProfit(self):
        print "{} has made a total of ${} in profits from sales of bicycles.".format(self.name, str(self.profit))
    
    
    def fullPrice(self, item):
        return item.cost + (item.cost * self.margin)
    
    def sellBike(self, item, cust):
        item.stock_quantity = item.stock_quantity - 1
        cust.budget = cust.budget - self.fullPrice(item)
        print "Congratulations {}!  Enjoy your new {} and get yourself some speedos with the ${} still in your bike budget!".format(cust.name, item.model, cust.budget)
        print "{} now has {} {}s remaining in stock.".format(self.name, str(item.stock_quantity), item.model)
        self.profit += item.cost * self.margin
        
    def makePitch(self, cust, bikes):
        models_in_budget = set([])
        for b in bikes:
            if self.fullPrice(b) <= cust.budget and b.stock_quantity:
                models_in_budget.add(b)
        
        print "I have {} models that fit your budget.  They are:".format(str(len(models_in_budget)))
        for b in models_in_budget:
            print "{} which is ${}.".format(b.model, str(self.fullPrice(b)))
        
        for b in models_in_budget:
            hooked = raw_input("Would you like the {} which is ${}? Type y if yes:  ".format(b.model, str(self.fullPrice(b))))
            if hooked == "y":
                self.sellBike(b, cust)
                break
            
class Customer(object):
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        
    def greet(self):
        print "Howdy!  My name is {} and I would like to buy a bike.".format(self.name)
        print "My budget is ${}".format(str(self.budget))
        print "Show me what you've got in my budget, please!"
        

    
    
    
        
        
        