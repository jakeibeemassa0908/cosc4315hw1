from operator import add
class BigInt():
    def __init__(self,num,node_size=1):
        #convert list of string into list of int
        self.list = list(map(int,num))

    def add(self,list2):
        diff = abs(len(list2.list)-len(self.list))

        # diferentiate the longer list than the smaller list
        smallerList,longer_list = (list2.list,self.list) if len(list2.list)<len(self.list) else (self.list,list2.list)
        smallerList = [0]*diff +smallerList

        self.list= list(map(add,smallerList,longer_list))

        for i in reversed(range(1,len(self.list))):
            if self.list[i]>9:
                self.list[i] -=10
                self.list[i-1] +=1

        if self.list[0]>9:
            self.list[0]-=10
            self.list = [1]+self.list
        
        return self


    def mutliply(self):
        return null

    def __repr__(self):
        return ''.join(list(map(str,self.list)))

    
