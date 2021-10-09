class MyClass:

    def __init__(self):
        pass
    
    def return_max(self,args):
        self.max=0
        for i in range(0,len(args),1):
            if args[i] > self.max:
                self.max =  args[i]
        return self.max
    
    def return_min(self,args):
        self.min=0
        for i in range(0,len(args),1):
            if args[i] <= self.min:
                self.min =  args[i]
        return self.min
    
    def return_max_squared(self,args):
        self.max=0
        for i in range(0,len(args),1):
            if args[i] > self.max:
                self.max =  args[i]
            
        return self.max*self.max

    def return_length(self,args):
        return len(args)
    
    def return_positive_sum(self,args):
        self.sum=0
        for i in range(0,len(args),1):
            if args[i] > 0:
                self.sum=self.sum+args[i]
        return self.sum
        
    def return_negative_count(self,args):
        self.count=0
        for i in range(0,len(args),1):
            if args[i] < 0:
                self.count=self.count+1
        return self.count
    
#create two additional methods 

    def return_positive_count(self,args):
        self.count=0
        for i in range(0,len(args),1):
            if args[i] >= 0:
                self.count=self.count+1
        return self.count
    
    def return_average(self,args):
        self.sum=0
        self.avg=0
        for i in range(0,len(args),1):
            self.sum=self.sum+args[i]
        self.avg=self.sum / len(args)
        return self.avg
    
    

import random
#Generate 10 random numbers between -10 and 30
randomlist = random.sample(range(-10, 30), 10)

print(randomlist)

a=MyClass()
print("max value in random list")
print(a.return_max(randomlist))
print("min value in random list")
print(a.return_min(randomlist))
print("max value squared in random list")
print(a.return_max_squared(randomlist))
print("length random list")
print(a.return_length(randomlist))
print("sum all positive value in random list")
print(a.return_positive_sum(randomlist))
print("count all negative value in random list")
print(a.return_negative_count(randomlist))
print("count all positive value in random list")
print(a.return_positive_count(randomlist))
print("average value in random list")
print(a.return_average(randomlist))