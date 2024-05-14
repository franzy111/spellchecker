import unittest
import coverage
from termcolor import colored
from flake8.api.legacy import get_style_guide


if __name__ == "__main__":
    cov = coverage.Coverage()
    cov.start()
    print(colored("\n================== unittest ==================\n", "yellow"))
    loader = unittest.TestLoader()
    suite = loader.discover(
        start_dir='./test/',
        pattern="*Test.py")
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

    print(colored("\n================== coverage ==================\n", "yellow"))
    cov.stop()
    cov.report()

    print(colored("\n==================  flake8  ==================\n", "yellow"))
    style_guide = get_style_guide()
    report = style_guide.check_files(['.',  'test'])