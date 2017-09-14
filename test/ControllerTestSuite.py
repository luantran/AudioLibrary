import unittest
from test import InitTests
from test import ImportTests
import os
if __name__ == '__main__':
    os.environ['MEDIA_PATH'] = '/home/luantran/Music/ImportTests'
    suite1 = unittest.TestLoader().loadTestsFromTestCase(InitTests.InitTests)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(ImportTests.ImportTests)
    unittest.TextTestRunner(verbosity=2).run(suite1)
    unittest.TextTestRunner(verbosity=2).run(suite2)
