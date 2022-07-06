import unittest
from set_operations import set_operations
from dictionary import dict_add,dict_del,dict_display,dict_check,d
from test.TestUtils import TestUtils
class FuctionalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.A={1,2,3,4}
        cls.B={2,10,4,20}
        cls.C={4,10,40,30,2}
    def test_union(self):
        test_obj = TestUtils()
        result=set_operations(1,FuctionalTests.A,FuctionalTests.B,FuctionalTests.C)
        if result=={1,2,3,4,40,10,20,30}:
            test_obj.yakshaAssert("TestUnion", True, "functional")
            print("TestUnion = Passed")
        else:
            test_obj.yakshaAssert("TestUnion", False, "functional")
            print("TestUnion = Failed")

    def test_intersection(self):
        test_obj = TestUtils()
        result=set_operations(2,FuctionalTests.A,FuctionalTests.B,FuctionalTests.C)
        if result=={2,4}:
            test_obj.yakshaAssert("TestIntersection", True, "functional")
            print("TestIntersection = Passed")
        else:
            test_obj.yakshaAssert("TestIntersection", False, "functional")
            print("TestIntersection = Failed")

    def test_difference(self):
        test_obj = TestUtils()
        result=set_operations(3,FuctionalTests.A,FuctionalTests.B,FuctionalTests.C)
        if result=={1,3}:
            test_obj.yakshaAssert("TestDifference", True, "functional")
            print("TestDifference = Passed")
        else:
            test_obj.yakshaAssert("TestDifference", False, "functional")
            print("TestDifference = Failed")

    def test_symmetric_difference(self):
        test_obj = TestUtils()
        result=set_operations(4,FuctionalTests.A,FuctionalTests.B,FuctionalTests.C)
        if result=={1,2,3,4,20,40,30}:
            test_obj.yakshaAssert("TestSymmetricDifferenc", True, "functional")
            print("TestSymmetricDifferenc = Passed")
        else:
            test_obj.yakshaAssert("TestSymmetricDifferenc", False, "functional")
            print("TestSymmetricDifferenc = Failed")

    def test_is_dict(self):
        test_obj = TestUtils()
        result=dict_add(101,'Apple')
        if type(result)==type({}):
            test_obj.yakshaAssert("TestIsDict", True, "functional")
            print("TestIsDict = Passed")
        else:
            test_obj.yakshaAssert("TestIsDict", False, "functional")
            print("TestIsDict = Failed")

    def test_element_added(self):
        test_obj = TestUtils()
        result=dict_add(101,'Apple')
        if result!=None:
            if len(result)!=0:
                test_obj.yakshaAssert("TestElementAdded", True, "functional")
                print("TestElementAdded = Passed")
            else:
                test_obj.yakshaAssert("TestElementAdded", False, "functional")
                print("TestElementAdded = Failed")
        else:
            test_obj.yakshaAssert("TestElementAdded", False, "functional")
            print("TestElementAdded = Failed")

    def test_is_element_added(self):
        test_obj = TestUtils()
        result=dict_add(102,'Orange')
        if result!=None:
            if len(result)!=0:
                test_obj.yakshaAssert("TestIsElementAdded", True, "functional")
                print("TestIsElementAdded = Passed")
            else:
                test_obj.yakshaAssert("TestIsElementAdded", False, "functional")
                print("TestIsElementAdded = Failed")
        else:
            test_obj.yakshaAssert("TestIsElementAdded", False, "functional")
            print("TestIsElementAdded = Failed")

    def test_is_result_dict_type(self):
        test_obj = TestUtils()
        result=dict_display()
        if type(result)==type({}):
            test_obj.yakshaAssert("TestIsResultDictType", True, "functional")
            print("TestIsResultDictType = Passed")
        else:
            test_obj.yakshaAssert("TestIsResultDictType", False, "functional")
            print("TestIsResultDictType = Failed")

    def test_search_element_of_dict(self):
        test_obj = TestUtils()
        result=dict_check(102)
        if result=="TRUE":
            test_obj.yakshaAssert("TestSearchElementOfDict", True, "functional")
            print("TestSearchElementOfDict = Passed")
        else:
            test_obj.yakshaAssert("TestSearchElementOfDict", False, "functional")
            print("TestSearchElementOfDict = Failed")

    def test_is_element_deleted(self):
        test_obj = TestUtils()
        result=dict_del(101)
        if result=="TRUE":
            test_obj.yakshaAssert("TestIsElementDeleted", True, "functional")
            print("TestIsElementDeleted = Passed")
        else:
            test_obj.yakshaAssert("TestIsElementDeleted", False, "functional")
            print("TestIsElementDeleted = Failed")
