define n = Character('Narrador', color="#BEBEBE")
define r = Character('Recepcionista', color="#DDA0DD")
define b = Character('Bartender', color = "#8FBC8F")
define w = Character('Lord Wayne', color = "#D3D3D3")
define d = Character('Político Desconhecido', color = "#EE82EE")


image personagem taberneiro = "Bartender.png"
image personagem cultista = "Cultista.png"
image personagem padrinho = "Padrinho.png"
image personagem politico = "Político.png"
image personagem sombra = "Sombra.png"
image bg capa = "capa.png"
image bg black = "#000000"
image bg bar = "Bar.png"
image bg bibliotecaescura = "Biblioteca 1 escura.png"
image bg bibliotecaclara = "Biblioteca 1 clara.png"
image bg bibliotecap = "Biblioteca.png"
image bg camara = "Câmaras.png"
image bg casa = "Casa protagonista.png"
image bg dungeon = "Dungeon.png"
image bg casapadrinho = "Casa padrinho.png"
image bg portapadrinho = "Porta padrinho.png"
image bg hallpadrinho = "Hall padrinho.png"
image bg lanterna = "Lanterna.png"
image bg parque = "Parque.png"
image bg esgotos = "esgotos.png"
image bg gm1 = "Game over01.png"
image bg gm2 = "Game over02.png"
image bg gm3 = "Game over03.png"
image bg gm4 = "Game over04.png"
image bg nending = "Neutral Ending.png"
image bg gending = "Good Ending.png"

# The game starts here.
label splashscreen:
    show Caçada ao Quitute {p} A Conspiraçao Iluminatti
    show bg capa
    with dissolve
    play music "The Other Side of the Door.mp3"
    $ renpy.pause(5.0)
    return

label start:
    scene bg casa
    with dissolve
    stop music
    queue music [ "Deep Haze.mp3", "Oppressive Gloom.mp3" ]
    $ aux = 0
    $ bar = 0
    $ carta = 0
    $ envelope = 0
    $ jornal = 0
    $ esgoto = 0
    $ camara = 0
    $ bibliotecap = 0
    $ gameover = 0
    $ dgpos = 1
    
    n "Seu apartamento."
    n "Nunca foi muita coisa mesmo, principalmente levando em consideração que você mora sozinho."
    n "Logo a sua frente pode-se ver sua sala, com seu velho sofá roído de traças e sua lareira."
    n "Alguns livros se encontram empilhados num canto, visto que você ainda não conseguiu comprar uma estante."
    n "A sua esquerda você pode ver sua cozinha, nas sombras.{w} Seu quarto se encontra no final do corredor. Nada lá além da sua cama,{w} desarrumada, e um pequeno armário."
    n "Hoje é o aniversário do seu padrinho. Como nos últimos anos, você resolve lhe fazer uma visita para almoçar."
    
    menu:
         "Ficar em casa":
              $ gameover = 1
              call Game_Over from _call_Game_Over
                            
         "Ir ao parque":
              jump parque
              n "Você decide passar pelo parque antes."
              
         "Visitar seu padrinho":
              jump padrinho
############################################################             
label houseHub:
  scene bg casa
  with dissolve
  while True:
    menu:
      "Voltar para a casa do seu padrinho":
         call menuPadrinho1 from _call_menuPadrinho1
      "Ir para o bar" if carta == 1:
         call bar from _call_bar
      "Ir para Biblioteca publica" if envelope == 1:
         call bibliotecaPublica from _call_bibliotecaPublica
      "Ir para os esgotos" if jornal== 1:
         call esgotos from _call_esgotos
      "Ir para o camara" if bar == 1:
         call camara from _call_camara
################################################ PARQUE1 ############################################################## 
label parque:  
    scene bg parque
    with dissolve
    n "O parque da cidade é o seu lugar favorito."
    n "Embora não se possa dizer que é bem cuidado, pelo menos te traz boas lembranças. Mas não há muito para fazer por aqui nessa hora do dia."
    
    menu:
        "Voltar para casa":
            jump start
            
        "Visitar seu padrinho":
            jump padrinho
################################################ Entrada na casa do padrinho ##############################################################            
label padrinho:
    scene bg portapadrinho
    with dissolve
    n "Assim que você chega em frente a casa de seu padrinho você percebe que algo está errado."
    n "Ele sempre foi um homem muito organizado e meticuloso, e, apesar de morar sozinho, sua casa sempre esteve em perfeita ordem."
    n "Ele nunca deixaria a porta de entrada aberta."
    n "Você decide entrar logo, sem bater." 
    n "Você se encontra no hall de entrada da casa do seu padrinho."
    n "Mansão, pra dizer a verdade. Só este cômodo tem quase o tamanho do seu apartamento."
    n "Um grande tapete se estende da porta de entrada até uma escadaria encurvada, levando ao segundo andar. Quadros, esculturas, armaduras e tapeçarias forram as paredes. Uma enorme e luxuosa lareira se encontra no fim da sala, ao lado da escada."
    n "As portas para a direita se encontram fechadas, mas você sabe que levam a copa e ao salão de jantar. À esquerda, a porta para o salão de baile se encontra fechada. A segunda porta se encontra entreaberta. Você consegue avistar de relance a primeira estante da extensa biblioteca do seu padrinho."

    jump menuPadrinho1
################################################ Hub da casa do padrinho ##############################################################
label menuPadrinho1:
    scene bg hallpadrinho
    with dissolve
    while True:
      menu:
          "Investigar a copa":
                n "A porta está trancada."
          "Investigar a cozinha":
                n "A porta está trancada."
          "Investigar o salão de bailes":
                n "A porta está trancada."
                if esgoto == 1 and camara == 1 and bibliotecap == 1:
                    n "Porém, você escuta barulhos do outro lado e tenta força-la."
                    jump salaoDeBailes
          "Investigar a Biblioteca":
                n "Por que a porta da biblioteca está aberta?"
                jump biblioteca
          "Voltar para casa" :
                call houseHub from _call_houseHub
################################################ Salão de Bailes ##############################################################
label salaoDeBailes:
    scene bg lanterna
    with dissolve
    n " Você acha uma lanterna encostada perto da porta, acende, e começa a perambular."
    while True:
        menu:
            "Examinar o salão":
                n "Embora o ambiente pareça vazio, você descobre que na verdade todos os móveis estão empilhados nos cantos da sala, como se tivessem sido empurrados para abrir espaço no meio."
                
            "Examinar os móveis":
                n "Você aproxima sua lanterna dos vários móveis. Mesas, cadeiras, um ou outro vaso ou decoração. Nada chama sua atenção."
          
            "Examinar as cortinas":
                n "Não tem nada de mais nas cortinas. Mas elas são pesadas demais para você se dar ao trabalho de abrir todas."
   
            "Examinar o piso":
                n "Você aproxima sua lanterna do chão e começa a procurar por alguma coisa fora do comum.{p}Ao cruzar o meio da sala, o som dos seus passos muda.{w}O piso do meio do salão é de madeira, diferente do resto."
                n "Uma pequena alavanca, inteligentemente escondida, lhe dá acesso a um escuro lance de escadas."
                jump dungeon
   
            "Voltar":
                jump menuPadrinho1

################################################ Biblioteta particular ##############################################################
label biblioteca:   

    n "Você está na biblioteca colossal da mansão do seu padrinho. Nunca você viu tanto papel num mesmo lugar."
    n "Devem haver centenas de livros aqui, e com certeza ele não deve ter lido todos."
    n "Uma aconchegante lareira se encontra no canto direito, ainda com algumas brasas. Na frente dela duas poltronas de feltro fornecem conforto para possíveis leitores. Uma mesa de escritório se encontra no canto esquerdo."
    n "Estranhamente, apesar da organização militar de seu padrinho, há vários papéis espalhados sobre a mesa e a cadeira."
    while True:
       menu:
           "Examinar papéis" if aux == 0:
              scene bg bibliotecaescura
              with dissolve
              n "Você examina os papéis, mas o cômodo está muito escuro para você ler qualquer coisa. [aux]"
              $ aux += 1

           "Reavivar lareira" if aux == 1:
              n "As brasas estão frias demais para você poder reavivá-las."
              $ aux += 1

           "Acender uma vela" if aux == 2:
              scene bg bibliotecaclara
              with dissolve
              n "Agora sim, com a vela em mãos você consegue finalmente ler os papéis."
              n "A maior parte são correspondências, endereçadas ao seu padrinho. O jornal diário, edição de dois dias atrás, também está junto. Um pequeno envelope marrom se encontra no fundo da pilha."
              $ aux += 1

           "Examinar carta" if aux > 2:
              scene bg bibliotecaclara
              with dissolve
              n "As duas primeiras são propagandas. A terceira é um relatório de investimentos. A quarta te chama a atenção: Num papel timbrado, de alta qualidade, um convite para jantar. O que te causa estranhamento, na verdade, não é o convite em si."
              n "Seu padrinho é um homem público, afinal. Mas o local no convite é um pequeno bar, de baixa classe, localizado na esquina do cartório."
              n "Nem você nunca entrou nesse lugar, achando que ele não possuia boa aparência. Uma carta de tão boa qualidade convidando para um local tão medíocre, e ainda por cima sem remetente, não é algo que se vê todo dia."
              n "A data do convite foi ontem a noite. Talvez ainda valha a pena investigar o bar."
              $ carta = 1
           "Examinar o envelope" if aux > 2: 
              scene bg bibliotecaclara
              with dissolve
              n "Um envelope pequeno e uniforme. Ao abri-lo, você encontra o cartão de biblioteca de seu padrinho."
              n "Parece que ele está com um livro em atraso, o que não faz sentido, conhecendo seu padrinho."
              n "O que será que ele estava lendo?"
              $ envelope = 1
           "Examinar o jornal" if aux > 2:
              scene bg bibliotecaclara
              with dissolve
              n "Você resolve abrir o jornal. Nada te salta aos olhos a princípio. Porém, perdido nas páginas internas, uma notícia foi marcada a tinta: É uma nota de fim de página sobre a paralisação das obras de reformas dos esgotos do bairro, após o desaparecimento do terceiro funcionário em três semanas."
              n "Porque seu padrinho estaria interessado nos desaparecimentos de funcionários de manutenção da rede de esgotos?"
              $ jornal = 1
           "Voltar":
              call menuPadrinho1 from _call_menuPadrinho1_1
################################################ Biblioteta Publica ##############################################################
label bibliotecaPublica:
  scene bg bibliotecap
  with dissolve
  n "A biblioteca pública. Um prédio cinzento de mármore lúgrebe. Você nunca realmente veio aqui antes, afinal, nunca precisou. Estantes enormes, de dois andares de altura, ocupam todas as paredes. Pequenas mesas de leitura ocupam corredores no centro do prédio. Logo a sua frente está a recepcionista. Todo o lugar está bastante vazio, na verdade. "
  n "Você não vê ninguém além da recepcionista. Você não deve ser o único a não gostar de ler."
  
  menu:
   "Perguntar à recepcionista sobre o material achado":
     n "Você se aproxima da recepcionista, que está entretida com um livro de bolso. Ela olha para você quando se aproxima:"
     r "Pois não?"
     n "Você explica, de forma resumida, que encontrou o cartão da biblioteca de seu padrinho e viu que ele estava devendo um livro. Mas, como você não achou o livro em lugar nenhum, veio aqui para conseguir mais detalhes."
     n "A funcionária se mostra um pouco incomodada com o fato, afinal o livro já está com quase uma semana de atraso, e desaparecido. Ainda assim, ela te indica o nome da obra."
     n "Você pede para ver outra edição do livro, para poder facilitar na sua busca, e ela te indica a seção correta."
     n "O livro é um estranho e antigo tomo sobre demonologia. Segundo a introdução, foi escrito para ajudar a identificar e combater diversos males sobrenaturais que poderiam ser liberados sobre a humanidade. "
     n "Por que diabos seu padrinho estaria interessado em tal crendice?"
     n "..."
     n "Você se despede da recepcionista, prometendo procurar o livro perdido, e volta pra casa."
     $ bibliotecap = 1
     call houseHub from _call_houseHub_1
################################################ Bar ##############################################################
label bar:
  scene bg bar
  with dissolve
  n "Este pequeno bar nunca realmente chamou sua atenção. Escondido entre uma alfaiataria e uma loja de penhores, e a janela está sempre tão suja de fuligem que não se enxerga através."
  n "O ambiente interno també não tem nada de mais."
  n "Alguns banquinhos comuns se encontram na frente do balcão. Na parede, por toda extensão do bar, pequenas mesas com cadeiras estofadas concentram a maioria dos clientes."
  n "O bartender está de costas para você, pegando alguma coisa da estante. Nesse horário o bar não está muito cheio."
  while True:
      show taberneiro
      menu:
       "Conversar com o bartender":
          n "Você pergunta ao bartender se ele por acaso conhece seu padrinho, por nome."
          n "Ele responde negativamente"
          n "Você então pergunta, descrevendo sua aparência"
          n "Ele responde que nenhum dos regulares se encaixa nessa descrição, e ele infelizmente não consegue se lembrar de todos os clientes."
          n "Mudando de técnica, você pergunta se ele se lembra de dois senhores bem vestidos, um deles este seu padrinho, que se encontraram no bar na noite anterior."
          b "Bem, conhecendo minha clientela, dizer que são bem vestidos já elimina a metade."
          b "As únicas pessoas assim que vieram na noite passada foram o Lorde Wayne e um convidado."
          b "Pensando bem, este convidado cabia na descrição do seu padrinho..."
          n "Voce agradece pela ajuda, mas sai ainda mais confuso."
          n "Será que o estimado Lorde Wayne saberia me explicar o desaparecimento do meu padrinho? Talvez devesse encontrá-lo na câmara. "
          n "Se correr posso chegar antes do almoço. Você pensa."
          $ bar = 1
       "Pedir uma bebida":
          n "Você se aproxima do balcão e pede uma cerveja. O bartender deixa de lado o que estava fazendo para te servir. "
       "Voltar para casa":
          jump houseHub



################################################ Esgotos ##############################################################

label esgotos:
  scene bg esgotos
  n "Você entra nos esgotos, descendo uma série de escadas na margem do rio."
  n "O túnel que você se encontra é bem pequeno, sua cabeça quase toca o teto."
  n "Você vira a esquerda."
  n "Esse túnel está todo tomado de musgos, revestindo as paredes."
  n "A passagem está bloqueada para a direita, então você vira a esquerda."
  n "O ambiente é muito escuro, você não tem certeza onde está pisando, e um fio de água passa pelo meio do túnel, fazendo com que seus passos façam muito barulho"
  n "De repete, o ambiente começa a clarear."
  n "Existe uma abertura no lado esquerdo, por onde passa uma fraca luz. Alguma coisa parece estranha sobre este local."
  menu:
   "Entrar na abertura":
      n "Quando você acaba de entrar no aposento, percebe que cometeu um gravíssimo erro."
      n "Mas já era tarde demais."
      n "Ao tentar escapar, sente em suas costas uma enorme e grossa........faca, e sua vida se esvai."
      show cultista
      $ gameover = 2
      call Game_Over from _call_Game_Over_1
   "Espiar o aposento":
      n "Lentamente, agachado, você se aproxima da abertura."
      n "O aposento a sua frente é bem grande, semicircular e revestido de pedras."
      show cultista
      n "Um grupo de talvez nove pessoas, cobertas com túnicas roxas, se encontra no centro."
      n "Eles estão cantando numa língua desconhecida para você, e parecem estar em transe. No meio do círculo uma figura solitária se contorce no chão. "
      n "Uma mulher, nua, de não mais de 20 anos. Conforme o canto chega a seu ápice, uma das figuras se separa do grupo e avança, ameaçadoramente, em direção a mulher no chão."
      menu:
       "Tentar intervir":
        n "Você entra heroicamente na sala, gritando com a força de mil sóis queimantes. Mas rapidamente alguém saca uma escopeta e te mata."
        $ gameover = 3
        call Game_Over from _call_Game_Over_2
       "Manter a discreção":
        n "De algum lugar nas dobras de seu manto ele saca uma adaga de aparência sinistra, que, com toda força, desce no peito da moça."
        n "Ela solta um grito aterrorizante, por apenas um momento, e então se cala."
        n "Atordoado, você percebe que todos se encontram em silêncio. O assassino, no centro do círculo, remove seu capuz."
        n "Você senta, atordoado. Não consegue crer no que viu."
        n "O assassino não é ninguém menos que Lorde Wayne, líder político e mais forte candidato a sucessão do primeiro ministro!!!"
        n "Rápido, mas silenciosamente, você retorna a superfície."
        $ esgoto = 1
        call houseHub from _call_houseHub_2
################################################### Câmara ###################################################################

label camara:
    scene bg camara
    with dissolve
    n "Você está de frente a câmara."
    n "Uma grande construção, a segunda mais antiga da cidade, foi o centro da vida política da região desde sempre."
    n "Pelo menos até onde você sabe."
    n "As escadas levam a um par de portas de carvalho, tão enceradas que são quase um espelho. O pouco do hall que você consegue ver daqui está cheio de gente, de um lado para o outro."
    n "Você se encontra na principal sala de audiências. Está vazio agora, a próxima sessão começando em um hora."
    n "Diversas cadeiras se organizam em fileiras perfeitamente simétricas. Toda a pompa foi utilizada na decoração do ambiente. Você se move rumo ao fundo da sala, onde uma cortina a separa da antessala."
    n "Conforme se aproxima, você percebe duas pessoas conversando do outro lado da sala, sendo que a primeira é exatamente quem você veio procurar."
    
    menu:
        "Se aproximar silenciosamente":
           if esgoto == 0:
            show politico
            show cultista
            d "...e é por isso que nós devemos agir rápido."
            n "Você reconhece essa voz, é a daquele político famoso e renomado discursante, Lorde Wayne."
            w "Não podemos esperar nem mais um dia, o ritual deve ser realizado esta noite. Como vão os preparativos?"
            n "... Ritual?"
            d "Meu senhor, falta apenas o últimos sacrifício, no último nexus."
            n "...Nexus? ...Sacrifício?"
            n "Essa voz não me é familiar, mas não me atrevo a mover, com medo de ser percebido."
            w "Eu mesmo tomarei conta disso. Reúna todos, estarei lá."
            d "Sim, meu senhor. Depois iremos imediatamente para a mansão do Campo Alto?"
            n "Meu padrinho mora no Campo Alto!"
            w "Imediatamente. Não disse que não temos tempo a perder? Agora vá, te encontro mais tarde."
            d "Senhor."
            n "Você escuta se levantarem e começaram a andar. Felizmente não vêm em sua direção. O que era essa conversa de rituais e sacrifícios?"
            $ camara = 1
            call houseHub from _call_houseHub_3
            
           if esgoto == 1:
            show politico
            show cultista
            d "...e é por isso que nós devemos agir rápido."
            n "Você reconhece essa voz, é aquele maldito Lorde Wayne."
            w "Não podemos esperar nem mais um dia, o ritual deve ser realizado esta noite. Como vão os preparativos?"
            n "... Ritual?"
            d "Meu senhor realizou o último sacrifício, no último nexus."
            n "...Nexus? ...Sacrifício? Foi isso aquela loucura que você presenciou nos esgotos?"
            w "Bom saber, nos dirigiremos diretamente para a mansão no Campo Alto esta noite."
            n "Meu padrinho mora no Campo Alto!"
            d "Senhor! Não prefere se preparar melhor, esperar a chegada de todos os acólitos?"
            n "Essa voz não me é familiar, mas não me atrevo a mover, com medo de ser percebido."
            w "Imediatamente. Não disse que não temos tempo a perder? Agora vá, te encontro mais tarde."
            d "Senhor."
            n "Você escuta se levantarem e começaram a andar. Felizmente não vêm em sua direção. O que era essa conversa de rituais e sacrifícios?"
            $ camara = 1
            call houseHub from _call_houseHub_4
        "Puxar a cortina":
            n "Você puxa abruptamente a cortina."
            n "Do outro lado está Lorde Wayne, e um homem que você não conhece em robes roxo escuro."
            n "“A há!”, você diz, apontando o dedo na cara do Lorde. Mais rápido que você consegue ver, o outro homem saca uma adaga e enfia na sua garganta."
            $ gameover = 4
            call Game_Over from _call_Game_Over_3
######################################## Game Over     ######################################
label Game_Over:
  stop music
  play music "Unlight.mp3"
  if gameover == 1:
    show bg gm1
    with dissolve
    n "VOCÊ CONTINUOU COM A SUA VIDINHA PATÉTICA, ATÉ QUE O MUNDO FOI DESTRUÍDO"
    $ renpy.pause(20.0)
    jump start
  if gameover == 2:
    show bg gm2
    with dissolve
    n "SURPRESA!"
    $ renpy.pause(20.0)
  if gameover == 3:
    show bg gm3
    with dissolve
    n "NÃO SÓ MORREU, COMO CONDENOU O MUNDO A PERDIÇÃO. TROUXA."
    $ renpy.pause(20.0)
  if gameover == 4:
    show bg gm4
    with dissolve
    n "MALDITA ALERGIA"
    $ renpy.pause(20.0)
  if gameover == 5:
    show bg gm3
    with dissolve
    n "NÃO É ESSE TIPO DE JOGO"
    $ renpy.pause(20.0)
  if gameover == 6:
    n "VOCÊ MORREU, E GARANTIU O FIM DA HUMANIDADE"
    show bg gm3
    with dissolve
    $ renpy.pause(7.0)
  if gameover == 7:
    n "A INVOCAÇÃO DEU CERTO E O NOSSO UNIVERSO ESTÁ CONDENADO"
    show bg gm3
    with dissolve
    $ renpy.pause(7.0)
  if gameover == 8:
    #NEUTRAL ENDING
    n "VOCÊ MORREU, MAS SALVOU A HUMANIDADE"
    show bg nending
    with dissolve
    $ renpy.pause(7.0)
  if gameover == 9:
    #NEUTRAL ENDING
    n "VOCÊ IMPEDIU O FIM DO MUNDO... POR ENQUANTO."
    show bg nending
    with dissolve
    $ renpy.pause(7.0)
  if gameover == 10:
    #GOOD ENDING
    n "O MUNDO FOI SALVO, PARABÉNS"
    show bg gending
    show Reiniciando Caçada ao Quitute
    with dissolve
    $ renpy.pause(7.0)
######################################## DIALOGO PAD   ######################################
$ dgpos = 4
jump dungeon
######################################## DUNGEON FINAL ######################################
label dungeon:
    scene bg dungeon
    play music "Metaphysik.mp3"
    if dgpos == 1:
        n "Você se encontra no pé da escada, numa pequena sala revestida de pedra."
        n "Um corredor começa a sua frente, rumo norte, mas você não consegue ver onde termina."
        menu:
            "Andar norte": 
                $ dgpos = 2
                jump dungeon
    if dgpos == 2:
        n "Tem uma teia de aranha enorme num canto da sala. O fato de você não ver a aranha só te deixa ainda mais nervoso."
        n "Há duas saídas, a leste e oeste."
        menu:
            "Andar leste":
                $ dgpos = 11
                jump dungeon
            "Andar oeste":
                $ dgpos = 3
                jump dungeon
    if dgpos == 3:
        n "Uma tocha no canto deixa essa junção bem iluminada."
        n "Você pode seguir pro norte ou leste."
        menu:
            "Andar norte":
                $ dgpos = 6
                jump dungeon
            "Andar leste":
                $ dgpos = 4
                jump dungeon
    if dgpos == 4:
        n "Não há nada de especial aqui."
        n "Você pode seguir para o sul ou oeste."
        menu:
            "Andar sul":
                $ dgpos = 5
                jump dungeon
            "Andar oeste":
                $ dgpos = 3
                jump dungeon
    if dgpos == 5:
        n "Essa sala parece uma masmorra.{p}A sua direita e esquerda há diversas celas, todas vazias."
        n "Você consegue ver movimento na cela no fim do corredor. Você se aproxima da cela, e realmente, tem alguém encolhido no canto."
        n "A figura se levanta quando você se aproxima,{w} e você percebe que se trata do seu padrinho."
        n "Suas roupas estão imundas e seu rosto é o de alguém que não se alimenta bem a semanas."
        jump dialogopad
    if dgpos == 6:
        n "Você está num corredor escuro e apertado."
        n "A única saída é ao norte."
        menu:
            "Andar norte":
                $ dgpos = 7
                jump dungeon
    if dgpos == 7:
        n "Está câmara está coberta de poeira. Parece que ninguém passa aqui em muito tempo."
        n "Você pode seguir a leste e oeste."
        menu:
            "Andar leste":
                $ dgpos = 8
                jump dungeon
            "Andar oeste":
                $ dgpos = 14
                jump dungeon
    if dgpos == 8:
        n "Esse corredor é tão estreito que você tem que passar de lado."
        n "Os único caminhos são rumo leste e oeste."
        menu:
            "Andar leste":
                $ dgpos = 9
                jump dungeon
            "Andar oeste":
                $ dgpos = 7
                jump dungeon
    if dgpos == 9:
        n "Nessa região os túneis se dividem em três direções, norte, leste e sul."
        menu:
            "Andar norte":
                $ dgpos = 13
                jump dungeon
            "Andar leste":
                $ dgpos = 8
                jump dungeon
            "Andar sul":
                $ dgpos = 10
                jump dungeon
    if dgpos == 10:
        n "Este corredor é igual todos os outros."
        n "A única saída é sul."
        menu:
            "Andar sul":
                $ dgpos = 11
                jump dungeon
    if dgpos == 11:
        n "Está parte dos túneis está meio colapsada."
        n "Você pode ver passagens ao norte, leste e oeste.{w}A passagem a sul está bloqueada com entulho."
        menu:
            "Andar norte":
                $ dgpos = 10
                jump dungeon
            "Andar leste":
                $ dgpos = 12
                jump dungeon
            "Andar oeste":
                $ dgpos = 2
                jump dungeon
    if dgpos == 12:
        n "O resto desse túnel está fechado por um desmoronamento. Há várias coisas espalhadas pelo chão."
        n "Você só pode voltar para o oeste"
        menu:
            "Andar oeste":
                $ dgpos = 11
                jump dungeon
    if dgpos == 13:
        n "Existe uma pequena grade de ventilação no canto esquerdo dessa sala. Fora isso, não há nada de interesse aqui."
        n "Sua única saída é ao sul"
        menu:
            "Andar sul":
                $ dgpos = 9
                jump dungeon
    if dgpos == 14:
        n "Você tem que passar com cuidado por aqui, já que não se enxerga um palmo na frente do nariz."
        n "Só pode seguir norte ou voltar à leste."
        menu:
            "Andar leste":
                $ dgpos = 7
                jump dungeon
            "Andar norte":
                $ dgpos = 15
                jump dungeon
    if dgpos == 15:
        n "Outro corredor apertado. Isso está ficando monótono."
        n "Você só pode seguir norte ou sul"
        menu:
            "Andar norte":
                $ dgpos = 16
                jump dungeon
            "Andar sul":
                $ dgpos = 14
                jump dungeon
    if dgpos == 16:
        n "Nesse corredor um par de cultistas com tochas mantém vigília."
        n "Uma caixa grande de papelão está jogada num canto."
        n "Seu caminho está bloqueado ao norte, só pode voltar ao sul"
        menu:
            "Andar norte":
                $ gameover = 3
                jump Game_Over
            "Andar sul":
                $ dgpos = 15
                jump dungeon
            "Tentar passar pelos cultistas":
                n "Os cultistas não parecem muito espertos, ou fortes. Além do mais, essa caixa pode ser útil."
                menu:
                    "Usar caixa":
                        n "Você se esconde embaixo da caixa, e começa a rastejar lentamente em direção a porta."
                        n "Incrivelmente, os guardas não percebem nada."
                        n "Mas é uma pena que você seja alérgico a poeira, e solta um espirro monumental."
                        n "Imediatamente, o cultista mais próximo te dá um forte chute, te atingindo bem na cabeça.{w} O mundo escurece."
                        $ gameover = 4
                        jump Game_Over
                    "Não usar caixa":
                        n "Isso seria estúpido demais, nem esses guardas cairiam."
                        n "Você resolve enfrentá-los no braço mesmo.{p} Você chega gritando, balançando os braços, e corre em direção aos cultistas."
                        n "O mais próximo, sem nem te olhar, te dá um soco de direita entre os olhos. O mundo escurece."
                        $ gameover = 5
                        jump Game_Over
                        