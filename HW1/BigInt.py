from operator import add
class BigInt():
    def __init__(self,num,node_size=1):
        #convert list of string into list of int
        self.list = list(map(int,num))

    def add(self, other):
        if isinstance(other, BigInt):
            return self.__add_bigint(other)
        else:
            raise ValueError('Cannot add BigInt and %s' % (BigInt))

    def __add_bigint(self,list2):
        diff = abs(len(list2.list)-len(self.list))

        # diferentiate the longer list than the smaller list
        smallerList,longerList = (list2.list,self.list) if len(list2.list)<len(self.list) else (self.list,list2.list)
        smallerList = [0]*diff +smallerList

        self.list= list(map(add,smallerList,longerList))

        for i in reversed(range(1,len(self.list))):
            if self.list[i]>9:
                self.list[i] -=10
                self.list[i-1] +=1

        if self.list[0]>9:
            self.list[0]-=10
            self.list = [1]+self.list
        
        return self


    def multiply(self,list2):
        sum_lists = []
        # diferentiate the longer list than the smaller list
        smallerList,longerList = (list2.list,self.list) if len(list2.list)<len(self.list) else (self.list,list2.list)

        multiplier = 0
        for i in reversed(range(len(smallerList))):
            new_list = []
            carry = 0
            for j in reversed(range(len(longerList))):
                numToAdd=(smallerList[i] * longerList[j])+ carry
                carry = numToAdd//10
                new_list.append(numToAdd%10)
            if carry > 0:
                new_list.append(carry)
            new_list.reverse()
            sum_lists.append(new_list+ [0] * multiplier)

            multiplier+=1
        self.list = sum_lists[0]

        for l in sum_lists[1:]:
            self.add(BigInt(l))

        return self

    def __repr__(self):
        return ''.join(list(map(str,self.list)))