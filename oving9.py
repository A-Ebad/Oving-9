
"""
Aauthor: Ebad Akbari
Øving: 9 Prosjekt del 1
"""

class Sporsmaal:

    def __init__(self, sporsmaal, svar, korekt_svar):
        self.sporsmaal = sporsmaal
        self.svar = svar
        self.korekt_svar = korekt_svar
        
    def __str__(self):
        tekst = self.sporsmaal + "\n"
        for indeks,alt in enumerate(self.svar):
            tekst += f"{indeks+1}: {alt}\n"
        return tekst
    
    def korekt_svar_test(self, korekt_svar):
        if self.korekt_svar == korekt_svar:
            return True
        return False
     
    def svar_rett(self):
        return self.svar[int(self.korekt_svar)]
 
def tekst_fil():

    spormaaler = []
    
    with open("sporsmaalsfil.txt", "r", encoding='UTF8') as txt:
        for linje in txt:
            svar, korekt_svar, liste = linje.strip().split(":")
            liste = liste.replace("[", "")
            liste = liste.replace("]", "")
            liste = liste.replace(" ", "")
            liste = liste.split(",")
            midltd = Sporsmaal(svar, liste, korekt_svar)
            spormaaler.append(midltd)
            
        return spormaaler
    
if __name__ == "__main__":
    lese_tekst = tekst_fil()
    n = 0
    tell_spiller_1 = 0
    tell_spiller_2 = 0

    for spormaaler in lese_tekst:
        print("\nSvar på følgende spormåler:" + '\n')
        print(lese_tekst[n]) 
        
        spiller_1_svar = input("Skriv svaret til spiller 1: ")
        spiller_2_svar = input("Skriv svaret til spiller 2: ")
        
        if spiller_1_svar == lese_tekst[n].svar_rett():
            tell_spiller_1 += 1
            print("\n Svaret til spiller 1 riktig! ")
            
        else:
            print("\n Svaret til spiller 1 feil")
                
        if spiller_2_svar == lese_tekst[n].svar_rett():
            tell_spiller_2 += 1
            print("\n Svaret til spiller 2 er riktig! ")
            
        else:
            print("\n Svaret til spiller 2 feil ")
               
        print("\nDen riktige svaret er ", lese_tekst[n].svar_rett())
              
        n+=1
            
    print(f"\nSpiller 1 svarte rett: {tell_spiller_1} av {len(lese_tekst)}") 
    print(f"\nSpiller 2 svarte rett: {tell_spiller_2} av {len(lese_tekst)}")