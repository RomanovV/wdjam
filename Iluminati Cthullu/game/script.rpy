# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.

define n = Character('Narrador', color="#c8ffc8")

image personagem taberneiro = "garçoUMMMM.png"
image tela = "tela.png"

label houseHub(carta=0, envelope=0, jornal=0):
  while True:
    menu:
      "Voltar para a casa do seu padrinho":
         jump menuPadrinho1
      "Ir para o bar" if carta == 1:
         call expression "bar" pass (algo)
      "Ir para Bivlioteca publica" if envelope == 1:
         call expression "bibliotecaPublica" pass (outro_algo)
      "Ir para os esgotos" if jornal== 1:
          call expression "esgotos" pass (mais_um_algo)

# The game starts here.
label start:
    n "Seu apartamento. Nunca foi muita coisa mesmo, principalmente levando em consideração que você mora sozinho. Logo a sua frente pode-se ver sua sala, com seu velho sofá roído de traças e sua lareira. Alguns livros se encontram empilhados num canto, visto que você ainda não conseguiu comprar uma estante. A sua esquerda você pode ver sua cozinha, nas sombras. Seu quarto se encontra no final do corredor. Nada lá além da sua cama, desarrumada, e um pequeno armário."

    n "Hoje é o aniversário do seu padrinho. Como nos últimos anos, você resolve lhe fazer uma visita para almoçar."
    
    menu:
         "Ficar em casa":
              jump gameOver1
              
         "Ir ao parque":
              jump parque
              
         "Visitar seu padrinho":
              jump padrinho
################################################ PARQUE1 ############################################################## 
label parque:  
    n "O parque da cidade é o seu lugar favorito. Embora não se possa dizer que é bem cuidado, pelo menos te traz boas lembranças. Mas não há muito para fazer por aqui nessa hora do dia."
    
    menu:
        "Voltar para casa":
            jump start
            
        "Visitar seu padrinho":
            jump padrinho
################################################ Entrada na casa do padrinho ##############################################################            
label padrinho:
    n "Assim que você chega em frente a casa de seu padrinho você percebe que algo está errado. Ele sempre foi um homem muito organizado e meticuloso, e apesar de morar sozinho sua casa estava sempre em perfeita ordem. Ele nunca deixaria a porta de entrada aberta."
    n "Você se encontra no hall de entrada da casa do seu padrinho."
    n "Mansão, mais exatamente. Só este cômodo tem quase o tamanho do seu apartamento. Um grande tapete se estende da porta de entrada até uma grande escadaria encurvada, levando ao segundo andar. Quadros, esculturas, armaduras e tapeçarias forram as paredes. Uma enorme e luxuosa lareira se encontra no fim da sala, ao lado da escada."
    n " As portas para a direita se encontram fechadas, mas você sabe que levam a copa e ao salão de jantar. À esquerda, a porta para o salão de baile se encontra fechada. A segunda porta se encontra aberta. Você consegue avistar de relance a primeira estante da enorme biblioteca do seu padrinho."

    jump menuPadrinho1
################################################ Hub da casa do padrinho ##############################################################
label menuPadrinho1(carta=0, envelope=0, jornal=0):
    n " carta [carta]"
    n "envelope [envelope]"
    n "jornal [jornal]"
    menu:
        "Investigar a copa":
              n "A porta está trancada."
              jump menuPadrinho1
        "Investigar a cozinha":
              n "A porta está trancada."
              jump menuPadrinho1
        "Investigar o salão de bailes":
              n "Você abre a porta, mas tudo está escuro."
              n "Todas as cortinas devem estar fechadas. Fora isso, o cômodo parece estar vazio."
              jump salaoDeBailes
        "Investigar a Biblioteca":
              jump biblioteca
        
        "Voltar para casa" :
              call houseHub(carta, envelope, jornal)
################################################ Salão de Bailes ##############################################################
label salaoDeBailes:
     $ salaoDeBailes_first_time = True
     if salaoDeBailes_first_time:
        n " Você acha uma lanterna encostada perto da porta, acende, e começa a perambular."
        menu:
            "Examinar o salão":
                n "Dessa vez você se dá ao trabalho de examinar o salão de bailes. Embora o ambiente tenha parecido vazio antes, você descobre que na verdade todos os móveis estão empilhados nos cantos da sala, como se tivessem sido empurrados para abrir espaço no meio."
                jump salaoDeBailes
                $ salaoDeBailes_first_time = False
            "Examinar os móveis":
                n "Você aproxima sua lanterna dos vários móveis. Mesas, cadeiras, um ou outro vaso ou decoração. Nada chama sua atenção."
                jump salaoDeBailes
                $ salaoDeBailes_first_time = False
            "Examinar as cortinas":
                n "Não tem nada de mais nas cortinas. Mas elas são pesadas demais para você se dar ao trabalho de abrir todas."
                jump salaoDeBailes
                $ salaoDeBailes_first_time = False
            "Examinar o piso":
                n "Você aproxima sua lanterna do chão e começa a procurar por alguma coisa for a do comum. Ao cruzar o meio da sala, o som dos seus passos muda. O piso do meio do salão é de madeira, diferente do resto. Uma pequena alavanca, inteligentemente escondida, lhe dá acesso a um escuro lance de escadas."
                jump salaoDeBailes
                $ salaoDeBailes_first_time = False
            "Voltar":
                jump menuPadrinho1
                $ salaoDeBailes_first_time = False
     else:
        menu:
            "Examinar o salão":
                n "Dessa vez você se dá ao trabalho de examinar o salão de bailes. Embora o ambiente tenha parecido vazio antes, você descobre que na verdade todos os móveis estão empilhados nos cantos da sala, como se tivessem sido empurrados para abrir espaço no meio."
                jump salaoDeBailes
            "Examinar os móveis":
                n "Você aproxima sua lanterna dos vários móveis. Mesas, cadeiras, um ou outro vaso ou decoração. Nada chama sua atenção."
                jump salaoDeBailes
            "Examinar as cortinas":
                n "Não tem nada de mais nas cortinas. Mas elas são pesadas demais para você se dar ao trabalho de abrir todas."
                jump salaoDeBailes
            "Examinar o piso":
                n "Você aproxima sua lanterna do chão e começa a procurar por alguma coisa for a do comum. Ao cruzar o meio da sala, o som dos seus passos muda. O piso do meio do salão é de madeira, diferente do resto. Uma pequena alavanca, inteligentemente escondida, lhe dá acesso a um escuro lance de escadas."
                jump salaoDeBailes
################################################ Biblioteta particular ##############################################################
label biblioteca:
    $ biblioteca_first_time = True
    $ aux = 0
    $ carta = 0
    $ envelope = 0
    $ jornal = 0
    while True:
     if biblioteca_first_time:
       n "Você está na biblioteca colossal da mansão do seu padrinho. Nunca você viu tanto papel num mesmo lugar. Deve haver centenas de livros aqui, e com certeza ele não tem como ter lido a todos. Uma aconchegante lareira se encontra no canto direito, ainda com algumas brasas. Na frente dela duas poltronas de feltro fornecem conforto para possíveis leitores. Uma mesa de escritório se encontra no canto esquerdo. Estranhamente, apesar da organização militar de seu padrinho, há vários papéis espalhados sobre a mesa e a cadeira."
       $ biblioteca_first_time = False
       menu:
        "Examinar papéis" if aux == 0:
          n "Você pega os papéis, mas o cômodo está muito escuro para você ler qualquer coisa. [aux]"
          $ aux += 1

        "Reavivar lareira" if aux == 1:
          n "As brasas estão frias demais para você poder reavivá-las."
          $ aux += 1

        "Acender uma vela" if aux == 2:
          n "Agora sim, com a vela em mãos você consegue finalmente ler os papéis. A maior parte são correspondências, endereçadas ao seu padrinho. O jornal do dia, de dois dias atrás, também estava junto. Um pequeno envelope marrom está no fundo da pilha."
          $ aux += 1

        "Examinar carta" if aux > 2:
          n "As duas primeiras são propagandas. A terceira é um relatório de investimentos. A quarta te chama a atenção. Num papel timbrado, de alta qualidade, um convite para jantar. O que te causa estranhamento, na verdade, não é o convite em si. Seu padrinho é um homem público, afinal. Mas o local no convite é um pequeno bar, de baixa classe, localizado na esquina do cartório. Você mesmo nunca entrou no lugar, não achando que ele possua uma boa aparência. Uma carta de tão boa qualidade convidando para um local tão medíocre, ainda por cima sem identificação do remetente, não é algo que se vê todo dia.A data do convite foi ontem a noite. Talvez ainda valha a pena investigar o bar."

        "Examinar o envelope" if aux > 2: 
          n "Um envelope pequeno e uniforme. Ao abri-lo, você encontra o cartão de biblioteca de seu padrinho. Parece que ele está com um livro em atraso, o que não faz sentido, conhecendo seu padrinho. O que será que ele estava lendo?"

        "Examinar o jornal" if aux > 2:
          n "Você resolve abrir o jornal. Nada te salta aos olhos no princípio. Porém, perdido nas páginas mais internas, uma notícia foi marcada a tinta. É uma nota de fim de página sobre a paralisação das obras de reformas dos esgotos do bairro, após o desaparecimento do terceiro funcionário em três semanas.Porque seu padrinho estaria interessado nos desaparecimentos de funcionários de manutenção da rede de esgotos?"
     else:
       menu:
        "Examinar papéis" if aux == 0:
          n "Você pega os papéis, mas o cômodo está muito escuro para você ler qualquer coisa. [aux]"
          $ aux += 1

        "Reavivar lareira" if aux == 1:
          n "As brasas estão frias demais para você poder reavivá-las."
          $ aux += 1

        "Acender uma vela" if aux == 2:
          n "Agora sim, com a vela em mãos você consegue finalmente ler os papéis. A maior parte são correspondências, endereçadas ao seu padrinho. O jornal do dia, de dois dias atrás, também estava junto. Um pequeno envelope marrom está no fundo da pilha."
          $ aux += 1

        "Examinar carta" if aux > 2:
          n "As duas primeiras são propagandas. A terceira é um relatório de investimentos. A quarta te chama a atenção. Num papel timbrado, de alta qualidade, um convite para jantar. O que te causa estranhamento, na verdade, não é o convite em si. Seu padrinho é um homem público, afinal. Mas o local no convite é um pequeno bar, de baixa classe, localizado na esquina do cartório. Você mesmo nunca entrou no lugar, não achando que ele possua uma boa aparência. Uma carta de tão boa qualidade convidando para um local tão medíocre, ainda por cima sem identificação do remetente, não é algo que se vê todo dia.A data do convite foi ontem a noite. Talvez ainda valha a pena investigar o bar."
          #libera o bar
          $ carta = 1
          n "carta [carta]"

        "Examinar o envelope" if aux > 2: 
          n "Um envelope pequeno e uniforme. Ao abri-lo, você encontra o cartão de biblioteca de seu padrinho. Parece que ele está com um livro em atraso, o que não faz sentido, conhecendo seu padrinho. O que será que ele estava lendo?"
          #libera a bibliotecaPublica
          $ envelope = 1
          n "envelope [envelope]"

        "Examinar o jornal" if aux > 2:
          n "Você resolve abrir o jornal. Nada te salta aos olhos no princípio. Porém, perdido nas páginas mais internas, uma notícia foi marcada a tinta. É uma nota de fim de página sobre a paralisação das obras de reformas dos esgotos do bairro, após o desaparecimento do terceiro funcionário em três semanas.Porque seu padrinho estaria interessado nos desaparecimentos de funcionários de manutenção da rede de esgotos?"
          #libera os Esgotos
          $ jornal = 1
          n "jornal [jornal]"
          
        "Voltar":
           call menuPadrinho1(carta, envelope, jornal)
label bibliotecaPublica:
  n "Biblioteca publica"
label bar:
  n "bar"
label esgotos:
  n "esgotos"

return