numero_placa = input("manda o numero final da placa do veiculo: ")
 
match numero_placa:
     case "1" | "2": print("Rodizio na segunda-feira")
     case "3" | "4": print("Rodizio na terça-feira")
     case "5" | "6": print("Rodizio na quarta-feira")
     case "7" | "8": print("Rodizio quinta-feira")
     case "9" | "0": print("Rodizio na sexta-feira")
     case _: print ("final de placa inválido")
     