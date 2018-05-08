import pandas as pd
import numpy as np

class CPTU(object):

    def __init__(self, plik):
        self.df = pd.read_csv(plik, delimiter=',')
        print('Zaimportowano pomyślnie')
        self.dd = 0.02
        self.a = 0.15
        self.Pa = 100.0
        self.Nkt = 14.0

    def pokaz(self, wiersze=10):
        print(self.df.head(wiersze))

    def interpreter(self):
        self.df['qt'] = (self.df['qc'] + (self.df['u2'] / 1000) * (1 - self.a)) * 1000

        self.df['Rf'] = (self.df['fs'] / self.df['qt']) * 100 #dodać zabezpieczenie, gdy Rf < 0 , Rf = 0 (0.01???)

        self.df['gamma'] = (0.27 * (np.log10(self.df['Rf'])) + 0.36 * (np.log10(self.df['qt'] / self.Pa)) + 1.236) * 9.81
        # zabezpieczyc logarytmy przed niewłaściwymi wartościami

Test = CPTU('test_CPTU.csv')
Test.pokaz()

Test.interpreter()

Test.pokaz()
