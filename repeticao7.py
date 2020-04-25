# 3 questoes multipla escolha, onde a respota da primeira é b, da segunda a e da terceira D. 
# Para cada resposta certa 1 ponto

pontos = 0
questao = 1

while questao <= 3:
    resposta = input ("Resposta da questão %d: " % questao)

    if questao == 1 and resposta == "b" or resposta == "B":
        pontos = pontos + 1
    
    if questao == 2 and resposta == "a" or resposta == "A":
        pontos = pontos + 1
    
    if questao == 3 and resposta == "c" or resposta == "C":
        pontos = pontos + 1
    
    questao + 1
print ("O aluno fez %d ponto (s)" % pontos)