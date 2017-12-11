'''
Created on Dec 11, 2017

@author: bockowsk@student.agh.edu.pl
'''

class Automat: 
    #konstruktor z mangling (pseudoprivate)
    def __init__(self,monety,puszki,wrzucone=0):
        self.__liczba_monet=monety
        self.__liczba_puszek=puszki
        self.__wrzucone=wrzucone

    def pobierz_monete(self,monety):
        self.__liczba_monet+=monety
        self.__wrzucone+=monety

    def wydaj_puszke(self,ile):
        #logika dla wydawania puszek i reszty
        if (self.__liczba_puszek >= ile) and (self.__wrzucone>=ile):
            self.__liczba_puszek-=ile
            self.__wrzucone-=ile
            if self.__wrzucone > 0:
                self.__zwroc_monete()
            return True
        else:
            return False
    
    def __zwroc_monete(self):
        self.__liczba_monet-=self.__wrzucone
        self.__wrzucone=0

    def podaj_ile(self):
        print self.__liczba_monet
        print self.__liczba_puszek

if __name__ == '__main__':
    a=Automat(10,50)
    a.pobierz_monete(8)
    a.pobierz_monete(2)
    a.podaj_ile()
    a.wydaj_puszke(6)
    a.podaj_ile()


        
    
