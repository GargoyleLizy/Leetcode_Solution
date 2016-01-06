class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        
        queue = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        
        self.queue.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        
        back_up = []
        while self.queue != []:
            back_up.append(self.queue.pop())
        ans = back_up.pop()
        
        while back_up != []:
            self.queue.append(back_up.pop())
        return 


    def peek(self):
        """
        :rtype: int
        """
        
         back_up = []
        while self.queue != []:
            back_up.append(self.queue.pop())
        ans = back_up.pop()
        back_up.append(ans)
        
        while back_up != []:
            self.queue.append(back_up.pop())
        
        return ans
            
        

    def empty(self):
        """
        :rtype: bool
        """
        return self.queue==[]
