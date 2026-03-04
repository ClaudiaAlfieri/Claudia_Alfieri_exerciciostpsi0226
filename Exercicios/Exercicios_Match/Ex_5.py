
# Recebe uma mensagem e retorna:
# •	“Saudação” se for “olá” ou “bom dia”
# •	“Pergunta” se terminar com “?”
# •	“Despedida” se contiver “tchau” ou “adeus”
# •	“Mensagem genérica” caso contrário

msg = input("Digite uma mensagem: ").lower()

if msg == "olá" or msg == "bom dia":
    print("Saudação")
elif msg.endswith("?"):
    print("Pergunta")
elif "tchau" in msg or "adeus" in msg:
    print("Despedida")
else:
    print("Mensagem genérica")