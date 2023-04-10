word = input(" ---------- Bienvenido al juego! ----------\n --------- Por favor ingrese su palabra ---------- \n").lower()
letters = list(word)
points = 0
for elem in letters:
    print(elem)
    match elem:
        case "a" | "e"|"i"|"o"|"u"|"l"|"n"|"r"|"s"|"t":
            points = points + 1
        case "d"|"g":
            points += 2
        case "b"|"c"|"m"|"p":
            points += 3
        case "f"|"h"|"v"|"w"|"y":
            points += 4
        case "k":
            points += 5
        case "j"|"x":
            points += 6
        case "q"|"z":
            points += 7
print ("Tus puntos son: ", points)