import runner_and_tournament
import unittest


class TournamentTest(unittest.TestCase):

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

    def test_01(self):
        tour01 = runner_and_tournament.Tournament(90, self.Runner01, self.Runner03)
        TournamentTest.all_results[1] = tour01.start()
        self.assertTrue(TournamentTest.all_results[1][len(TournamentTest.all_results[1])].name == 'Ник')

    def test_02(self):
        tour01 = runner_and_tournament.Tournament(90, self.Runner02, self.Runner03)
        TournamentTest.all_results[2] = tour01.start()
        self.assertTrue(TournamentTest.all_results[2][len(TournamentTest.all_results[2])].name == 'Ник')

    def test_03(self):
        tour01 = runner_and_tournament.Tournament(90, self.Runner01, self.Runner02, self.Runner03)
        TournamentTest.all_results[3] = tour01.start()
        self.assertTrue(TournamentTest.all_results[3][len(TournamentTest.all_results[3])].name == 'Ник')

    def test_04(self):
        # Проверка результатов на разных дистанциях
        for i in range(1, 161):
            Runner01 = runner_and_tournament.Runner('Усэйн', 10)
            Runner02 = runner_and_tournament.Runner('Андрей', 9)
            Runner03 = runner_and_tournament.Runner('Ник', 6)
            tour01 = runner_and_tournament.Tournament(i, Runner01, Runner02, Runner03)
            all_results = tour01.start()
            if all_results[len(all_results)].name != 'Ник':
                print('dist Error:', i)
            else:
                print('dist OK:', i)


if __name__ == "__main__":
    unittest.main()
