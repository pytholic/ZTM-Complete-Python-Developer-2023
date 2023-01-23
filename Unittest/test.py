import unittest
import script


class Testscript(unittest.TestCase):
    def setUp(self) -> None:
        print("about to test a function")

    def test_do_stuff(self):
        """
        *** Add comments here! ***
        """
        test_param = 10
        result = script.do_stuff(test_param)
        self.assertEqual(result, 15)

    # def test_do_stuff2(self):
    #     test_param = "abc"
    #     result = script.do_stuff(test_param)
    #     self.assertEqual(result, ValueError)

    def test_do_stuff2(self):
        test_param = "abc"
        result = script.do_stuff(test_param)
        # self.assertTrue(isinstance(result, ValueError))
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = script.do_stuff(test_param)
        self.assertEqual(result, "please enter number")

    def test_do_stuff4(self):
        test_param = ""
        result = script.do_stuff(test_param)
        self.assertEqual(result, "please enter number")

    def tearDown(self) -> None:
        print("Cleaning up!")


if __name__ == "__main__":
    unittest.main()
