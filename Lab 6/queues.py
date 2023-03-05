class BoundedQueue: 
    # Creates a new empty queue:
    def __init__(self, capacity): 
        assert isinstance(capacity, int), ('Error: Type error: %s' % (type(capacity))) # throws an assertion error on not true
        assert capacity >= 0, ('Error: Illegal capacity: %d' % (capacity))
        self.__items = [] # init the list/queue as empty
        self.__capacity = capacity
 
    # Adds a new item to the back of the queue, and returns nothing:
    def enqueue(self, item):
        if self.__size == self.__capacity:
            raise Exception('Error: Queue is full')
        self.__back = (self.__back + 1) % self.__capacity
        self.__items.insert(self.__back, item)
        self.__size += 1

        
    # Removes and returns the front-most item in the queue.      
    # Returns nothing if the queue is empty.    
    def dequeue(self):        
        '''
        Dequeue the element from the front of the queue and return it
        :return: The object that was dequeued
        '''
        if self.isEmpty():
            raise Exception('Error: Queue is empty')
        return self.__items.pop(0)
    
    # Returns the front-most item in the queue, and DOES NOT change the queue.      
    def peek(self):        
        if len(self.__items) <= 0:            
            raise Exception('Error: Queue is empty')        
        return self.__items[0]
        
    # Returns True if the queue is empty, and False otherwise:    
    def isEmpty(self):
        return len(self.__items) == 0        
    
    # Returns True if the queue is full, and False otherwise:    
    def is_full(self):
        return len(self.__items) == self.__capacity
    
    # Returns the number of items in the queue:    
    def size(self):        
        return len(self.__items)        
    
    # Returns the capacity of the queue:    
    def capacity(self):        
        return self.__capacity
    
    # Removes all items from the queue, and sets the size to 0    
    # clear() should not change the capacity    
    def clear(self):        
        self.__items = []

class CircularQueue:
    # Creates a new empty circular queue:
    def __init__(self, capacity):
        assert isinstance(capacity, int), ('Error: Type error: %s' % (type(capacity))) # throws an assertion error on not true
        assert capacity >= 0, ('Error: Illegal capacity: %d' % (capacity))
        self.__items = []
        self.__capacity = capacity
        self.__size = 0
        self.__front = 0
        self.__back = -1
        
    # Adds a new item to the back of the queue:
    def enqueue(self, item):
        if self.__size == self.__capacity:
            raise Exception('Error: Queue is full')
        self.__back = (self.__back + 1) % self.__capacity
        self.__items.insert(self.__back, item)
        self.__size += 1
        
    # Removes and returns the front-most item in the queue.      
    # Returns nothing if the queue is empty.    
    def dequeue(self):
        if self.__size == 0:
            return None
        item = self.__items[self.__front]
        self.__front = (self.__front + 1) % self.__capacity
        self.__size -= 1
        return item
    def peek(self):        
        if self.__count == 0:            
            raise Exception('Error: Queue is empty')        
        
        return self.__items[self.__head]
    
    # Returns True if the queue is empty, and False otherwise:    
    def isEmpty(self):
        return self.__count == 0        
    
    # Returns True if the queue is full, and False otherwise:    
    def isFull(self):
        return self.__count == self.__capacity
    
    # Returns the number of items in the queue:    
    def size(self):        
        return self.__count        
    
    # Returns the capacity of the queue:    
    def capacity(self):        
        return self.__capacity
    
    # Removes all items from the queue, and sets the size to 0    
    # clear() should not change the capacity    
    def clear(self):        
        self.__items = []
        self.__count = 0
        self.__head = 0
        self.__tail = 0
    
    # Returns a string representation of the queue: 
    def __str__(self):               
        str_exp = "]"        
        i = self.__head
        for j in range(self.__count):            
            str_exp += str(self.__items[i]) + " "
            i = (i+1) % self.__capacity
        return str_exp + "]"
        
    # Returns a string representation of the object CircularQueue    
    def __repr__(self):        
        return str(self.__items) + " H= " + str(self.__head) + " T="+str(self.__tail) + " (" +str(self.__count)+"/"+str(self.__capacity)+")"  
 
 
 
def main():
    # Test bounded queue creation
    bq=BoundedQueue(3)
    print("My bounded queue is:", bq)
    print(repr(bq))
    print("Is my bounded queue empty?", bq.isEmpty())
    print('----------------------------------')
    

    # 1. To Do
    # Test when we try to dequeue from an EMPTY queue
    try:
        bq.dequeue()
    except Exception as dequeueError:
        print("Test 1: Dequeue from empty queue - Passed")
        print(dequeueError)

    print('----------------------------------')

    

    # 2. To Do
    # Test adding one element to queue
    
    # Your test code goes here...
    
    bq.enqueue("john")
    print("Test 2: Add one element to queue - Passed")
    print(bq)
    print(str(bq))
    print("Is my bounded queue empty?", bq.isEmpty())
    print('----------------------------------')

    

    # 3. Uncomment and run
    # Test adding more elements to queue
    bq.enqueue("eva")
    bq.enqueue("paul")
    print(repr(bq))
    print("Is my bounded queue full?", bq.isFull())
    print("There are", bq.size(), "elements in my bounded queue.")
    print('----------------------------------')

 

    # 4. To Do
    # Test trying to add an element to a FULL queue
    
    # Your test code goes here...hint: look at dequeuing from EMPTY queue
    bq.enqueue("eva")
    bq.enqueue("paul")
    try:
        bq.enqueue("jane")
    except Exception as enqueueError:
        print("Test 4: Add element to full queue - Passed")
        print(enqueueError)

    print('----------------------------------')


    # 5. Uncomment and run
    # Test removing element from full queue
    item = bq.dequeue()
    print(repr(bq))
    print(item,"was first in the bounded queue:", bq)
    print("There are", bq.size(), "elements in my bounded queue.")
    print('----------------------------------')

    

    # 6. Uncomment and run
    # Test capacity of queue
    print("Total capacity is:", bq.capacity())


    # 7. To Do: Uncomment print statements, one at a time
    # Can we just access private capacity attribute directly outside of Class definition?
    try:
        print(bq.capacity)
    except Exception as accessError:
        print("Test 7: Accessing private capacity attribute - Passed")
        print(accessError)


    
if __name__ == '__main__':
    main()
