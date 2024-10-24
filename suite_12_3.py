import unittest
import tests_12_3

testTS = unittest.TestSuite()
testTS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
testTS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(testTS)
