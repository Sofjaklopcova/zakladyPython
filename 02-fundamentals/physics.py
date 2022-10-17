'''
Konstanty v Pythonu

Konstanta je vlastně speciální typ proměnné, jejíž hodnota nemůže být změněna.
V Pythonu jsou konstanty obvykle deklarovány a přiřazovány v modulu, který bývá importován do souboru aplikace.
Konstanty jsou pojmenovány velkými písmeny a jednotlivá slova jsou oddělována podtržítky.
'''

EARTH_GRAVITY = 9.80665 #? normální pozemské tíhové zrychlení
MOON_GRAVITY = 1.62 #? měsíční gravitace
SPEED_OF_LIGHT = 3000000 #? rychlost světla ve vakuu
SPEED_OF_SOUND = 343 #? rychlost zvuku při teplotě 20 °C v suchém vzduchu

''' 
Úkol:
1. Doplňte správně hodnoty uvedených konstant.
2. Doplňte physics.py o několik výpočtových funkcí (opatřené docstrings), v nichž využijete minimálně všechny výše uvedené konstanty.
Samozřejmě můžete své řešení rozšířit i o jiné fyzikální konstanty.
3. Vytvořte z tohoto souboru samostatný modul v Pythonu podle návodu, který si sami najdete na internetu.      
4. Vytvořte vlastní aplikaci myapp.py, do níž tento modul importujte. Demonstrujte v ní na jednoduchých příkladech využití vámi
připravených funkcí.  
'''

def funkce_light(vteriny):
    '''
    vypocita vzdalenost, kterou dokazes zdolat za zadane vteriny rychlosti svetla
    '''
    return SPEED_OF_LIGHT  * vteriny

def funkce_sound(vteriny):
    '''
    vypocita vzdalenost v metrech, kterou dokazes zdolat za zadane vteriny rychlosti zvuky
    '''
    return SPEED_OF_SOUND  * vteriny


def zemska_tiha(kg):
    '''
    poznamka, co funkce dela melo by to pocitat jakou tihou pusobime na zem podle kg
    '''
    return kg * EARTH_GRAVITY

def mesicni_tiha(kg):
    '''
    poznamka, co funkce dela melo by to pocitat jakou tihou pusobime na mesic podle kg, kdyz tak to zkontroluj
    '''
    return kg * MOON_GRAVITY