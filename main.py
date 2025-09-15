conversation = {                # conversation data dictionary
    'user': '',                 # section user
    'topic': None,              # section topic     - initially whithout subject
    'personality': 'formal'     # personality section
}

personalities = {               # personality dictionary (personality: common texts + theme texts)
    
    # 'personality':
    #   'greeting': 'text'      - saudation
    #   'welcome': 'text'       - welcome user (necessarily a key -> '{}')
    #   'farewell': 'text'      - goodbye user
    #   'default': 'text'       - stardant mensage
    #
    # # subject text
    # 'subjects': 'written about the subjects'
    # (...)
    
    'formal': {                 # formal personality 
        'greeting': "Olá",
        'welcome': "{} é um prazer te conhecer. Em que posso te ajudar?",
        'farewell': "{} foi um prazer te ajudar. Tenha um ótimo dia.",
        'default': "Não compreendi sua solicitação.",

        # subject text
        'subject 1': "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus tincidunt tincidunt est, sit amet luctus ex mattis eget. Donec nunc velit, ullamcorper eget consectetur sed, ornare eget arcu. Curabitur posuere eros et odio interdum ultrices. Aenean egestas pharetra neque, sit amet venenatis magna eleifend vel. Mauris convallis hendrerit diam, in placerat dolor imperdiet at. In vel massa ex. Fusce sit amet metus suscipit, rutrum enim nec, ullamcorper augue. Morbi et leo non lorem molestie lobortis. Phasellus dapibus dui ac facilisis vestibulum. Nullam diam dui, pretium vel rhoncus in, egestas eget sem. Nulla condimentum volutpat arcu ut pharetra. Maecenas cursus tristique faucibus. ",
        'subject 2': "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus tincidunt tincidunt est, sit amet luctus ex mattis eget. Donec nunc velit, ullamcorper eget consectetur sed, ornare eget arcu. Curabitur posuere eros et odio interdum ultrices. Aenean egestas pharetra neque, sit amet venenatis magna eleifend vel. Mauris convallis hendrerit diam, in placerat dolor imperdiet at. In vel massa ex. Fusce sit amet metus suscipit, rutrum enim nec, ullamcorper augue. Morbi et leo non lorem molestie lobortis. Phasellus dapibus dui ac facilisis vestibulum. Nullam diam dui, pretium vel rhoncus in, egestas eget sem. Nulla condimentum volutpat arcu ut pharetra. Maecenas cursus tristique faucibus. ",
        'subject 3': "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus tincidunt tincidunt est, sit amet luctus ex mattis eget. Donec nunc velit, ullamcorper eget consectetur sed, ornare eget arcu. Curabitur posuere eros et odio interdum ultrices. Aenean egestas pharetra neque, sit amet venenatis magna eleifend vel. Mauris convallis hendrerit diam, in placerat dolor imperdiet at. In vel massa ex. Fusce sit amet metus suscipit, rutrum enim nec, ullamcorper augue. Morbi et leo non lorem molestie lobortis. Phasellus dapibus dui ac facilisis vestibulum. Nullam diam dui, pretium vel rhoncus in, egestas eget sem. Nulla condimentum volutpat arcu ut pharetra. Maecenas cursus tristique faucibus. "
    },
    
    'pushy': {                  # pushy personality
        'greeting': "E aí o'que você quer?",
        'welcome': "Olha {}, por que você está me encomodando?",
        'farewell': "Vaza daqui. Esquece que eu existo.",
        'default': "Escreve direito, analfabeto.",

        # subject text
        'subject 1': "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus tincidunt tincidunt est, sit amet luctus ex mattis eget. Donec nunc velit, ullamcorper eget consectetur sed, ornare eget arcu. Curabitur posuere eros et odio interdum ultrices. Aenean egestas pharetra neque, sit amet venenatis magna eleifend vel. Mauris convallis hendrerit diam, in placerat dolor imperdiet at. In vel massa ex. Fusce sit amet metus suscipit, rutrum enim nec, ullamcorper augue. Morbi et leo non lorem molestie lobortis. Phasellus dapibus dui ac facilisis vestibulum. Nullam diam dui, pretium vel rhoncus in, egestas eget sem. Nulla condimentum volutpat arcu ut pharetra. Maecenas cursus tristique faucibus. ",
        'subject 2': "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus tincidunt tincidunt est, sit amet luctus ex mattis eget. Donec nunc velit, ullamcorper eget consectetur sed, ornare eget arcu. Curabitur posuere eros et odio interdum ultrices. Aenean egestas pharetra neque, sit amet venenatis magna eleifend vel. Mauris convallis hendrerit diam, in placerat dolor imperdiet at. In vel massa ex. Fusce sit amet metus suscipit, rutrum enim nec, ullamcorper augue. Morbi et leo non lorem molestie lobortis. Phasellus dapibus dui ac facilisis vestibulum. Nullam diam dui, pretium vel rhoncus in, egestas eget sem. Nulla condimentum volutpat arcu ut pharetra. Maecenas cursus tristique faucibus. ",
        'subject 3': "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus tincidunt tincidunt est, sit amet luctus ex mattis eget. Donec nunc velit, ullamcorper eget consectetur sed, ornare eget arcu. Curabitur posuere eros et odio interdum ultrices. Aenean egestas pharetra neque, sit amet venenatis magna eleifend vel. Mauris convallis hendrerit diam, in placerat dolor imperdiet at. In vel massa ex. Fusce sit amet metus suscipit, rutrum enim nec, ullamcorper augue. Morbi et leo non lorem molestie lobortis. Phasellus dapibus dui ac facilisis vestibulum. Nullam diam dui, pretium vel rhoncus in, egestas eget sem. Nulla condimentum volutpat arcu ut pharetra. Maecenas cursus tristique faucibus. "
    },
    
    'carioca': {                # carioca personality
        'greeting': "Coé, meu mano? Tranquilo?",
        'welcome': "Pega a visão, {}. Qual a boa?",
        'farewell': "É nós, fica com deus, falou.",
        'default': "Papo reto, não entendi nada. Desenrola.",

        # subject text
        'subject 1': "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus tincidunt tincidunt est, sit amet luctus ex mattis eget. Donec nunc velit, ullamcorper eget consectetur sed, ornare eget arcu. Curabitur posuere eros et odio interdum ultrices. Aenean egestas pharetra neque, sit amet venenatis magna eleifend vel. Mauris convallis hendrerit diam, in placerat dolor imperdiet at. In vel massa ex. Fusce sit amet metus suscipit, rutrum enim nec, ullamcorper augue. Morbi et leo non lorem molestie lobortis. Phasellus dapibus dui ac facilisis vestibulum. Nullam diam dui, pretium vel rhoncus in, egestas eget sem. Nulla condimentum volutpat arcu ut pharetra. Maecenas cursus tristique faucibus. ",
        'subject 2': "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus tincidunt tincidunt est, sit amet luctus ex mattis eget. Donec nunc velit, ullamcorper eget consectetur sed, ornare eget arcu. Curabitur posuere eros et odio interdum ultrices. Aenean egestas pharetra neque, sit amet venenatis magna eleifend vel. Mauris convallis hendrerit diam, in placerat dolor imperdiet at. In vel massa ex. Fusce sit amet metus suscipit, rutrum enim nec, ullamcorper augue. Morbi et leo non lorem molestie lobortis. Phasellus dapibus dui ac facilisis vestibulum. Nullam diam dui, pretium vel rhoncus in, egestas eget sem. Nulla condimentum volutpat arcu ut pharetra. Maecenas cursus tristique faucibus. ",
        'subject 3': "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus tincidunt tincidunt est, sit amet luctus ex mattis eget. Donec nunc velit, ullamcorper eget consectetur sed, ornare eget arcu. Curabitur posuere eros et odio interdum ultrices. Aenean egestas pharetra neque, sit amet venenatis magna eleifend vel. Mauris convallis hendrerit diam, in placerat dolor imperdiet at. In vel massa ex. Fusce sit amet metus suscipit, rutrum enim nec, ullamcorper augue. Morbi et leo non lorem molestie lobortis. Phasellus dapibus dui ac facilisis vestibulum. Nullam diam dui, pretium vel rhoncus in, egestas eget sem. Nulla condimentum volutpat arcu ut pharetra. Maecenas cursus tristique faucibus. "
    },
    
    'bahiano': {                # baiano personality
        'greeting': "E aí, meu rei? Tudo na paz?",
        'welcome': "Bicho, que bom te ver.",
        'farewell': "Se pique meu nego.",
        'default': "Situação barril meu nego. Mas vem cá, largue o doce.",

        # subject text
        'subject 1': "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus tincidunt tincidunt est, sit amet luctus ex mattis eget. Donec nunc velit, ullamcorper eget consectetur sed, ornare eget arcu. Curabitur posuere eros et odio interdum ultrices. Aenean egestas pharetra neque, sit amet venenatis magna eleifend vel. Mauris convallis hendrerit diam, in placerat dolor imperdiet at. In vel massa ex. Fusce sit amet metus suscipit, rutrum enim nec, ullamcorper augue. Morbi et leo non lorem molestie lobortis. Phasellus dapibus dui ac facilisis vestibulum. Nullam diam dui, pretium vel rhoncus in, egestas eget sem. Nulla condimentum volutpat arcu ut pharetra. Maecenas cursus tristique faucibus. ",
        'subject 2': "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus tincidunt tincidunt est, sit amet luctus ex mattis eget. Donec nunc velit, ullamcorper eget consectetur sed, ornare eget arcu. Curabitur posuere eros et odio interdum ultrices. Aenean egestas pharetra neque, sit amet venenatis magna eleifend vel. Mauris convallis hendrerit diam, in placerat dolor imperdiet at. In vel massa ex. Fusce sit amet metus suscipit, rutrum enim nec, ullamcorper augue. Morbi et leo non lorem molestie lobortis. Phasellus dapibus dui ac facilisis vestibulum. Nullam diam dui, pretium vel rhoncus in, egestas eget sem. Nulla condimentum volutpat arcu ut pharetra. Maecenas cursus tristique faucibus. ",
        'subject 3': "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus tincidunt tincidunt est, sit amet luctus ex mattis eget. Donec nunc velit, ullamcorper eget consectetur sed, ornare eget arcu. Curabitur posuere eros et odio interdum ultrices. Aenean egestas pharetra neque, sit amet venenatis magna eleifend vel. Mauris convallis hendrerit diam, in placerat dolor imperdiet at. In vel massa ex. Fusce sit amet metus suscipit, rutrum enim nec, ullamcorper augue. Morbi et leo non lorem molestie lobortis. Phasellus dapibus dui ac facilisis vestibulum. Nullam diam dui, pretium vel rhoncus in, egestas eget sem. Nulla condimentum volutpat arcu ut pharetra. Maecenas cursus tristique faucibus. "
    },
    
    'cearense': {               # cearense personality
        'greeting': "Cuida pai, tudo bem hoje?",
        'welcome': "Bem-vindo {} a baixa da égua. Em que posso te ajudar?",
        'farewell': "",
        'default': "",

        # subject text
        'subject 1': "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus tincidunt tincidunt est, sit amet luctus ex mattis eget. Donec nunc velit, ullamcorper eget consectetur sed, ornare eget arcu. Curabitur posuere eros et odio interdum ultrices. Aenean egestas pharetra neque, sit amet venenatis magna eleifend vel. Mauris convallis hendrerit diam, in placerat dolor imperdiet at. In vel massa ex. Fusce sit amet metus suscipit, rutrum enim nec, ullamcorper augue. Morbi et leo non lorem molestie lobortis. Phasellus dapibus dui ac facilisis vestibulum. Nullam diam dui, pretium vel rhoncus in, egestas eget sem. Nulla condimentum volutpat arcu ut pharetra. Maecenas cursus tristique faucibus. ",
        'subject 2': "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus tincidunt tincidunt est, sit amet luctus ex mattis eget. Donec nunc velit, ullamcorper eget consectetur sed, ornare eget arcu. Curabitur posuere eros et odio interdum ultrices. Aenean egestas pharetra neque, sit amet venenatis magna eleifend vel. Mauris convallis hendrerit diam, in placerat dolor imperdiet at. In vel massa ex. Fusce sit amet metus suscipit, rutrum enim nec, ullamcorper augue. Morbi et leo non lorem molestie lobortis. Phasellus dapibus dui ac facilisis vestibulum. Nullam diam dui, pretium vel rhoncus in, egestas eget sem. Nulla condimentum volutpat arcu ut pharetra. Maecenas cursus tristique faucibus. ",
        'subject 3': "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus tincidunt tincidunt est, sit amet luctus ex mattis eget. Donec nunc velit, ullamcorper eget consectetur sed, ornare eget arcu. Curabitur posuere eros et odio interdum ultrices. Aenean egestas pharetra neque, sit amet venenatis magna eleifend vel. Mauris convallis hendrerit diam, in placerat dolor imperdiet at. In vel massa ex. Fusce sit amet metus suscipit, rutrum enim nec, ullamcorper augue. Morbi et leo non lorem molestie lobortis. Phasellus dapibus dui ac facilisis vestibulum. Nullam diam dui, pretium vel rhoncus in, egestas eget sem. Nulla condimentum volutpat arcu ut pharetra. Maecenas cursus tristique faucibus. "
    }
}


# list of keywords
formal_keyword = ['']       # formal keywords
pushy_keyword = ['']        # pushy keywords
carioca_keyword = ['']      # carioca keywords
baiano_keyword = ['']       # baiano keywords
cearense_keyword = ['']     # cearense keywords

# chat knowledge base
know = {
    'qual seu nome': 'Me chamo de',

    # knowledge of subjects
    # 'subject': 'text'
    #   'subject branch': 'text'

    'assunto 1': 'assunto',
        'assunto 1 branch': '',

    'assunto 2': 'assunto',
        'assunto 2 branch': '',

    'assunto 3': 'assunto',
        'assunto 3 branch': ''
}


# history of demonstrations
stats = {
    # data 1: x,
    # data 2: x

    # default messages data
    'send': 0,
    'qual o seu nome': 0,

    # subjects data
    'assunto 1': 0,
    'assunto 2': 0,
    'assunto 3': 0,

    # keywords data
    'formal_keyword': 0,
    'pushy_keyword': 0,
    'carioca_keyword': 0,
    'baiano_keyword': 0,
    'cearense_keyword': 0
}
interaction_count = 0               # chat interaction count


# chat inicialization
print(personalities[conversation['personality']]['greeting'])   # salute    - remove the salute from the active personality

name = str(input('Name: '))                # name request
conversation['user'] = name
print(personalities[conversation['personality']]['welcome'].format(conversation['user']))   # welcome   - welcome to the user


while True:
    # send message
    send = str(input('Mensagem: '))
    interaction_count += 1              # note the number of interactios during the chat
    
    # personality detection
    personality_chagend = False
    # se any word sent belongs to one of the keys mentioned, do:
    # pt-br: se em qualquer palavra enviada, pertencer a uma das chaves dita, faça:
    if any(word in send for word in formal_keyword):        # personality formal
        conversation['personality'] = 'formal'
        stats['formal_keyword'] += 1
        personality_chagend = True

    elif any(word in send for word in pushy_keyword):       # personality pushy
        conversation['personality'] = 'pushy'
        stats['pushy_keyword'] += 1
        personality_chagend = True

    elif any(word in send for word in carioca_keyword):     # personality carioca
        conversation['personality'] = 'carioca'
        stats['carioca_keyword'] += 1
        personality_chagend = True

    elif any(word in send for word in baiano_keyword):      # personality baiano
        conversation['personality'] = 'baiano'
        stats['baiano_keyword'] += 1
        personality_chagend = True

    elif any(word in send for word in cearense_keyword):    # personality cearense
        conversation['personality'] = 'cearense'
        stats['cearense_keyword'] += 1
        personality_chagend = True

    # close the chat
    if ('exit' or 'to go out' or 'get out') in send.lower():
        print(personalities[conversation['personality']]['farewell'].format(conversation['user']))
        # here structure to pull data
        break

    # continuation of the conversation
    elif 'mais' in send.lower() and conversation['topic']:
        if conversation['topic'] == 'assunto 1':
            print(personalities[conversation['personality']]['default'].replace('', 'Sobre assunto 1, o que mais você quer saber?'))
            if 'assunt 1 branch' in send.lower():
                print('')

        elif conversation['topic'] == 'assunto 2':
            print(personalities[conversation['personality']]['default'].replace('', 'Sobre assunto 2,  o que mais você quer saber?'))
            if 'assunt 1 branch' in send.lower():
                print('')

        elif conversation['topic'] == 'assunto 3':
            print(personalities[conversation['personality']]['default'].replace('', 'Sobre assunto 3,  o que mais você quer saber?'))
            if 'assunt 1 branch' in send.lower():
                print('')

        else:
            print('Não entendi sobre o que você quer saber mais.')
    
    # machine learning
    elif send in know:
        print('')
        if send in stats:
            stats[send] += 1                    # note the number of submissions
        conversation['topic'] = send.lower()    # update the topic according to the user
    
    else:
        print(personalities[conversation['personality']]['default'])                # receives theme from user
        learn_question = input('Me diga a resposta (ou "não" para pular): ')        # receives response from the user

        # if the user don't want to
        if learn_question.lower() != 'não':
            know[send.lower()] = learn_question
            print('Entendido')

            # add the statistics
            stats[send.lower()] = 1
            conversation['topic'] = send.lower()
