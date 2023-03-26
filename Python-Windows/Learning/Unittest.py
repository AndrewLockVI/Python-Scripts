#This is for learning about how assertions for test cases work
#Basiacally you import unittest initialize it using unittest.main()
#Then you need to have initialize a class with an input parameter of unittest.TestCase
#For functions that you want to be used as test cases you should have an input param of self meaning the instance of the class
#Then with the refrence to self you can find use the assert statements

#Honestly a simple assert statement is better and easier to implement though it will stop the function if it is false so ymmv

import unittest






class TestClass(unittest.TestCase):
    def test_function(self):
        self.assertTrue(True)
        self.assertTrue(False)





unittest.main()

test_class = TestClass()

test_class.test_function()