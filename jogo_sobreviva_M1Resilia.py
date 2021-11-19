# Boas vindas
def primeiroPasso():
    print('Seja bem vindo ao Sobrevivendo. Aqui vivemos uma vida normal e pacata, assim como a sua. E assim como você, já sobrevivemos ao dia da nossa morte várias vezes.\n')

    print('Como? Sim. Quantas vezes você já passou pelo dia da sua morte e conseguiu se salvar?\n')

    print('Nesse jogo você precisa passar com o seu personagem por 3 situações cotidianas. Passar pelo dia da sua morte e conseguir sobreviver a isso. Você consegue? Hoje você poderá tentar sobreviver na pele de três personagens:\n')
primeiroPasso()

# Algumas definições de funções usadas durante o jogo

def quebraLinha():
    print('-=' * 42)

def opcaoInvalida():
    print('Opção inválida. Escolha opção válida.')

def instrucoes():
    print('O jogo conta com três fases e nelas você precisa sobreviver a sua morte. O intuito do jogo é que você consiga lutar pela vida argumentando com a morte para que ela vá embora sem te levar. Escolha as respostas certas.\n')

def boaEscolha():
    print('Boa escolha. Você conseguiu sobreviver até aqui... Vamos ver até quando.\n')

def fimDoJogo():
    validaOpcao = False
    while validaOpcao == False:
        print('Não foi dessa vez que você consegiu escapar. Talvez se tivesse feito outra escolha...\n')
        jogarNovamente = int(input('Desja jogar novamente? Responda 1 para sim ou 2 para não: '))

        if jogarNovamente == 1:
            validaOpcao == True
            conhecaJogador()
            escolhaPersonagem()
        elif jogarNovamente == 2:
            validaOpcao == True
            print("Obrigada por jogar conosco.")
        else:
            validaOpcao == False
            opcaoInvalida

def finalFeliz():
    print('Você conseguiu. Chegou até aqui. Obrigada por jogar esse jogo. Espero que tenha aprendido algo. Até a próxima.')


# Criar variáves para cada jogar

jogador1='Tiago'
jogador2='Josy'
jogador3='Ariel'

# Escolher jogador

def conhecaJogador():
    print(f'{jogador1} viveu dentro de casa uma vida muito difícil na infância. Presenciou o que uma crianças não deveria presenciar. Por conta disso sempre teve pressa de viver a frente do seu tempo.')
    quebraLinha()
    print(f'A {jogador2} entendeu desde cedo o seu dever de mudar o destino da sua casa. Seus sonhos são todos relacionados a ter a dignidade que não pôde ter na infancia e combater o que viveu dentro de casa.')
    quebraLinha()
    print(f'{jogador3} cresceu com um enorme sonho e foi alimentado por ele por muito tempo. Ariel vive uma vida motivada pelo desejo de realiza-lo. ')
    quebraLinha()
    print('Agora que você já conhece os jogadores você pode escolher em que pele viverá.\n')
    quebraLinha()
conhecaJogador()

# função para escolha dos jogadores
def escolhaPersonagem():
    validaOpcao = False
    
    while validaOpcao == False:
        personagem = int(input('Digite o número correspondente ao personagem escolhido, sendo 1 para Tiago, 2 para Josy e 3 para Ariel: '))

        if personagem == 1:
            validaOpcao = True
            quebraLinha()
            print(str('Você escolheu fazer as escolhas por Tiago. Vamos começar...\n'))
            # Chamar as instruções do jogo
            instrucoes()
            exibaHistoriaTiagoCrianca()
            escolhasTiagoCrianca()
            exibaHistoriaTiagoAdulto()
            escolhasTiagoAdulto()
            exibaHistoriaTiagoIdoso()
            escolhasTiagoIdoso()

        elif personagem == 2:
            validaOpcao = True
            quebraLinha()
            print(str('Você escolheu fazer as escolhas por Josy. Vamos começar...\n'))
            # Chamar as instruções do jogo
            instrucoes()
            exibaHistoriaJosyCrianca()
            escolhasJosyCrianca()
            exibaHistoriaJosyAdulta()
            escolhasJosyAdulta()
            exibaHistoriaJosyoIdosa()
            escolhasJosyIdosa()
        elif personagem == 3:
            validaOpcao = True
            quebraLinha()
            print(str('Você escolheu fazer as escolhas por Ariel. Vamos começar...\n'))
            # Chamar as instruções do jogo
            instrucoes()
            exibaHistoriaArielCrianca()
            escolhasArielCrianca()
            exibaHistoriaArielAdulto()
            escolhasArielAdulto()
            exibaHistoriaArieloIdoso()
            escolhasArielIdoso()
        else:
            validaOpcao = False
            opcaoInvalida = print('Opção inválida. Digite 1, 2 ou 3')


# Fase 1 do Jogador Tiago
def exibaHistoriaTiagoCrianca():
    print('A infância de Tiago: Tiago vivia em um bairro bem violento da cidade. Frequentando a escola do bairro ouvia muitas histórias assustadoras e ao mesmo tempo cotidianas. Assaltos, sequestros, tentativas de roubo ao banco da pracinha. Conheceu fulano, que é primo de ciclano que é primo do traficante X. E ouvia muitos sons de arrepiar vindo da rua nas madrugadas, muitas vezes não conseguia dormir.\n')

    print (input('Complicado, né? \n'))

    print('Apesar do dia a dia complicado tudo até ia bem. Na verdade, parecia que Tiago era poupado de muita coisa pela mãe. \n')

    print('Falando nisso, sua família vinha passando por uma mudança de comportamento. Era notório que seus pais, que quase não tinham conflitos, começaram a brigar mais, se enfrentavam e muitas vezes ficavam um tempo sem se falar. Chegou a pegar sua mãe chorando uma vez. Tiago era filho único e não tinha muito com quem compartilhar, mas achava que era normal. Existem épocas em que todos estão mais estressados que o normal…\n')

    print('Até que um dia…\n')

    print('Numa tarde de feriado, sem aulas e com os pais em casa, Tiago viu uma oportunidade de estar mais com o seu pai que quase não via. Ele passava mais tempo fora de casa a trabalho que a mãe. Mas o pai não saía do quarto. A mãe pediu para que Tiago não o incomodasse. Mas ele queria estar com o pai.\n')

    print('Então Tiago resolve ver se o pai está bem. Vai até o quarto, abre a porta e vê algo estranho. Estranho? Não muito estranho. Tiago sabia exatamente o que o pai estava fazendo. Eu diria… inesperado. Tiago já havia conversado sobre isso com os amigos, já tinha visto isso na tv e até na rua já viu pessoas escondidas usando drogas. Mas o pai… foi a primeira vez. Que impacto. Ele saiu antes mesmo que alguém notasse. Para o pai e a mãe nada aconteceu. Para Tiago o mundo girou.\n')

    print(input('Você esperava por essa? \n'))

    quebraLinha()

    print('Tiago passou todos os dias seguidos buscando uma justificativa para o pai fazer isso. E na sua adolescência encontrou nas ruas uma resposta. Aprendeu que a droga é uma forma diferente de se divertir, que se divertir era uma forma diferente de se desestressar e que não era muito difícil conseguir o que queria.\n')

    print('E todo fim de semana, depois de dias estressantes de trabalho para ajudar em casa, saía com os amigos para se divertir.\n')

    print('Hoje é um desses dias. Viva como o Tiago.\n')


def escolhasTiagoCrianca():
    validaOpcao = False
    print('-Que semana cansativa! Hoje eu preciso zuar. Tô pique inimigo do fim, vou pro after do after. Vou fazer valer o documento de identidade falso.\n')
    primeiraEscolha = print('Você quer aproveitar ao máximo e antes de começar tem duas opções:\n1 - Beber do lado de fora da festa para salvar dinheiro, já que a bebida no local vai estar bem mais cara.\n2- Deixa para beber dentro da festa, não está ligando para economia de dinheiro hoje.\n')

    while validaOpcao == False:
        exibaPergunta01 = int(input('Qual a sua escolha? Responda 1 ou 2: '))
        if exibaPergunta01 == 1:
            validaOpcao = True
            print('-Só aqui já salvei um dinheiro.\n')
            print('Tiago conseguiu convencer todos os amigos que estavam com ele a já começar do lado de fora. O dinheiro é muito suado, vamos otimizar os gastos e assim conseguiu curtir mais lá dentro.\nJá na porta muita confusão. Boatos de que a minutos atrás algumas pessoas foram pisoteadas aos serem empurradas por quem estava atrás na fila pra conseguir pegar um bom lugar no show. Que loucura. Isso não te assusta?\n')
            exibaAssusta = (int(input('Isso não te assusta? Responda 1 para sim ou 2 para não: ')))
            if exibaAssusta == 1:
                validaOpcao = True
                print('\n-Pessoal, estou assustado. Acho que vou desistir.\n')
                boaEscolha()
                quebraLinha()
            elif exibaAssusta == 2:
                validaOpcao = True
                print('-Que loucura, pessoal. Mas só se vive uma vez, né?\n')
                print('O que eu não esperava era que o pior poderia acontecer comigo. Ao tentar acessar o local houve uma grande confusão novamente. E não tive muitas chances. Fui empurrado, não sabia como sair de onde eu estava. Esse foi o meu fim\n')
                quebraLinha()
                fimDoJogo()
            else:
                opcaoInvalida()
                validaOpcao = False
        elif exibaPergunta01 == 2:
            validaOpcao = True
            print('-Só se vive uma vez!\n')
            print('Tiago conseguiu convencer todos os amigos que estavam com ele a começar a consumir lá dentro. O dinheiro é muito suado, vamos fazer valer cada segundo do evento. Tiago quer pegar a grande, ficar bem pertinho do palco.\nJá na porta muita confusão. Não era só ele quem queria estar perto do palco. O público estava enfurecido e começou um empurra empurra quando os portões se abriram. Boatos de que algumas pessoas estão sendo pisoteadas por conta da confusão. Tiago tenta começar a ir contra a maré. Mas não tem jeito.\n')
            fimDoJogo()
        else:
            opcaoInvalida()
            validaOpcao = False

#Fase 2 jogador Tiago

def exibaHistoriaTiagoAdulto():
    print('Aquele show na adolescência de Tiago havia o marcado para sempre. Se não tivesse acontecido nada com certeza ele teria se arrependido de ir embora. Mas as notícias não mentem: aquele dia ele poderia ter feito a escolha errada. Um grande desastre aconteceu, ele poderia estar no meio. A escolha de ir para casa deu uma nova chance ao rapaz.\n')

    print('Depois daquele dia uma decisão foi tomada: É preciso mudar de vida. Tiago virou outra pessoa.\n')

    print('...Quer dizer, também não é assim. Ele não virou um herói. Mas também resolveu repensar a forma que vivia.\n')

    print('Uma coisa é certa, Tiago se tornou mais responsável. E essa responsabilidade levou ele a tomar muitas outras decisões corretas, como deixar de ingerir ilícitos. O impacto dos traumas da vida tinha sido interrompido ali. Ele permitiu que isso fosse interrompido.\n')

    print('Até que um dia…\n')

    quebraLinha()

    print('Tiago vinha passando por problemas financeiros. A vida vinha ficando cada vez mais difícil. Não só os 25 anos estavam batendo na porta, mas começava a pesar para ele o dinheiro que conseguia gerar. Não garantia a sua subexistência. \n')

    print(input('Complicado, né? \n'))

    print('Desabafando com um amigo conseguiu uma indicação. O amigo trabalhava em uma empresa de eletrônica, mexia com cabiamento de rua. Haviam duas vagas abertas: Uma para pessoas sem experiência, salário mínimo, não muito diferente do que ganhava no bico de garçon. Outra para pessoas com experiência, era tentador, salário maior e contratação imediata.\n')

    print('Segundo o amigo o trabalho era tranquilo: "nada que você não consiga aprender na internet". Tiago viu como uma oportunidade de ver o dinheiro que tanto precisava entrando no bolso mais rápido. Mnetiu no currículo e se candidatou a vaga com experiência.\n')

    print('Ele foi contratado e hoje é o seu primeiro dia. Viva como o Tiago.\n')


def escolhasTiagoAdulto():
    validaOpcao = False
    print('-Era a oportunidade que eu precisava. Me dediquei a semana toda buscando na internet as funções. Tirei dúvida com o meu amigo que me ajudou como pôde. Acho que entendi. \n')

    print('Ao conversar com o supervisor Tiago se esforçou para contar uma boa história. Inventou várias situações para encrementar a experiência profissional que não tinha. Perifeito, o supervisor confia nele. Lá vai o Tiago para a rua acompanhando um funcionário.\n')

    primeiraEscolha = print('Você quer aproveitar ao máximo aquela oportunidade de ver em ação o funcionário que está acompanhando. Sabe que na próxima vez irá sozinho resolver a demanda. Então começa a observar pacientemente os passos dele. Parece moleza, muito próximo ao que você pesquisou online. Mas a teoria parece fácil, nunca fiz isso sozinho. Eu tenho duas escolhas:\n1- Falar a verdade ao funcionário e ver a reação dele. Não somos amigos, não sei se ele me denunciaria ou tentaria me ajudar.\n2- Vou sozinho para o próximo desafio. Eu consigo, me pareceu fácil e confio em mim.\n')

    while validaOpcao == False:
        exibaPergunta02 = int(input('Qual a sua escolha? Responda 1 ou 2: '))
        if exibaPergunta02 == 1:
            validaOpcao = True
            print('-Eu nunca fiz isso antes. Vi o emprego como uma oportunidade de conseguir uma grana.\n')
            print('Tiago resolve falar a verdade. Pensou bem e escolheu não arriscar. Acreditou que o novo colega de trabalho o ajudaria.\n')
            print('A verdade também tem seu preço. Tiago foi denunciado pelo companeheiro de trabalho ao supervisor. O supervisor, por sua vez, confiou em sua honestidade e o rebaixou para o cargo sem experiência. Não era bem uma punição, ele merecia ser demitido. Foi uma oportunidade.')
            boaEscolha()
        elif exibaPergunta02 == 2:
            validaOpcao = True
            print('-Só se vive uma vez!\n')
            print('Tiago resolveu confiar em si. Ele sabia que podia fazer aquilo. Se dedicou a estudar tudo por uma semana, não é possível que daria errado. Ele estava confiante e isso bastava.\n')
            print('Tiago está sozinho. Precisa fazer o corte em um cabo mas não se lembra se é o amarelo ou o vermelho. Qualquer erro pode ser fatal. Não dá tempo de conferir, escolha com sabedoria:')
            exibaCorCabo = int(input('Qual a sua escolha? Responda 1 para vermelho ou 2 para amarelo: '))
            if exibaCorCabo == 1:
                validaOpcao = True
                print('\nNada acontece. Mas ainda assim não solucionou o problema. Isso foi muito arriscado\n')
                print('-Acho que vou encerrar por aqui e pedi ajuda a algum funcionário que esteja próximo para me socorrer.')
                boaEscolha()
                quebraLinha()
            elif exibaCorCabo == 2:
                validaOpcao = True
                print('Uma grande explosão acontece. A experiêcia fez falta. Esse foi seu fim.\n')
                quebraLinha()
                fimDoJogo()
            else:
                opcaoInvalida()
                validaOpcao = False
        else:
            opcaoInvalida()
            validaOpcao = False


# Fase 3 jogador Tiago

def exibaHistoriaTiagoIdoso():
    print('Nossa, você chegou até aqui! Que bom!\n')

    print('Tiago conseguiu se desenvolver na empresa e alcançar o inimaginável. Lá fez ótimas amizades e as levou para a vida. Com essas pessoas ele pôde compartilhar o quanto a vida pode nos ensinar. Que os nossos traumas de infância podem nos fazer crescer. Que a honestidade pode nos levar longe.\n')

    print('Mas o principal ensinamento que passou a frente foi que as nossas decisões nos fazem percorrer um longo caminho de vida ou encurta-lo. E como dizem "A única certeza é a morte" Tiago está pronto para viver a última fase da sua jornada. \n')

    print('De certo: Daqui ninguém passa. Mas existem escolhas que podem determinar nosso melhor fim. E aqui vai mais um jogo de escolhas.\n')


def escolhasTiagoIdoso():
    validaOpcao = False
    print('Quando somos idosos passamos muito tempo introspectivos. As lembranças são inevitáveis e os fantasmas nos revisitam. Com Tiago não seria diferente.\n')

    print('Fazendo um balanço da vida é impossível não pensar no que poderia ter sido diferente. Será que se o seu pai não fosse um usuário ele não teria dado a família condições de morar em um lugar melhor? Será que se Tiago não tivesse sido tão exposto ao caos a sua adolescência teria sido menos traumática? Será que se ele tivesse sido sempre honesto não teria conquistado mais coisas? Quantas oportunidades foram deixadas de lado a partir das suas escolhas?\n')

    print('-Não sei se devo guardar tanta mágoa da minha história.\n')

    print('Mas será que esses questionamentos não são razoáveis?\n')

    print('Faça sua última decisão por Tiago\n')

    primeiraEscolha = print('1- Nada mais justo do que vemos a nossa história com os olhos da realidade. Tiago não deve ser forçar a perdoar o seu passado, o seu pai, as suas escolhas... \n2- Tiago está idoso demais para ficar se preocupando com o que já passou. Mesmo que ninguém tenha o pedido desculpas, Tiago deve perdoar o seu passado')

    while validaOpcao == False:
        exibaPergunta03 = int(input('Qual a sua escolha? Responda 1 ou 2: '))
        if exibaPergunta03 == 1:
            validaOpcao = True
            print('Não existe resposta errada nessa questão. Mas existem consequências. De certa forma a mágoa aquece o coração, faz com que o que foi vivido faça sentido, não foi um sofrimento em vão. Mas a mágoa ainda assim é maléfica para o nosso corpo. Por suas escolhas Tiago descobriu e conviveu com um câncer que o levou rapidamente. Tiago sobreviveu até a sua velhice. Muitos ficaram para trás na corrida da vida. A pesar das suas escolhas é impossível chama-lo de perdedor. ')
            quebraLinha()
            finalFeliz()
        elif exibaPergunta03 == 2:
            validaOpcao = True
            print ('Não existe resposta errada nessa questão. Mas existem consequências. Tiago escolheu viver uma vida livre das opressões da sua mente. E viveu até os 100 anos. Existe algum lucro em viver tanto tempo? Eu não sei te responder. Tiago sobreviveu até a sua velhice. Muitos ficaram para trás na corrida da vida. A pesar das suas escolhas é impossível chama-lo de perdedor.\n')
            quebraLinha()
            finalFeliz()
        else:
            opcaoInvalida()
            validaOpcao = False



# Fase 1 do Jogador Josy
def exibaHistoriaJosyCrianca():
    print('A infância de Josy: Josy na sua infância passou por poucas e boas. Passou por uma das coisas que nenhuma criança deveria passar: a fome. Viu em casa seus pais lutando para que essa realidade mudasse. Mas aquela realidade tinha um misto de falta de amparo governamental junto ao pouco letramento daqueles responsáveis.\n')

    print (input('Complicado, né? \n'))

    print('Apesar do dia a dia complicado tudo até ia bem. Na verdade, parecia que Josy era poupada de muita coisa pela mãe. \n')

    print('Falando nisso, foi traumático perceber na adolescência que muitas vezes em que a sua mãe não parecia bem, parecia estar doente, na verdade ela estava convivendo com a fome para que Josy e seus irmãos não precisassem sofrer com ela.\n')

    quebraLinha()

    print('Josy passou todos os dias seguidos buscando uma solução para tirar a sua família daquela situação. E na sua adolescência encontrou sua primeira oportunidade digna de emprego.\n')

    print('Na escola conheceu a posição de jovem aprendiz. E após muita luta veio o resultado do processo seletivo: devido a sua força e garra Josy havia sido selecionada para a vaga. Que festa! Aquele pouco salário levaria mais esperança para dentro de casa.\n')

    print('Hoje é o dia de levar a documentação na empresa. Viva como a Josy.\n')


def escolhasJosyCrianca():
    validaOpcao = False
    print('Josy foi avisada que não poderia chegar atrasada sobe o risco de perder a vaga. Ela sabia que o tempo era curto e tinha montado uma estratégia para que conseguisse sair da escola a tempo de atravessar a cidade e chegar no horário. Mas pensou na possibilidade de conversar com a empresa para que conseguisse chegar mais tarde mas em segurança. Você já tinha impressionado eles, mas talvez a tentativa fosse colocar a oportunidade em risco.\n')
    primeiraEscolha = print('Você precisa decidir:\n1- Correr o máximo que pode para conseguir chegar a tempo todos os dias e não perder essa oportunidade.\n2- Tentar negociar um novo horário de trabalho, mesmo que isso signifique sair mais tarde do outro lado da cidade.\n')

    while validaOpcao == False:
        exibaPergunta01 = int(input('Qual a sua escolha? Responda 1 ou 2: '))
        if exibaPergunta01 == 1:
            validaOpcao = True
            print('-Não posso colocar essa oportunidade em risco.\n')
            print('Josy, uma menina tão fisicamente fragil mas tão decidida. Correu atrás de seus sonhos com sangue nos olhos, queria ver a realidade da sua família mudando. Queria ser o agente transformador daquela casa.\nAquela cidade é tão grande. Como pode isso não assusta-la? Josy está no meio da maior avenida da cidade, do outro lado da sua o metrô que precisa pegar, quase partindo. Josy deve arriscar atravessar para chegar no horário ou deve aguardar em segurança na faixa e explicar na empresa o seu atraso?')
            exibaAssusta = (int(input('Isso não te assusta? Responda 1 para arriscar ou 2 para aguardar na faixa: ')))
            if exibaAssusta == 1:
                validaOpcao = True
                print('\n-Ao forçar atravessar um grande acidente acontece. Josy estava tão decidida a pegar aquele trem que não percebeu quando o ônibus cortava a rua em sua direção. Aquele corpo magro pela fome, frágil pelos obstáculos que vive, foi engolido pelo ônibus. Esse foi o seu fim.\n')
                fimDoJogo()
                quebraLinha()
            elif exibaAssusta == 2:
                validaOpcao = True
                print('-Vou prezar pela minha segurança.\n')
                print('Josy chegou a conclusão de que conseguiria dialogar com a empresa. Já os impressionou durante todo o processo seletivo, ali não seria diferente. Estava disposta a sair de lá com um acordo que beneficiasse ambos os lados. Mas infelizmente o resultado não foi o esperado. Josy acabou perdendo a vaga.\n')
                quebraLinha()
            else:
                opcaoInvalida()
                validaOpcao = False
        elif exibaPergunta01 == 2:
            validaOpcao = True
            print('-Vou prezar pela minha segurança.\n')
            print('Josy chegou a conclusão de que conseguiria dialogar com a empresa. Já os impressionou durante todo o processo seletivo, ali não seria diferente. Estava disposta a sair de lá com um acordo que beneficiasse ambos os lados. E assim como o esperado, o seu senso de responsabilidade mais uma vez impressionou os gestores. Josy conseguiu negociar com a empresa e, mesmo saindo um pouco no prejuízo, não perdeu a oportunidade.\n')
            boaEscolha()
        else:
            opcaoInvalida()
            validaOpcao = False


#Fase 2 jogadora Josy

def exibaHistoriaJosyAdulta():
    print('Aquela experiência truxe dias complicados. Mas engrandecedores. Josy tirou grandes lições da sua infância e adolescência. No fim quanto mais a gente sofre mais a gente aprende, certo?\n')

    print('Me responda você, eu ainda estou pensando se todo sofrimento vale a pena.\n')

    print('...Quer dizer, também não é assim. Ela não virou um heroína. Mas também resolveu repensar a forma que viveria dali pra frente.\n')

    print('Uma coisa é certa, Josy se tornou mais responsável. E essa responsabilidade levou ele a tomar muitas outras decisões corretas, que as levaram vivenciar situações muito enriquecedoras e conhecer pessoas muito especiais.\n')

    print('Seria esse o respiro aliviado de quem venceu na vida?\n')

    quebraLinha()

    print('Josy conviveu e se envolveu com pessoas que marcaram a sua vida de forma expressiva. Mas ninguém como o Marcio. \n')

    print(input('Sente cheiro de romance, né? \n'))

    print('Pra ser honesto essa não é uma história de amor. O relacionamento com Marcio foi breve. Mas presentiou Josy com algo inesperadamente lindo: Ana, sua filha.\n')

    print('Josy estava acostumada a lutar. E mais uma vez escolheu viver essa grande surpresa da sua história.\n')

    print('Hoje é o dia do parto. Viva como a Josy.\n')


def escolhasJosyAdulta():
    validaOpcao = False
    print('Para muitas mulheres esse momento é muito sonhado e planejado. Não seia diferente para Josy. \n')

    print('Durante toda a sua gestção Josy se lembrou das histórias contadas pela mãe sobre sua gravidez e parto. Normal e sem anestesia, era como se nascia o povo pobre. Josy queria experenciar isso. Não por não ter outra opção, mas por entender que assim faria valer o legado da mãe e, de alguma forma, se conectaria com ela.\n')

    primeiraEscolha = print('Você quer aproveitar ao máximo aesse momento. Viver cada dor e choro que ele pode causar. Josy gosta de ser vista como guerreira e obstinada, foi chamada assim a vida inteira. De certa forma entendia que essa escolhia a faria honrar o esforço da mãe de educar uma mulher forte. A pesar disso tudo, o médico plantonista recomedou que fosse feita cesariana. Após algumas irregularidades na pressão e uns apontamentos estranhos em exames (que não daria tempo de serem investigados) a recomendação médica era que essa modalidade cirúrgica fosse feita. \n')

    while validaOpcao == False:
        exibaPergunta02 = int(input('Qual a sua escolha? Responda 1 para cesariana ou 2 para parto normal: '))
        if exibaPergunta02 == 1:
            validaOpcao = True
            print('-Vou negar minha intuição por acreditar que a orientação médica deveria falar mais alto nesse momento.\n')
            print('A verdade é que essa decisão já foi tomada com arrependimento De certa forma Josy sentia que não conseguiu honrar o compromisso que traçou com a mãe. Deu ouvidos a razão e deixou a intuição de lado. Bom, Ana nasceu bem.')
            boaEscolha()
        elif exibaPergunta02 == 2:
            validaOpcao = True
            print('-Só se vive uma vez!\n')
            print('Josy decide honrar o compromisso que traçou com a sua mãe, acreditava que a sua intuição não era apenas baseada no desejo do parto normal mas também uma mensagem do além vinda direta de sua mãe.\n')
            print('Após algumas horas em trabalho de parto o diagnóstico: Josy enfrentava um quadro de eclampisia. A decisão a ser tomada: Preservar a minha vida ou a do bebê?\n')
            exibaCorCabo = int(input('Qual a sua escolha? Responda 1 preservar Josy ou 2 para preservar Ana: '))
            if exibaCorCabo == 1:
                validaOpcao = True
                print('\nNão existe resposta correta aqui. Ainda que houvesse uma escolha existia o risco de ser perder as duas. Mas não foi o que aconteceu. Assim como a medicina age os milagres também. As duas conseguiram sobreviver ao parto.\n')
                boaEscolha()
                quebraLinha()
            elif exibaCorCabo == 2:
                validaOpcao = True
                print('\nNão existe resposta correta aqui. Ainda que houvesse uma escolha existia o risco de ser perder as duas. E foi isso o que aconteceu. Nenhuma das duas conseguiram sobreviver ao parto.\n')
                quebraLinha()
                fimDoJogo()
            else:
                opcaoInvalida()
                validaOpcao = False
        else:
            opcaoInvalida()
            validaOpcao = False


# Fase 3 jogadora Josy

def exibaHistoriaJosyoIdosa():
    print('Nossa, você chegou até aqui! Que bom!\n')

    print('Josy entendeu com a vida que com grandes poderes virão grandes responsabilidades. E que muitas vezes a intuição nos leva ao auge e a queda. Mas a Josy teve histórias pra contar. Viveu a vida com maestria. Entendeu o quanto a vida pode nos ensinar. Que os nossos traumas de infância podem nos fazer crescer. Como deve ser bom viver ao lado de uma pessoa tão sábia.\n')

    print('Será? Bom, Ana não vê dessa forma. Existem pessoas que nasceu para lutar. Josy lutou até o fim em respeito a família que teve. Mas não teve o mesmo em troca. A filha que gerou sonhando em se reconectar com a sua própria infância e reconstruiria essa história com muito mais conforto e aconchego não honrou os planos da mãe. \n')

    print('A Josy planejou todo o futuro com a filha. Mas não estava nos planos da Ana seguir o desejo da mãe. Muito pelo contrário, foi muito difícil para a Ana conviver com uma mãe cheia de planos e expectativas para a sua vida. O afastamento foi inevitável.')

    print('De certo: Daqui ninguém passa. Mas existem escolhas que podem determinar nosso melhor fim. E aqui vai mais um jogo de escolhas.\n')


def escolhasJosyIdosa():
    validaOpcao = False
    print('Quando somos idosos passamos muito tempo introspectivos. As lembranças são inevitáveis e os fantasmas nos revisitam. Com Josy não seria diferente.\n')

    print('Fazendo um balanço da vida é impossível não pensar no que poderia ter sido diferente. Qual seria o impacto na vida da Josy se ela tivesse crescido com mais oportunidades? Será que as decisões da adolescência reservaram para a Josy o melhor futuro? Quantas oportunidades foram deixadas de lado pelo excesso de planejamento? A Ana viveria melhor com o que Josy planejou para ela ou com o que construiu sozinha?\n')

    print('-Não sei se devo guardar tanta mágoa da minha história.\n')

    print('Mas será que esses questionamentos não são razoáveis?\n')

    print('Faça sua última decisão por Josy\n')

    primeiraEscolha = print('1- Nada mais justo do que vermos a nossa história com os olhos da realidade. Josy não deve ser forçar a perdoar o seu passado, a filha, as suas escolhas... \n2- Josy está idosa demais para ficar se preocupando com o que já passou. Mesmo que ninguém tenha a pedido desculpas, Josy deve perdoar o seu passado')

    while validaOpcao == False:
        exibaPergunta03 = int(input('Qual a sua escolha? Responda 1 ou 2: '))
        if exibaPergunta03 == 1:
            validaOpcao = True
            print('Não existe resposta errada nessa questão. Mas existem consequências. De certa forma a mágoa aquece o coração, faz com que o que foi vivido faça sentido, não foi um sofrimento em vão. Mas a mágoa ainda assim é maléfica para o nosso corpo. Por suas escolhas Josy descobriu e conviveu com um câncer que a levou rapidamente. Josy sobreviveu até a sua velhice. Muitos ficaram para trás na corrida da vida. A pesar das suas escolhas é impossível chama-la de perdedora. ')
            quebraLinha()
            finalFeliz()
        elif exibaPergunta03 == 2:
            validaOpcao = True
            print ('Não existe resposta errada nessa questão. Mas existem consequências. Josy escolheu viver uma vida livre das opressões da sua mente. E viveu até os 100 anos. Existe algum lucro em viver tanto tempo? Eu não sei te responder. Josy sobreviveu até a sua velhice. Muitos ficaram para trás na corrida da vida. A pesar das suas escolhas é impossível chama-la de perdedora.\n')
            quebraLinha()
            finalFeliz()
        else:
            opcaoInvalida()
            validaOpcao = False


# Fase 1 do Jogador Ariel
def exibaHistoriaArielCrianca():
    print('A infância de Ariel: Aos 8 anos Ariel foi apresentado ao piano na igreja. A sua curiosidade chamou atenção do músico do local. Ariel era apaixonado pela sonoridade e todos os dias que tinha culto estava presente, na primeira fila, sempre observando o músico.\n')

    print('Quando lhe foi oferecido a oportunidade de estudar música foi como um sonho realizado. Ele começou a se dedicar bastante a essa oportunidade. E era notória a sua evolução.\n')

    print('Até que...\n')

    print('Ariel queria estar, sempre que possível, na igreja para ter mais aulas, mas era uma criança. E dependia de seus pais para que pudesse atravessar a cidade para chegar até a igreja. E isso começou a incomodar a sua família. Eles diziam que não ficariam reféns desse gosto maluco do filho. E então o menino acabou desistindo...\n')

    print(input('Você já teve que desistir de algum sonho? \n'))

    quebraLinha()

    print('Ariel passou todos os dias seguidos buscando uma solução para essa situação. Ser impedido de praticar foi como uma facada no peito, como se tivesse perdido seu bem mais precioso. Com os anos pararam de frequentar a igreja, único local que conhecia onde poderia ouvir o instrumento. \n')

    print('Uma vez conversando na escola sobre sua frustração com uma colega ouviu falar de uma loja de instrumentos próximo a sua casa que tinha um piano elétrico. Era a oportunidade que tinha. Foi na loja, conheceu o dono mas ele não parecia uma pessoa muito legal. Não permitiu que o menino fosse lá. Na verdade ficou incomodado com a frequêcia que o menino ia a loja e não comprava nada.\n')

    print('Os amigos então sugeriram que fossem lá quando a loja estivesse fechada para tentarem entrar.\n')

    print('Hoje é o dia de tentar entrar na loja. Viva como Ariel.\n')


def escolhasArielCrianca():
    validaOpcao = False
    print('Ariel foi avisado de que a região tinha vigia noturno contratado. O pai de um colega era um dos vigias e sabia como era o dia a dia de plantão. Sabia que tinha um horário de troca de plantão onde o posto ficava sem vigilância por um tempo. E se levasse um fone conseguiria entrar tocar o instrumento elétrico sem que fizesse barulho. Observou que a loja não tinha nenhum outro tipo de mecanismo de segurança. Parece fácil mas também arriscado.\n')
    primeiraEscolha = print('Você precisa decidir:\n1- Correr o risco .\n2- Não arriscar.\n')

    while validaOpcao == False:
        exibaPergunta01 = int(input('Qual a sua escolha? Responda 1 ou 2: '))
        if exibaPergunta01 == 1:
            validaOpcao = True
            print('-Só se vive uma vez.\n')
            print('Ariel arrisca e vai com tudo. Tinha um plano todo esquematizado na sua cabeça e em um papel. Mas isso não queria dizer que daria certo, né? Quando chegou lá a situação era um pouco diferente do que o esperado. Mas percebeu que o vigia do local cuidava também de outra loja. Então pensa na possibilidade de esperar ele se afastar para tentar entrar na loja. Ele sabia como arrombar uma porta, aprendeu na internet e treinou em casa. Sabia que precisaria de segundos, seria rápido. Tudo e nome do sonho.')
            exibaAssusta = (int(input('Isso não te assusta? Responda 1 para arriscar ou 2 para desistir do plano: ')))
            if exibaAssusta == 1:
                validaOpcao = True
                print('\n-Ariel avança no plano. Só não contava que na verdade o plantonista da vez estava atrasado, enquanto o plantonista que sairia estava longe o novo chegou e viu alguém tentando entrar na loja. Ariel foi golpeado na cabeça. Um golpe que não interferiria na vida de um homem adulto, mas muito forte para um adolescente (mesmo com porte físico de adulto) Ariel foi encaminhado para o hospital mas teve complicações. Esse foi o seu fim.\n')
                fimDoJogo()
                quebraLinha()
            elif exibaAssusta == 2:
                validaOpcao = True
                print('-Vou prezar pela minha segurança.\n')
                print('Ariel chegou a conclusão de que era muito difícil completar a missão seguir o plano. Que como alí não era a situação ideal o melhor a fazer era tentar outro dia. Ele não tinha certeza do que estava acontecendo. Foi pra casa e com a cabeça fria optou por tentar outra coisa.\n')
                boaEscolha()
                quebraLinha()
            else:
                opcaoInvalida()
                validaOpcao = False
        elif exibaPergunta01 == 2:
            validaOpcao = True
            print('-Vou prezar pela minha segurança.\n')
            print('Na hora h deu medo. Ariel chegou a conclusão de que dali um tempo poderia arrumar um emprego e comprar o próprio instrumento. Demoraria muito mas era a escolha mais segura.\n')
            boaEscolha()
        else:
            opcaoInvalida()
            validaOpcao = False


#Fase 2 jogador Ariel

def exibaHistoriaArielAdulto():
    print('Aquela experiência truxe dias complicados. Mas engrandecedores. Ariel tirou grandes lições da sua infância e adolescência. No fim quanto mais a gente sofre mais a gente aprende, certo?\n')

    print('Me responda você, eu ainda estou pensando se todo sofrimento vale a pena.\n')

    print('...Quer dizer, também não é assim. Ele não virou um herói. Mas também resolveu repensar a forma que viveria dali pra frente.\n')

    print('Uma coisa é certa, Ariel se tornou mais solitário. Não ter o apoio da família o marcou, não tinha como. Ter que adiar um sonho que era quase intrínseco à ele foi difícil. Ele se tornou introspectivo e batalhador. Instrospectivo pois não podia compartilhar com ninguém suas pequenas vitórias para alcançar o objetivo da compra do instrumento. Batalhador pois lutou sozinho pelo seu objetivo .\n')

    print(input('Lutar sozinho é ruim, né? \n'))

    quebraLinha()

    print('O tempo passou e Ariel comprou o seu primeiro piano. \n')

    print('Não tinha pra onde correr, o cara nascue pra isso. Com a retomada dos estudos Ariel se destacou rapidamente. Paixão incrementa no talento, né? E assim foi, conciliou dois empregos até ter a sua primeira oportunidade como musico. \n')

    print(input('Sentindo orgulho do Ariel? \n'))

    print('Pra ser honesto essa não é uma história tão feliz assim. O impacto de uma vida solitária até ali foi grave e ireversível. Ariel não sabia mais viver de outro jeito.\n')

def escolhasArielAdulto():
    validaOpcao = False
    print('A solidão não incomodava a ele mais. Ele aprendeu a viver com a própria companhia. As pessoas o achava estranho, volta e meia alguém o dizia que algo estava errado. Talvez todo músico erudito seja assim. \n')

    primeiraEscolha = print('O que você me diz? Ariel deve escolher viver uma vida mais solitária ou deve se forçar a recuperar o convívio com os outros?\n')

    while validaOpcao == False:
        exibaPergunta02 = int(input('Qual a sua escolha? Responda 1 para recuperar convívio ou 2 para ter uma vida solitária: '))
        if exibaPergunta02 == 1:
            validaOpcao = True
            print('-Vou negar minha intuição, dar ouvido às pessoas e tentar socializar.\n')
            print('Talvez isso faça bem, né? Ouvimos tanto sobre as doenças da alma que crescem em pessoas solitárias. Acredito que Ariel não vai se arrepender de tentar.')
            boaEscolha()
        elif exibaPergunta02 == 2:
            validaOpcao = True
            print('-Soltude e solidão.\n')
            print('Ariel escolhe não ceder à pressão dos outros. Viver sozinho é bom. Mas até quando?\n')
            print('Ariel começou a perceber que não comemorava aniversário, dia dos pais, natal, ano novo. Sua casa era silenciosa, o timbre do seu piano completava o espaço que faltava nessa casa. Mas o tempo faz aparecer o mais obscuro e escondido dos nossos medos. Era inevitável o adoecimento da alma. E assim aconteceu. Ariel se foi realizado, solitário e feliz. Isso é um gem over?\n')
            fimDoJogo()
        else:
            opcaoInvalida()
            validaOpcao = False


# Fase 3 jogador Ariel

def exibaHistoriaArieloIdoso():
    print('Nossa, você chegou até aqui! Que bom!\n')

    print('Ariel entendeu com a vida que escolhas devem ser tomadas com sabedoria. Viveu solitário até quando pôde e foi bom até. Depois soube pedir ajuda e retomar convívio social. Ariel teve histórias pra contar. Histórias que guardou pra si por muito tempo. Viveu bem a vida. Entendeu o quanto a vida pode nos ensinar. Que os nossos traumas de infância podem nos fazer crescer e amadurecer.\n')

    print('Ariel não se tornou um música mundialmente reconhecido. Mas a sua história foi ouvida, seu talento foi explorado e conseguiu viver a vida da forma que queria.\n')

    print('De certo: Daqui ninguém passa. Mas existem escolhas que podem determinar nosso melhor fim. E aqui vai mais um jogo de escolhas.\n')


def escolhasArielIdoso():
    validaOpcao = False
    print('Quando somos idosos passamos muito tempo introspectivos. As lembranças são inevitáveis e os fantasmas nos revisitam. Com Ariel não seria diferente.\n')

    print('Fazendo um balanço da vida é impossível não pensar no que poderia ter sido diferente. Qual seria o impacto na vida de Ariel se ele tivesse crescido com mais oportunidades? Será que as decisões dos seus pais reservaram para a Ariel o melhor futuro? Quantas oportunidades foram deixadas de lado na vida? O que teria acontecido se Ariel tivesse conseguido continuar seus treinos na adolescência?\n')

    print('-Não sei se devo guardar tanta mágoa da minha história.\n')

    print('Mas será que esses questionamentos não são razoáveis?\n')

    print('Faça sua última decisão por Ariel\n')

    primeiraEscolha = print('1- Nada mais justo do que vermos a nossa história com os olhos da realidade. Ariel não deve ser forçar a perdoar o seu passado, sua famíalia, as suas escolhas... \n2- Ariel está idoso demais para ficar se preocupando com o que já passou. Mesmo que ninguém tenha a pedido desculpas, Ariel deve perdoar o seu passado')

    while validaOpcao == False:
        exibaPergunta03 = int(input('Qual a sua escolha? Responda 1 ou 2: '))
        if exibaPergunta03 == 1:
            validaOpcao = True
            print('Não existe resposta errada nessa questão. Mas existem consequências. De certa forma a mágoa aquece o coração, faz com que o que foi vivido faça sentido, não foi um sofrimento em vão. Mas a mágoa ainda assim é maléfica para o nosso corpo. Por suas escolhas Ariel descobriu e conviveu com um câncer que o levou rapidamente. Ariel sobreviveu até a sua velhice. Muitos ficaram para trás na corrida da vida. A pesar das suas escolhas é impossível chama-lo de perdedor. ')
            quebraLinha()
            finalFeliz()
        elif exibaPergunta03 == 2:
            validaOpcao = True
            print ('Não existe resposta errada nessa questão. Mas existem consequências. Ariel escolheu viver uma vida livre das opressões da sua mente. E viveu até os 100 anos. Existe algum lucro em viver tanto tempo? Eu não sei te responder. Ariel sobreviveu até a sua velhice. Muitos ficaram para trás na corrida da vida. A pesar das suas escolhas é impossível chama-lo de perdedor.\n')
            quebraLinha()
            finalFeliz()
        else:
            opcaoInvalida()
            validaOpcao = False

escolhaPersonagem()