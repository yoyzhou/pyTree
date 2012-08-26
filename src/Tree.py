'''
pyTree

Created on Aug 21, 2012

@author: yoyzhou
'''
import collections

(S,T) = range(2)

 
class Tree(object):
    '''
        A Python implementation of Tree data structure 
    '''
    
     
    def __init__(self, data = None, children = None):
        '''
        @param data: content of this node
        @param children: sub node(s) of Tree, could be None, child (single) or children (multiple)
        '''
        self.data = data
        self.__children = []
        self.__parent=None  #private parent attribute
        
        if children: #construct a Tree with child or children
            if isinstance(children, Tree):
                self.__children.append(children)
                children.__parent = self 
                
            elif isinstance(children, collections.Iterable):
                for child in children:
                    if isinstance(child, Tree):
                        self.__children.append(child)
                        child.__parent = self
                    else:
                        raise TypeError('Child of Tree should be a Tree type.')      
            else:
                raise TypeError('Child of Tree should be a Tree type')
    
    
    def __setattr__(self, name, value):
        
            
        """
            Hide the __parent and __children attribute from using dot assignment.
            To add __children, please use addChild or addChildren method; And
            node's parent isn't assignable
        """
            
        if name in ('parent', '__parent', 'children'):
                raise AttributeError("To add children, please use addChild or addChildren method.")
        else:
            super().__setattr__(name, value)
            
    def __str__(self, *args, **kwargs):
        
        return self.data.__str__(*args, **kwargs)

    def addChild(self, child):
        """
            Add one single child node to current node
        """
        if isinstance(child, Tree):
                self.__children.append(child)
                child.__parent = self
        else:
                raise TypeError('Child of Tree should be a Tree type')
            
    def addChildren(self, children):
        """
            Add multiple child nodes to current node
        """
        if isinstance(children, list):
                for child in children:
                    if isinstance(child, Tree):
                        self.__children.append(child)
                        child.__parent = self
                    else:
                        raise TypeError('Child of Tree should be a Tree type.')      
         
         
    def getParent(self):
        """
            Get node's parent node.
        """
        return self.__parent
    
    def getChild(self, index):
        """  
            Get node's No. index child node.
            @param index: Which child node to get in children list, starts with 0 to number of children - 1
            @return:  A Tree node presenting the number index child
            @raise IndexError: if the index is out of range 
        """
        try:
            return self.__children[index]
        except IndexError:
            raise IndexError("Index starts with 0 to number of children - 1")
        
    def getChildren(self):
        """
            Get node's all child nodes.
        """
        return self.__children
    
    
    
    def getNode(self, content):
        """
                         
            Get the first matching item(including self) whose data is equal to content. 
            Method uses data == content to determine whether a node's data equals to content, note if your node's data is 
            self defined class, overriding object's __eq__ might be required.
            Implement Tree travel (level first) algorithm using queue

            @param content: node's content to be searched 
            @return: Return node which contains the same data as parameter content, return None if no such node
        """
        nodesQ = [self]
        
        while nodesQ:
            child = nodesQ[0]
            if child.data == content:
                return child
            else:
                nodesQ.extend(child.getChildren())
                del nodesQ[0]
                
    def delChild(self, index):
        """  
            Delete node's No. index child node.
            @param index: Which child node to delete in children list, starts with 0 to number of children - 1
            @raise IndexError: if the index is out of range 
        """
        try:
            del self.__children[index]
        except IndexError:
            raise IndexError("Index starts with 0 to number of children - 1")
    
    def delNode(self, content):
         
        """
                         
            Delete the first matching item(including self) whose data is equal to content. 
            Method uses data == content to determine whether a node's data equals to content, note if your node's data is 
            self defined class, overriding object's __eq__ might be required.
            Implement Tree travel (level first) algorithm using queue

            @param content: node's content to be searched 
        """
        
        nodesQ = [self]
        
        while nodesQ:
            child = nodesQ[0]
            if child.data == content:
                if child.isRoot():
                    del self
                    return
                else:
                    parent = child.getParent()
                    parent.delChild(parent.getChildren().index(child))
                    return
            else:
                nodesQ.extend(child.getChildren())
                del nodesQ[0]
                
    def getRoot(self):
        """
            Get root of the current node.
        """
        if self.isRoot():
            return self
        else:
            return self.getParent().getRoot()
            
      
    def isRoot(self):
        """
            Determine whether node is a root node or not.
        """
        if self.__parent is None:
            return True
        else:
            return False
    
    def isBranch(self):
        """
            Determine whether node is a branch node or not.
        """
        if self.__children == []:
            return True
        else:
            return False
        
    def printTree(self, _MODE = S):
        """"
            Print tree structure with nested-list style (the default, with _MODE S) or hierarchy style, with _MODE T.
            For example:
            [0] nested-list style
                [Root[C01[C11[C111,C112]],C02,C03[C31]]]
            [1] hierarchy style
                Root
                |___ C01
                |     |___ C11
                |          |___ C111
                |          |___ C112
                |___ C02
                |___ C03
                |     |___ C31
            @param _MODE: Print style, S for Simple nested-list style; T for hierarchical Tree style
        """
        raw = '['
       
        nodesQ = [self]
        index = 0;
        
        while nodesQ:
            c_raw = '['
            child = nodesQ[0]
            if child.isRoot():
                raw += str(child.data)
                nodesQ.extend(child.getChildren())
                index = len(raw) 
            else:
                if raw.find(str(child)) != -1: #already in raw
                    nodesQ.extend(child.getChildren())
                    del nodesQ[0]
                    continue
                else:
                    parent = child.getParent()
                    index = raw.find(str(parent)) + len(str(parent))
                    nodesQ.extend(child.getChildren())
                    c_raw += str(child.data) + '['
            
            if child.getChildren() == []: 
                c_raw =  c_raw[ : -1] + ']'                 
            else:
                c_raw +=  ','.join([str(c) for c in child.getChildren()]) + ']]'
            
            raw = raw[ : index] + c_raw + raw[index: ]
            del nodesQ[0]
        
        #*************Print a Simple list representing the Tree structure************#  
        if _MODE == S:
            print(raw)
        
        #*************    Print a REAL Tree structure with parameter T   ************#   
        elif _MODE == T:
            cur = 0
            pointer = 1
            level = 0
            
            while pointer != len(raw):
                cur_char = raw[pointer] 
                if cur_char == '[':
                    label = raw[cur + 1 : pointer]
                    self.__printLabel__(label, level)
                    cur = pointer
                    level +=1
                elif cur_char == ']':
                    label = raw[cur + 1 : pointer]
                    self.__printLabel__(label, level)
                    cur = pointer
                    level -= 1
                elif cur_char == ',':
                    label = raw[cur + 1 : pointer]
                    self.__printLabel__(label, level)
                    cur = pointer
                else:
                    pass
                pointer += 1
                    
        #*************                Unknown print MODE                  ************#   
        else:
            raise ValueError("Print MODE should be 'S' to print a list representing Tree structure or 'T' to print a REAL Tree")    
            
    def __printLabel__(self, label, level):
        """
           Print each node
        """
        if level == 0:
            print(label)
        else:
            if level == 1:
                leadingSpaces = ''
                addl = ''
            else:
                leadingSpaces =   ' ' * 5 * (level - 1)
                addl = '|'
            
            if label.strip() != '': 
                print('{0}{1}{2}{3} {4}'.format('|', leadingSpaces, addl, '_' * 3, label))
        
            
            
            
            
            
            
            
            
            
            
            
            
        
