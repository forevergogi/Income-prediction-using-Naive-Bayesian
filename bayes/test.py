"""Bayes test function. Use this file to check your input and bayes function."""

from bayes import Evaluate


def test():
  # Set the test dataset file path and the generated file path.
  test_url = '../data/adult.test'
  report_url = '../result/BayesReport.txt'

  #test the Evaluate method.
  Evaluate(test_url,report_url)


if __name__ == '__main__':
  test()