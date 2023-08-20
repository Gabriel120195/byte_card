from model import Cartao

visa = Cartao("1111 2222 3333 4444", "08/2030","123", 20000.00, "Walter White")
masterCard = Cartao("9999 8888 7777 6666", "01/29", "987", 10000.00, "Saul Goodman")

visa.limite = 5000.00
masterCard.limite = 7500.00

print(visa.limite)
print(masterCard.limite)