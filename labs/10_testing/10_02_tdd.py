'''
Write a script that demonstrates TDD. Using pseudocode, plan out a couple simple functions. They could be
as simple as add and subtract or more complex such as functions that read and write to files.

Instead of writing out the functions, only provide the tests. Think about how the functions might
fail and write tests that will check and prevent failure.

You do not need to implement the actual functions after writing the tests but you may.

'''
import unittest

#function: multiply_by_four()
#multiply user input by 4

def multiply_by_four(n):
    return n*4

class TestMultiplyByFour(unittest.TestCase):
    def test_DivisibleByFour(self):
        self.assertEqual(multiply_by_four(5) % 4, 0)
        
# function: import_text_file
# take user input and open file of that name
        
def import_text_file(file_name):
    with  open(file_name, 'r') as fin:
            text=(fin.readlines()) 

class TestFileImport(unittest.TestCase):
    def test_FNFError(self):
        with self.assertRaises(FileNotFoundError):
            import_text_file("butts")


unittest.main()