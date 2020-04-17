print(__name__)

#standard exit code to prevent use as a program
if __name__ == '__main__':
    errormessage = 'This is a module and should not be run alone'
    print(errormessage)
    #quits if run as script
    from sys import exit
    exit(errormessage)

#------------------------------------------------

from .. import globale_variablen, settings
import time, pygame

#hier begint de customclock class. En dan kan je denken:"Sytze, waarom noem je class niet gwn clock?". NOU OMDAT PYGAME AL EEN OBJECT HEEFT GENAAMD CLOCK!!!!!!!!!!!    
class stopwatch():
    def __init__(self, kleurrect, kleurtijd, xleft, ytop, uren, outline, dikte, kleuroutline):
        self.kleurrect = kleurrect
        self.kleurtijd = kleurtijd
        self.xleft = xleft
        self.ytop = ytop
        self.uren = uren
        self.outline = outline
        self.dikte = dikte
        self.kleuroutline = kleuroutline
        #Dit slaat de tijd op op het moment dat dit script wordt gestart.
        #time.gmtime() geeft een aray aan variabelen(?). Waarbij [3] de uren geeft, [4] de minuten en [5] de seconden.
        self.start = time.gmtime()
        
#Hier begint de functie drawclock waarin een stopwatch wordt geïnitïeerd en daarna ook getekend/
    def update(self):
        #Door global screen te doen haal kan je screen gebruiken die eerder gedefnieerd is.
        #Dit komt doordat screen zich in de globale sector bevindt en deze class zit in de lokale sector.
        global screen
        #Slaat de tijd op van nu. Dit is dus de steeds veranderende tijd.
        now = time.gmtime()
        #Hier wordt het verschil in seconden berekent tussen de starttijd en de tijd van nu.
        seconde = now[5]-self.start[5]
        #Hier wordt het verschil in minuten berekent tussen de starttijd en de tijd van nu.
        minuut = now[4]-self.start[4]
        #Hier wordt het verschil in uren berekent tussen de starttijd en de tijd van nu.
        uur = now[3]-self.start[3]

        #De lettertype grootte
        grootte = 25

        #De font (lettertype) wordt  hier bepaald.
        default_font = pygame.font.Font("C:/Windows/Fonts/comicz.TTF", grootte)
        #Als het verschil in seconden negatief wordt, wordt het met behulp van dit trucje weer goed positief gemaakt.
        if seconde < 0:
            seconde += 60
            minuut -= 1
            
        #Als het verschil in minuten negatief wordt, wordt het met behulp van dit trucje weer goed positief gemaakt.
        if minuut < 0:
            minuut += 60
            uur -= 1
            
        #Het rechthoekje met tijd erin kan verschillen door het hebben van uren in de tijd of niet. De breedte van het rechthoekje wordt hier dan gecorigeerd.
        if self.uren:
            breedte = 170    
        else:
            breedte = 105
            
        #De hoogte blijft wel altijd gelijk.    
        hoogte = 30    

        #Als self.outline is True dan wordt er eerst een grotere rechthoek getekent waarna het kleinere het rechthoek er overheen wordt getekent waardoor het lijkt
        #alsof er een outline is getekent om het kleinere rechthoek heen.
        if self.outline and self.dikte>0 and self.dikte<10:
            #grotere rechthoek wordt getekent
            pygame.draw.rect(globale_variablen.screen, self.kleuroutline, (self.xleft-5-self.dikte, self.ytop+5-self.dikte, breedte+2*self.dikte, hoogte+2*self.dikte))
        #kleinere rechthoek wordt getekent    
        pygame.draw.rect(globale_variablen.screen, self.kleurrect, (self.xleft-5, self.ytop+5, breedte, hoogte))
        #als self.uren false is dan worden de uren niet in het tijdsblokje gegeven. Anders wel.
        if not self.uren:
            #tekst zonder uren
            tijd_tekst = default_font.render(str(minuut).zfill(2) + ' : ' + str(seconde).zfill(2), True, self.kleurtijd)
        else:
            #tekst met uren
            tijd_tekst = default_font.render(str(uur).zfill(2) + ' : ' + str(minuut).zfill(2) + ' : ' + str(seconde).zfill(2), True, self.kleurtijd)
        #tekst wordt getekent
        globale_variablen.screen.blit(tijd_tekst, (self.xleft,self.ytop))

