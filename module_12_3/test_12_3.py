import unittest
from runner import Runner
from runner_and_tournament import Runner, Tournament

def skip_if_frozen(test_method):
    def wrapper(self, *args, **kwargs):
        if getattr(self, "is_frozen", False):
            self.skipTest("Тесты в этом кейсе заморожены")
        else:
            test_method(self, *args, **kwargs)
    return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen
    def test_walk(self):
        runner = Runner("Walker")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @skip_if_frozen
    def test_run(self):
        runner = Runner("Runner")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @skip_if_frozen
    def test_challenge(self):
        runner1 = Runner("Runner1")
        runner2 = Runner("Runner2")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

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

    @skip_if_frozen
    def test_race_1(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        self.all_results["race_1"] = results
        self.assertTrue(results[max(results.keys())].name == "Ник")

    @skip_if_frozen
    def test_race_2(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results["race_2"] = results
        self.assertTrue(results[max(results.keys())].name == "Ник")

    @skip_if_frozen
    def test_race_3(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results["race_3"] = results
        self.assertTrue(results[max(results.keys())].name == "Ник")

    @skip_if_frozen
    def test_race_4(self):
        tournament = Tournament(90, self.runner1, self.runner2)
        results = tournament.start()
        self.all_results["race_4"] = results
        self.assertTrue(results[max(results.keys())].name == "Андрей")


if __name__ == "__main__":
    suite = unittest.TestSuite()