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

        def friction_ratio(fs, qt):
            if float(fs) <= 0:
                return 0.0
            else:
                return (fs / qt) * 100

        self.df['Rf'] = self.df.apply(lambda x: friction_ratio(x['fs'], x['qt']), axis = 1)

        def soil_unit_weight(Rf, qt, Pa):
            if Rf == 0.0:
                return (0.27 * (-1) + 0.36 * (np.log10(qt / Pa)) + 1.236) * 9.81
            else:
                return (0.27 * (np.log10(Rf)) + 0.36 * (np.log10(qt / Pa)) + 1.236) * 9.81

        self.df['gamma'] = self.df.apply(lambda x: soil_unit_weight(x['Rf'], x['qt'], self.Pa), axis=1)

Test = CPTU('test_CPTU.csv')
Test.pokaz()

Test.interpreter()

Test.pokaz()
