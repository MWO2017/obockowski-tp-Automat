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

    def pobierz_monete(self):
        self.__liczba_monet+=1
        self.__wrzucone+=1

    def wydaj_puszke(self):
        if (self.__liczba_puszek > 0) and (self.__wrzucone>0):
            self.__liczba_puszek-=self.__wrzucone
            self.__wrzucone=0
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
    a.pobierz_monete()
    a.pobierz_monete()
    a.podaj_ile()
    a.wydaj_puszke()
    a.podaj_ile()


        
    
