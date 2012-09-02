pyTree
======

A Python implementation of Tree data structure
 
#Examples

## Build up tree structure:
### Initialization case 1: Initialize as single node
	        root = Tree('Root')
	        child01 = Tree('C01')
	        child02 = Tree('C02')
	        child03 = Tree('C03')
	        child11 = Tree('C11')
	        child31 = Tree('C31')
	        child111 = Tree('C111')
	        child112 = Tree('C112')
	        #add children nodes
	        root.addChildren([child01, child02, child03]) 
	        child01.addChild(child11)
	        child03.addChild(child31)
	        child11.addChild(child111)
	        child11.addChild(child112)
	        
	        #to print hierarchy tree structure
	        root.prettyTree()
	        #to print nested-list tree structure
	        #root.nestedTree()
#### Output:
		   	Root
	         |___ C01
	         |     |___ C11
	         |          |___ C111
	         |          |___ C112
	         |___ C02
	         |___ C03
	         |     |___ C31
	            
### Initialization case 2: Initialize with child
		child31 = Tree('C31')
	 	child03 = Tree('C03', child31 )
 			
### Initialization case 3: Initialize with children
		child01 = Tree('C01')
		child02 = Tree('C02')
		child03 = Tree('C03')
		root = Tree('Root', [child01, child02, child03] )
 			
## Methods
		Methods
			|___ addChild
			|___ addChildren
			|___ getParent
			|___ getChild
			|___ getChildren
			|___ getNode
			|___ delChild
			|___ delNode
			|___ getRoot
			|___ isRoot
			|___ isBranch
			|___ prettyTree
			|___ nestedTree

#LICENSING
Copyright 2012 Yoyo Zhou. Distributed under the [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0.html).  See the `LICENSE` file for details.