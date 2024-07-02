carro = {
    "modelo" : "Renegade",
    "ano" : 2021,
}

print(carro)

print(carro["modelo"])

carro["cor"] = "Prata"
print(carro)
#del carro["ano"]
print(carro["modelo"])

carro2 = {
    "modelo" : "Doblo",
    "ano" : 2006,
    "cor" : "Preto"
}

carro3 = {
    "modelo" : "Uno",
    "ano" : 2003,
    "cor" : "Branco"
}
frota = (carro, carro2)
print("----------------------")
print(frota)

carro2["modelo"] = carro3["modelo"]
print(frota)