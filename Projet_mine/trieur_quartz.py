tas_de_minerai = [ 
{"type": "or", "calibre":"2", "pureté":"haute"},
{"type": "quartz", "calibre": "3" , "pureté":"moyenne"},
{"type": "emeraude", "calibre": "4", "pureté":"moyenne"},
{"type": "topaze", "calibre" : "5", "pureté": "basse"}
]

wagonnet_joailler =[]

print("Démarrage de la cabine de tri \n")

for pierre in tas_de_minerai :
    if pierre["type"] == "quartz" and pierre["calibre"] == "3":
        wagonnet_joailler.append(pierre)

print("commande prête pour la joaillerie")
print(f"quantité extraite : {len(wagonnet_joailler)}pierres correspondantes")
print("Détail du wagonnet:",wagonnet_joailler)