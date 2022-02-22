#Quantas vezes o jogador ganhou (tirou carta maior que o programa);
#Quantas vezes o jogador perdeu;
#Quantas vezes ambos empataram;
#Quantas vezes tiraram cartas do mesmo naipe.

# Um baralho comum tem 52 cartas de 4 naipes
# de 1 (ás) até 13 (rei) variando de “ouros”, “paus”, “espadas” e “copas”

#O jogador deve pegar uma carta ou terminar o jogo
#(escolha como ele dirá que quer terminar).
#O programa mostra a ele qual foi a carta e depois retira outra carta.
#Quando o Baralho terminar, o jogo acabou e as estatísticas são exibidas.
from baralho import Baralho
from estatistica import Estatistica
from carta import Carta

estatistica = Estatistica()
bar = Baralho()
bar.embaralhar()
print('Pegue uma carta apertando C ou sair apertando X')
letra = input()

while letra != 'X':
    if letra != 'C':
        print('Pressione X (sair) ou C (nova carta) para continuar')
        letra = input()
    else:
        minhaCarta : Carta = bar.retirar_carta()
        carta_oponente: Carta  = bar.retirar_carta()
        estatistica.adicionar_cartas(minhaCarta, carta_oponente)
        print(f'Sua carta é: ' ,  minhaCarta.tipo , minhaCarta.valor)
        print(f'Carta da Maquina: ', carta_oponente.tipo, carta_oponente.valor)
        print('Pressione X (sair) ou C (nova carta) para continuar')
        letra = input()

print('resultado das cartas: ')
estatistica.contabilizar_resultado()
estatistica.printar_resultado()
exit()



