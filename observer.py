# QBI-Observer Lite+

import re
from collections import Counter

class QBIObserverLite:
    def __init__(self):
        self.pensieri = []

        self.emozioni = ["paura", "speranza", "curiosità", "rimpianto", "frustrazione", "gioia", "ansia"]
        self.pattern_meta = ["perché", "come mai", "dovrei", "sto andando", "continuo"]

    def aggiungi_pensiero(self, pensiero):
        self.pensieri.append(pensiero.lower())

    def rileva_loop(self):
        conteggio = Counter(self.pensieri)
        return [pensiero for pensiero, freq in conteggio.items() if freq > 1]

    def rileva_domande(self):
        return [pensiero for pensiero in self.pensieri if '?' in pensiero]

    def riconosci_emozioni(self):
        emotivi = []
        for pensiero in self.pensieri:
            emotivi.extend([emoz for emoz in self.emozioni if emoz in pensiero])
        return emotivi

    def classificazione_metacognitiva(self):
        punteggio = 0
        punteggio += len(self.rileva_loop()) * 0.3
        punteggio += len(self.rileva_domande()) * 0.2
        punteggio += len(self.riconosci_emozioni()) * 0.25
        punteggio += sum(1 for pensiero in self.pensieri if any(meta in pensiero for meta in self.pattern_meta)) * 0.4

        if punteggio < 1:
            return "Bassa"
        elif punteggio < 2:
            return "Media"
        else:
            return "Alta"

    def get_diario_sessione(self):
        return self.pensieri

# Esempio di utilizzo
if __name__ == "__main__":
    observer = QBIObserverLite()
    observer.aggiungi_pensiero("Perché continuo a sbagliare?")
    observer.aggiungi_pensiero("Ho paura di fallire")
    observer.aggiungi_pensiero("Devo trovare una soluzione")
    observer.aggiungi_pensiero("Perché continuo a sbagliare?")

    print("Loop rilevati:", observer.rileva_loop())
    print("Domande interne:", observer.rileva_domande())
    print("Emozioni rilevate:", observer.riconosci_emozioni())
    print("Livello metacognitivo:", observer.classificazione_metacognitiva())
    print("Diario della sessione:", observer.get_diario_sessione())

