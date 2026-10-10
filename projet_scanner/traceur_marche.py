import time

portefeuille =[
    {"actif": "Solana" , "prix_actuel": 165.20, "take_profit":160.00},
    {"actif": "Nvidia", "prix_actuel" : 850.50, "take_profit":900.00},
    {"actif": "Or", "prix_actuel":2360.00, "take_profit": 2400.00},
    {"actif": "Sp500", "prix_actuel":5120.00, "take_profit": 5200.00}
]

print("Démarrage du scanner de marché...\n")

cycle_effectue = 0


while True:
    cycle_effectue += 1
    print(f"---cycle de scan n°{cycle_effectue}---")

    for token in portefeuille:
        if token["prix_actuel"]>=token["take_profit"]:
            print(f"ALERTE TP: {token['actif']} déclenche le profit à token {token['take_profit']}!")
        else:
            print(f"{token['actif']} suit les prix du marché (Actuel {token['prix_actuel']})")

    if cycle_effectue == 3:
        print("\n limite atteinte : le programme coupe ses positions et s'éteint proprement")
        break

    print("\n En attente pour le procain scan...\n")
    time.sleep(60)