from rt_with_exceptions import Runner
import logging


class RunnerTest:

    def test_walk(self):
        try:
            r1 = Runner('Вася', -5)
            for _ in range(10):
                r1.walk()
            logging.info('"test_walk" выполнен успешно')
        except ValueError as err:
            logging.warning("Неверная скорость для Runner", exc_info=True)

    def test_run(self):
        try:
            r2 = Runner(2)
            for _ in range(10):
                r2.run()
        except TypeError as err:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding="utf-8",
                        format="%(asctime)s | %(levelname)s | %(message)s")
    rt = RunnerTest()
    rt.test_run()
    rt.test_walk()
