listOfPlayers = ["messi", "ronaldo", "neymar"]

for player in listOfPlayers:
    searchPlayer = input("Ingrese el jugador que desea buscar: ")
    if searchPlayer == player:
        print(player)
    else:
        print("Jugador no encontrado")