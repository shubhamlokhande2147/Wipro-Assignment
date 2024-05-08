class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__top=-1

    def get_max_size(self):
        return self.__max_size

    def is_full(self):
        return self.__top == self.__max_size - 1

    def push(self,data):
        if not self.is_full():
            self.__top += 1
            self.__elements[self.__top] = data
        else:
            print("Stack Overflow! Cannot push element", data)

    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg=[]
        index=self.__top
        while(index>=0):
            msg.append(str(self.__elements[index]))
            index-=1
        msg=" ".join(msg)
        msg="Stack data(Top to Bottom): "+msg
        return msg

stack1=Stack(5)
#Push all the required element(s).
stack1.push("Shirt1")
stack1.push("Shirt1")
stack1.push("Shirt1")
stack1.push("Shirt1")
stack1.push("Shirt1")
stack1.push("Shirt1") #here, stack is full here

