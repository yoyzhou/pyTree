'''
Unit test case for Tree class.
 
Created on Aug 25, 2012
@author: yoyzhou
'''
import unittest

from pyTree.Tree import Tree as Tree

(S, T) = range(2)

class TestTree(unittest.TestCase):
    
    def setUp(self):
        """
        Test Tree structure:
            Root
            |___ C01
            |     |___ C11
            |          |___ C111
            |          |___ C112
            |___ C02
            |___ C03
            |     |___ C31
        """
        self.root = Tree('Root')
        self.child01 = Tree('C01')
        self.child02 = Tree('C02')
        self.child03 = Tree('C03')
        self.child11 = Tree('C11')
        self.child31 = Tree('C31')
        self.child111 = Tree('C111')
        self.child112 = Tree('C112')
        self.root.addChildren([self.child01, self.child02, self.child03])
        self.child01.addChild(self.child11)
        self.child03.addChild(self.child31)
        self.child11.addChild(self.child111)
        self.child11.addChild(self.child112)
        #self.root.printTree(T)
        
    def test_initialization(self):
        pass
    
    def test_NewTree(self):
        root = Tree("Root")
        child1 = Tree("C01")
        child2 = Tree("C02")
        child21 = Tree("C21")
        root.addChild(child1)
        root.addChild(child2)
        child2.addChild(child21)
        self.assertEqual(root.data, "Root")
        self.assertEqual(root.getChildren()[0].data, "C01")
        
    def test_NewTreeSingle(self):
        child1 = Tree("C01")
        root = Tree('Root', child1)
        self.assertEqual(root.data, "Root")
        self.assertEqual(root.getChildren()[0].data, "C01")
     
    def test_NewTreeMulti(self):
        child1 = Tree("C01")
        child2 = Tree("C02")
        root = Tree('Root', [child1, child2])
        self.assertEqual(root.data, "Root")
        self.assertEqual(root.getChildren()[1].data, "C02")
        
    def test_Parent(self):
        self.assertEqual(self.child01.getParent(),  self.root)
        self.assertEqual(self.child02.getParent(),  self.root)
        self.assertEqual(self.child03.getParent(),  self.root)
        self.assertEqual(self.child11.getParent(),  self.child01)
        self.assertEqual(self.child31.getParent(),  self.child03)    
        
    def test_IsRoot(self):
        self.assertTrue(self.root.isRoot())
        self.assertFalse(self.child01.isRoot())
        self.assertFalse(self.child31.isRoot())
    
    def test_IsBranch(self):
        self.assertFalse(self.root.isBranch())
        self.assertFalse(self.child01.isBranch())
        self.assertFalse(self.child03.isBranch())
        self.assertTrue(self.child02.isBranch())
        self.assertFalse(self.child11.isBranch())
        self.assertTrue(self.child31.isBranch())
    
    def test_ChildrendotAssign(self):

        #self.root.children = []
        with self.assertRaises(AttributeError) as excpt:
            self.root.children = []
            self.assertEqual(excpt.expection, AttributeError)

    def test_GetRoot(self):
        self.assertEqual(self.root.getRoot(), self.root);
        self.assertEqual(self.child01.getRoot(), self.root)
        self.assertEqual(self.child31.getRoot(), self.root)
        
    def test_GetChild(self):
        self.assertEqual(self.root.getChild(2), self.child03)
        self.assertEqual(self.child03.getChild(0), self.child31);
        
        
    def test_GetNode(self):
        self.assertEqual(self.root.getNode('C31'), self.child31)
        self.assertEqual(self.child11.getNode('C11'), self.child11)
        self.assertEqual(self.root.getNode('C41'), None)
    
    def test_DelChild(self):
        self.child11.delChild(0);
        #self.root.prettyTree()
        
     
    def test_DelNode(self):
        self.root.delNode('C03');
        #self.root.prettyTree()
      
            
    def test_PrintTree(self):
        root = Tree('root')
        t1 = Tree('1')
        t11 = Tree('11')
        t111 = Tree('111')
        t1111 = Tree('1111')
        t11111 = Tree('11111')
        t111111 = Tree('111111')
        t1111111 = Tree('1111111')
        root.addChild(t1)
        t1.addChild(t11)
        t11.addChild(t111)
        t111.addChild(t1111)
        t1111.addChild(t11111)
        t1111.addChild(Tree('44444'))
        t11111.addChild(t111111)
        t111111.addChild(t1111111)
        root.prettyTree()       
        #self.root.prettyTree()
        # self.root.nestedTree()
       
        
    def tearDown(self):
        del self.root
        
        
if __name__ == "__main__":
    unittest.main()
        


