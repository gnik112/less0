import runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        Runner01 = runner.Runner('name')
        for _ in range(10):
            Runner01.walk()
        self.assertEqual(Runner01.distance, 50)

    def test_run(self):
        Runner01 = runner.Runner('name')
        for _ in range(10):
            Runner01.run()
        self.assertEqual(Runner01.distance, 100)

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


if __name__ == "__main__":
    unittest.main()
