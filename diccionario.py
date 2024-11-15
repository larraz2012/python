dicionario={"lol" : "algo gracioso",
            "cringe":"algo em barazoso",
            "sheesh":"ligera desaprobacion",
            "creepy":"ateerador",
            "aggro":"ponerse violento",
            "rofl":"una respuesta a una broma",
}

word = input("escribe la palabra que no sepas")

if word in dicionario.keys():
    print(dicionario[word])

else:
    print("esa palabra no esta en este diccionario")
