lista = []

print("illeszd be a domaineket, mindent külön sorba. ha végeztél, nyomj entert")

while True:
    felhasználói_bevitel = input()
    if felhasználói_bevitel == "":
        break
    lista.append(felhasználói_bevitel)

új_lista = ["0.0.0.0 " + item for item in lista]

újabb_lista = [item for sublist in [item.split(",") for item in új_lista] for item in sublist]

for item in újabb_lista:
    print(item)
