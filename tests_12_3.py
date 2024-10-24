import runner
import runner_and_tournament
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        Runner01 = runner.Runner('name')
        for _ in range(10):
            Runner01.walk()
        self.assertEqual(Runner01.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        Runner01 = runner.Runner('name')
        for _ in range(10):
            Runner01.run()
        self.assertEqual(Runner01.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        Runner01 = runner.Runner('name')
        Runner02 = runner.Runner('name')
        for _ in range(10):
            Runner01.run()
            Runner02.walk()
        for _ in range(5):
            Runner02.run()
            Runner01.walk()
        self.assertNotEqual(Runner01.distance, Runner02.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.Runner01 = runner_and_tournament.Runner('Усэйн', 10)
        self.Runner02 = runner_and_tournament.Runner('Андрей', 9)
        self.Runner03 = runner_and_tournament.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for i, data in cls.all_results.items():
            res_str = ''
            for i1, d1 in data.items():
                res_str += f'{i1}: {d1}, '
            print('{' + res_str[:-2] + '}')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_01(self):
        tour01 = runner_and_tournament.Tournament(90, self.Runner01, self.Runner03)
        TournamentTest.all_results[1] = tour01.start()
        self.assertTrue(TournamentTest.all_results[1][len(TournamentTest.all_results[1])].name == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_02(self):
        tour01 = runner_and_tournament.Tournament(90, self.Runner02, self.Runner03)
        TournamentTest.all_results[2] = tour01.start()
        self.assertTrue(TournamentTest.all_results[2][len(TournamentTest.all_results[2])].name == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_03(self):
        tour01 = runner_and_tournament.Tournament(90, self.Runner01, self.Runner02, self.Runner03)
        TournamentTest.all_results[3] = tour01.start()
        self.assertTrue(TournamentTest.all_results[3][len(TournamentTest.all_results[3])].name == 'Ник')
