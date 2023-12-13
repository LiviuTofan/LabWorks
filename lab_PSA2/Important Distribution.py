from numpy.random import choice

def taxatoare():
    tries = 730
    capusta = 0
    c = 0
    for i in range(tries):
        posibil = [False, True]
        taxatoarea = choice(posibil, 1, p=[0.98, 0.02])[0] #[0] ca sa intoarca elementul dar nu lista, fara [0] = [False], cu [0] = False
        controlorul = choice(posibil, 1, p=[0.95, 0.05])[0]
        if taxatoarea:
            capusta += 6
        elif controlorul:
            if c == 0:
                capusta += 50
            elif c == 1:
                capusta += 150
            elif c >= 2:
                capusta += 300
            c += 1
    return capusta

capusta = taxatoare()
print('Jora pays with:',capusta - (6*730),'more than student')