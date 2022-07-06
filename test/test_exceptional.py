import unittest
from set_operations import set_operations
from dictionary import dict_add,dict_del,dict_display,dict_check,d
from test.TestUtils import TestUtils
class ExceptionalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.A={1,2,3,4}
        cls.B={2,10,4,20}
        cls.C={4,10,40,30,2}
    def test_union_incorrect(self):
        test_obj = TestUtils()
        result=set_operations(1,ExceptionalTests.A,ExceptionalTests.B,ExceptionalTests.C)
        if result!={1,2,3,4,40,10,20,30}:
            test_obj.yakshaAssert("TestUnionIncorrect", False, "exception")
            print("TestUnionIncorrect = Failed")
        else:
            test_obj.yakshaAssert("TestUnionIncorrect", True, "exception")
            print("TestUnionIncorrect = Passed")

    def test_intersection_incorrect(self):
        test_obj = TestUtils()
        result=set_operations(2,ExceptionalTests.A,ExceptionalTests.B,ExceptionalTests.C)
        if result!={2,4}:
            test_obj.yakshaAssert("TestIntersectionIncorrect", False, "exception")
            print("TestIntersectionIncorrect = Failed")
        else:
            test_obj.yakshaAssert("TestIntersectionIncorrect", True, "exception")
            print("TestIntersectionIncorrect = Passed")

    def test_difference_incorrect(self):
        test_obj = TestUtils()
        result=set_operations(3,ExceptionalTests.A,ExceptionalTests.B,ExceptionalTests.C)
        if result!={1,3}:
            test_obj.yakshaAssert("TestDifferenceIncorrect", False, "exception")
            print("TestDifferenceIncorrect = Failed")
        else:
            test_obj.yakshaAssert("TestDifferenceIncorrect", True, "exception")
            print("TestDifferenceIncorrect = Passed")

    def test_symmetric_difference_incorrect(self):
        test_obj = TestUtils()
        result=set_operations(4,ExceptionalTests.A,ExceptionalTests.B,ExceptionalTests.C)
        if result!={1,2,3,4,20,40,30}:
            test_obj.yakshaAssert("TestSymmetricDifferenceIncorrect", False, "exception")
            print("TestSymmetricDifferenceIncorrect = Failed")
        else:
            test_obj.yakshaAssert("TestSymmetricDifferenceIncorrect", True, "exception")
            print("TestSymmetricDifferenceIncorrect = Passed")

    def test_is_dict_incorrect(self):
        test_obj = TestUtils()
        result=dict_add(101,'Apple')
        if type(result)!=type({}):
            test_obj.yakshaAssert("TestIsDictIncorrect", False, "exception")
            print("TestIsDictIncorrect = Failed")
        else:
            test_obj.yakshaAssert("TestIsDictIncorrect", True, "exception")
            print("TestIsDictIncorrect = Passed")


    def test_is_element_not_added(self):
        test_obj = TestUtils()
        result=dict_add(101,'Apple')
        if result!=None:
            if len(result)==0:
                test_obj.yakshaAssert("TestIsElementNotAdded", False, "exception")
                print("TestIsElementNotAdded = Failed")
            else:
                test_obj.yakshaAssert("TestIsElementNotAdded", True, "exception")
                print("TestIsElementNotAdded = Passed")
        else:
            test_obj.yakshaAssert("TestIsElementNotAdded", False, "exception")
            print("TestIsElementNotAdded = Failed")

    def test_element_not_added(self):
        test_obj = TestUtils()
        result=dict_add(102,'Oraange')
        if result!=None:
            if len(result)!=0:
                test_obj.yakshaAssert("TestElementNotAdded", True, "functional")
                print("TestElementNotAdded = Passed")
            else:
                test_obj.yakshaAssert("TestElementNotAdded", False, "functional")
                print("TestElementNotAdded = Failed")
        else:
            test_obj.yakshaAssert("TestElementNotAdded", False, "functional")
            print("TestElementNotAdded = Failed")

    def test_is_element_not_deleted(self):
        test_obj = TestUtils()
        result=dict_del(101)
        if result!=None:
            if result=="FALSE":
                test_obj.yakshaAssert("TestIsElementNotDeleted", False, "exception")
                print("TestIsElementNotDeleted = Failed")
            else:
                test_obj.yakshaAssert("TestIsElementNotDeleted", True, "exception")
                print("TestIsElementNotDeleted = Passed")
        else:
            test_obj.yakshaAssert("TestIsElementNotDeleted", False, "exception")
            print("TestIsElementNotDeleted = Failed")

    def test_is_result_dict_not_type(self):
        test_obj = TestUtils()
        result=dict_display()
        if type(result)!=type({}):
            test_obj.yakshaAssert("TestIsResultNotDictType", False, "exception")
            print("TestIsResultNotDictType = Failed")
        else:
            test_obj.yakshaAssert("TestIsResultNotDictType", True, "exception")
            print("TestIsResultNotDictType = Passed")

    def test_search_element_of_dict_false(self):
        test_obj = TestUtils()
        result=dict_check(102)
        if result!=None:
            if result=="FALSE":
                test_obj.yakshaAssert("TestSearchElementOfDictFalse", False, "exception")
                print("TestSearchElementOfDictFalse = Failed")
            else:
                test_obj.yakshaAssert("TestSearchElementOfDictFalse", True, "exception")
                print("TestSearchElementOfDictFalse = Passed")
        else:
            test_obj.yakshaAssert("TestSearchElementOfDictFalse", False, "exception")
            print("TestSearchElementOfDictFalse = Failed")
