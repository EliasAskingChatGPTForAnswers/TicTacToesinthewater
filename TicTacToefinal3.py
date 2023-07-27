def main():
    sym_1 = input('Spieler 1, willst du X oder O sein? ').upper()
    while sym_1 not in ['X', 'O']:
        print('Falsch, mach gescheit')
        sym_1 = input('Spieler 1, willst du X oder O sein? ').upper()

    sym_2 = 'O' if sym_1 == 'X' else 'X'

    brett = spielbrett()

    zug = 1
    while zug < 10:
        start(sym_1, sym_2, brett, zug, falsch)
        printboard(brett)
        if gewinner(brett, sym_1, sym_2):
            print('Spiel vorbei!')
            return
        elif zug == 9:
            print('Unentschieden')
        zug += 1


def spielbrett():
    return [[" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]]

def start(sym_1, sym_2, brett, zug, falsch):
    if zug % 2 == 0:
        spieler = sym_2
    else:
        spieler = sym_1
    print('Spieler ' + spieler + ", du bist dran ")
    zeile = int(input('Wähle eine Zeile, drücke die Zahlen 1 bis 3 für die jeweilige Zeile: '))
    spalte = int(input('Wähle eine Spalte, drücke die Zahlen 1 bis 3 für die jeweilige Spalte: '))
    while zeile > 3 or spalte > 3:
        falsch(zeile, spalte)
        zeile = int(input('Wähle eine Zeile: '))
        spalte = int(input('Wähle eine Spalte: '))
    while brett[zeile-1][spalte-1] == sym_1 or brett[zeile-1][spalte-1] == sym_2:
        print('Feld ist bereits belegt')
        zeile = int(input('Wähle eine Zeile: '))
        spalte = int(input('Wähle eine Spalte: '))
    if spieler == sym_1:
        brett[zeile-1][spalte-1] = sym_1
    else:
        brett[zeile-1][spalte-1] = sym_2
    return brett

def falsch(zeile, spalte):
    print('Wähle nochmal, diesmal korrekt')

def printboard(brett):
    print("---+---+---")
    for r in range(3):
        print(brett[r][0], "|", brett[r][1], "|", brett[r][2])
        print("---+---+---")

def gewinner(brett, sym_1, sym_2):
    # Überprüfung der Zeilen und Spalten
    for i in range(3):
        if brett[i][0] == brett[i][1] == brett[i][2] == sym_1 or \
           brett[0][i] == brett[1][i] == brett[2][i] == sym_1:
            print("Spieler 1 hat gewonnen!")
            return True
        elif brett[i][0] == brett[i][1] == brett[i][2] == sym_2 or \
             brett[0][i] == brett[1][i] == brett[2][i] == sym_2:
            print("Spieler 2 hat gewonnen!")
            return True

    # Überprüfung der Diagonalen
    if brett[0][0] == brett[1][1] == brett[2][2] == sym_1 or \
       brett[0][2] == brett[1][1] == brett[2][0] == sym_1:
        print("Spieler 1 hat gewonnen!")
        return True
    elif brett[0][0] == brett[1][1] == brett[2][2] == sym_2 or \
         brett[0][2] == brett[1][1] == brett[2][0] == sym_2:
        print("Spieler 2 hat gewonnen!")
        return True

    return False

main()
