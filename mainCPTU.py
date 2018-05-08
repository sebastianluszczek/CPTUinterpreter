import pandas as pd

class CPTU(object):

    def __init__(self, plik):
        self.df = pd.read_csv(plik, delimiter=',')
        print('Zaimportowano pomyślnie')

    def pokaz(self, wiersze=10):
        print(self.df.head(wiersze))

Test = CPTU('test_CPTU.csv')
Test.pokaz()
