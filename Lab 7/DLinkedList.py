class DLinkedListNode:
    # An instance of this class represents a node in Doubly-Linked List
    def __init__(self,initData,initNext,initPrevious):
        self.data = initData
        self.next = initNext
        self.previous = initPrevious
        
        if initNext != None:
            self.next.previous = self
        if initPrevious != None:
            self.previous.next = self
            
    def getData(self):
        return self.data
    
    def setData(self,newData):
        self.data = newData
        
    def getNext(self):
        return self.next
    
    def getPrevious(self):
        return self.previous
    
    def setNext(self,newNext):
        self.next = newNext
        
    def setPrevious(self,newPrevious):
        self.previous = newPrevious


class DLinkedList:
	# An instance of this class represents the Doubly-Linked List
	def __init__(self):
		# Constructor that takes no arguments and creates an empty list
		self.__head = None
		self.__tail = None
		self.__size= 0        

	def search(self, item):
		current = self.__head
		found = False
		while current != None and not found:
			if current.getData() == item: 
				found= True
			else: 
				current = current.getNext()
		return found

	def index(self, item):
		current = self.__head
		found = False
		index = 0
		while current != None and not found:
			if current.getData() == item:
				found= True
			else:
				current = current.getNext()
				index = index + 1
		if not found: 
			index = -1
		return index    
  
	def add(self, item):
		node = DLinkedListNode(item, self.__head, None)
		if self.__head != None:
			self.__head.setPrevious(node)
		else: 
			self.__tail = node
		self.__head = node 
		self.__size += 1
		
	def remove(self, item):
		current = self.__head
		while current.getData() != item and current is not None:
			current = current.getNext()
		if current is not None:
			if current == self.__head:
				self.__head = self.__head.getNext() 
				if self.__head is not None: 
					self.__head.setPrevious(None) 
				else: 
					self.__tail = None
			elif current == self.__tail:
				self.__tail = self.__tail.getPrevious() 
				self.__tail.setNext(None) 
			else: 
				current.getPrevious().setNext(current.getNext())
				current.getNext().setPrevious(current.getPrevious())
			current.setNext(None)
			current.setPrevious(None) 
			self.__size -= 1
				
	def append(self, item):
		node = DLinkedListNode(item, None, None)
		if self.__head == None:
			self.__head = node
		else:
			self.__tail.setNext(node) 
			node.setPrevious(self.__tail)
		self.__tail = node 
		self.__size += 1
		
	def insert(self, pos, item):
		if pos == 0:
			self.add(item)
		elif pos == self.__size:
			self.append(item)
		else:
			current = self.__head
			index = 0
			while current != None and index != pos:
				current = current.getNext()
				index = index + 1
			if index == pos:
				node = DLinkedListNode(item, None, None)
				node.setNext(current)
				node.setPrevious(current.getPrevious())
				current.getPrevious().setNext(node)
				current.setPrevious(node)
				self.__size += 1
	
	def pop1(self):
		if self.__size == 0: 
			return None
		if self.__size == 1: 
			element = self.__head.getData()
			self.__head = self.__tail = None
			self.__size = 0 
			return element
		element = self.__tail.getData()
		self.__tail = self.__tail.getPrevious()
		self.__tail.setNext(None)
		self.__size	-= 1
		return element 

	def pop(self, pos=None):
		if pos is None:
			return self.pop1()
		if pos < 0 or pos >= self.__size:
			raise Exception("Position not in range.")
		if pos == 0: 
			element = self.__head.getData()
			self.__head = self.__head.getNext() 
			if self.__head == None: 
				self.__tail = None
			else:
				self.__head.setPrevious(None)
			self.__size -= 1
			return element
		elif pos == self.__size	- 1:
			return self.pop1()
		current = self.__head
		index = 0
		while current != None and index != pos:
			current = current.getNext()
			index += 1
		element = current.getData()
		current.getPrevious().setNext(current.getNext())
		current.getNext().setPrevious(current.getPrevious())
		current.setNext(None)
		current.setPrevious(None)
		self.__size -= 1
		return element
			
	def searchLarger(self, item):
		current = self.__head
		index = 0
		while current != None and current.getData() <= item:
			current = current.getNext()
			index = index + 1
		if current is None:
			index = -1
		return index
		
	def getSize(self):
		return self.__size
	
	def getItem(self, pos):
		if pos >= 0:
			index = 0
			current = self.__head 
			while current != None and index != pos:
				current = current.getNext()
				index += 1
			if current is not None: 
				return current.getData()
			else:
				raise Exception("Position not in range.")	
		else:
			index = -1 
			current = self.__tail 
			while current != None and index != pos:
				current = current.getPrevious()
				index -= 1
			if current is not None:
				return current.getData()
			else: 
				raise Exception("Position not in range.")
	
	def __str__(self):
		if self.__size == 0: 
			return ""
		current = self.__head 
		nodeList = "" 
		while current.getNext() is not None:
			nodeList = nodeList + "{} ".format(current.getData())
			current = current.getNext()
		nodeList = nodeList + "{}".format(current.getData())
		return nodeList

def test():
                  
    linked_list = DLinkedList()
                    
    is_pass = (linked_list.getSize() == 0)
    assert is_pass == True, "fail the test"
            
    linked_list.add("World")
    linked_list.add("Hello")    
        
    is_pass = (str(linked_list) == "Hello World")
    assert is_pass == True, "fail the test"
              
    is_pass = (linked_list.getSize() == 2)
    assert is_pass == True, "fail the test"
            
    is_pass = (linked_list.getItem(0) == "Hello")
    assert is_pass == True, "fail the test"
        
        
    is_pass = (linked_list.getItem(1) == "World")
    assert is_pass == True, "fail the test"    
            
    is_pass = (linked_list.getItem(0) == "Hello" and linked_list.getSize() == 2)
    assert is_pass == True, "fail the test"
            
    is_pass = (linked_list.pop(1) == "World")
    assert is_pass == True, "fail the test"     
            
    is_pass = (linked_list.pop() == "Hello")
    assert is_pass == True, "fail the test"     
            
    is_pass = (linked_list.getSize() == 0)
    assert is_pass == True, "fail the test" 
                    
    int_list2 = DLinkedList()
                    
    for i in range(0, 10):
        int_list2.add(i)      
    int_list2.remove(1)
    int_list2.remove(3)
    int_list2.remove(2)
    int_list2.remove(0)
    is_pass = (str(int_list2) == "9 8 7 6 5 4")
    assert is_pass == True, "fail the test"
                
    for i in range(11, 13):
        int_list2.append(i)
    is_pass = (str(int_list2) == "9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"
                
    for i in range(21, 23):
        int_list2.insert(0,i)
    is_pass = (str(int_list2) == "22 21 9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"
                
    is_pass = (int_list2.getSize() == 10)
    assert is_pass == True, "fail the test"    
                    
    int_list = DLinkedList()
                    
    is_pass = (int_list.getSize() == 0)
    assert is_pass == True, "fail the test"                   
                    
    for i in range(0, 1000):
        int_list.append(i)      
    correctOrder = True
            
    is_pass = (int_list.getSize() == 1000)
    assert is_pass == True, "fail the test"            
            
        
    for i in range(0, 200):
        if int_list.pop() != 999 - i:
            correctOrder = False
                            
    is_pass = correctOrder
    assert is_pass == True, "fail the test" 
            
    is_pass = (int_list.searchLarger(200) == 201)
    assert is_pass == True, "fail the test" 
            
    int_list.insert(7,801)   
        
    is_pass = (int_list.searchLarger(800) == 7)
    assert is_pass == True, "fail the test"
            
            
    is_pass = (int_list.getItem(-1) == 799)
    assert is_pass == True, "fail the test"
            
    is_pass = (int_list.getItem(-4) == 796)
    assert is_pass == True, "fail the test"
                    
    if is_pass == True:
        print ("=========== Congratulations! Your have finished exercise 2! ============")

                
if __name__ == '__main__':
    test()
