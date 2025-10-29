from os import remove


class MyArrayList:
    INIT_CAP = 1
    def __init__(self, init_capacity = None):
        self.data = [None] * (init_capacity if init_capacity is not None else self.INIT_CAP)
        self.size = 0
    # add to the last 
    def add_last(self, e):
        cap = len(self.data)
        # check whether the capacity is enough
        if self.size == cap:
            self._resize(2*cap)
        self.data[self.size] = e
        self.size +=1

    # add to the index
    def add(self,index,e):
        self._check_position_index(index)
        cap = len(self.data)
        if self.size == cap:
            self._resize(2 * cap)
        for i in range(self.size-1, index-1, -1):
            self.data[i+1] = self.data[i]
        self.data[index] = e
        self.size +=1

    def add_first(self, e):
        self.add(0,e)

    def remove_last(self):
        if self.size == 0:
            raise Exception("NoSuchElementException")
        cap = len(self.data)
        if self.size == cap // 4:
            self._resize(cap//2)

        deleted_val = self.data[self.size-1]
        self.data[self.size-1] = None
        self.size -= 1
        return deleted_val
    
    def remove(self,index):
        self._check_element_index(index)
        cap = len(self.data)
        if self.size == cap//4:
            self._resize(cap//2)
        deleted_val = self.data[index]

        for i in range(index+1, self.size):
            self.data[i-1] = self.data[i]
        self.data[self.size-1]=None
        self.size -= 1
        return deleted_val
    
    def remove_first(self):
        return remove(0)
    
    def get(self,index):
        self._check_element_index(index)
        return self.data[index]
    
    def set(self,index,element):
        self._check_element_index(index)
        old_val = self.data[index]
        self.data[index] = element
        return old_val
    
     # util functionalities
    def _resize(self, new_cap):
        temp = [None] * new_cap
        for i in range(self.size):
            temp[i] = self.data[i]
        self.data = temp

    def _is_element_index(self, index):
        return 0<= index < self.size
    
    def _is_position_index(self, index):
        return 0<= index <= self.size

    def _check_position_index(self, index):
        if not self._is_position_index(index):
            raise IndexError(f"Index:{index}, Size:{self.size}")
    
    def _check_element_index(self, index):
        if not self._is_position_index(index):
            raise IndexError(f"Index:{index}, Size:{self.size}")
    
    def display(self):
        print(f"size={self.size}, cap = {len(self.data)}")
        print(self.data)
    
    

        
