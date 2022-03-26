import sys

# print(sys.path)

from behave import __main__ as TestRunner

if __name__=='__main__':
        sys.stdout.flush()
        TestRunner.main()

# test_runner()