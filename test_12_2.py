import unittest
from runner_and_tournament import Runner, Tournament

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner("Усэйн", 10)
        self.runner2 = Runner("Андрей", 9)
        self.runner3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print({k: v.name for k, v in result.items()})

    def test_race_1(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        self.all_results["race_1"] = results
        self.assertTrue(results[max(results.keys())].name == "Ник")

    def test_race_2(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results["race_2"] = results
        self.assertTrue(results[max(results.keys())].name == "Ник")

    def test_race_3(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results["race_3"] = results
        self.assertTrue(results[max(results.keys())].name == "Ник")

if __name__ == "__main__":
    unittest.main()
