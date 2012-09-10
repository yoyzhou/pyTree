'''
pyTree: A list-derived TREE data structure in Python 

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
    
    
    
    def getNode(self, content, includeself = True):
        """
                         
            Get the first matching item(including self) whose data is equal to content. 
            Method uses data == content to determine whether a node's data equals to content, note if your node's data is 
            self defined class, overriding object's __eq__ might be required.
            Implement Tree travel (level first) algorithm using queue

            @param content: node's content to be searched 
            @return: Return node which contains the same data as parameter content, return None if no such node
        """
        
        nodesQ = []
        
        if includeself:
            nodesQ.append(self)
        else:
            nodesQ.extend(self.getChildren())
            
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
        
    def prettyTree(self):
        """"
            Another implementation of printing tree using Stack
            Print tree structure in hierarchy style.
            For example:
                Root
                |___ C01
                |     |___ C11
                |          |___ C111
                |          |___ C112
                |___ C02
                |___ C03
                |     |___ C31
            A more elegant way to achieve this function using Stack structure, 
            for constructing the Nodes Stack push and pop nodes with additional level info. 
        """

        level = 0        
        NodesS = [self, level]   #init Nodes Stack
        
        while NodesS:
            head = NodesS.pop() #head pointer points to the first item of stack, can be a level identifier or tree node 
            if isinstance(head, int):
                level = head
            else:
                self.__printLabel__(head, NodesS, level)
                children = head.getChildren()
                children.reverse()
                
                if NodesS:
                    NodesS.append(level)    #push level info if stack is not empty
                
                if children:          #add children if has children nodes 
                    NodesS.extend(children)
                    level += 1
                    NodesS.append(level)
    
    def nestedTree(self):
        """"
            Print tree structure in nested-list style.
            For example:
            [0] nested-list style
                [Root[C01[C11[C111,C112]],C02,C03[C31]]]
            """
        
        NestedT = ''  
        delimiter_o = '['
        delimiter_c = ']'                                                                                  
        NodesS = [delimiter_c, self, delimiter_o]
                                                                                            
        while NodesS:
            head = NodesS.pop()
            if isinstance(head, str):
                NestedT += head
            else:
                NestedT += str(head.data)
                
                children = head.getChildren()
            
                if children:          #add children if has children nodes 
                    NodesS.append(delimiter_c)
                    for child in children: 
                        NodesS.append(child)
                        NodesS.append(',')
                    NodesS.pop()
                    NodesS.append(delimiter_o) 
               
        print(NestedT)
          
    def __printLabel__(self, head, NodesS, level):
        """
           Print each node
        """
        leading = '' 
        lasting = '|___ '
        label = str(head.data)
        
        if level == 0:
            print(str(head))
        else:
            for l in range(0, level - 1):
                sibling = False
                parentT = head.__getParent__(level - l)
                for c in parentT.getChildren():
                    if c in NodesS:
                        sibling = True
                        break
                if sibling:
                    leading += '|     '
                else:
                    leading += '     '
            
            if label.strip() != '': 
                print('{0}{1}{2}'.format( leading, lasting, label))
        
    
    def __getParent__(self, up):
        parent = self;
        while up:
            parent = parent.getParent()
            up -= 1
        return parent
            
            
            
            
            
            
            
            
            
            
        
