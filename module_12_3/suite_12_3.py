import unittest
from test_12_3 import RunnerTest, TournamentTest

suite = unittest.TestSuite()

suite.addTests(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

test_runner = unittest.TextTestRunner(verbosity=2)
test_runner.run(suite)
