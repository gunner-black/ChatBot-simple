# files
know_files = 'know.txt'
stats_file = 'stats.txt'
report_file = 'report.txt'

know = {
    'ola': 'Olá! Em que posso ajudar?',
    'qual o seu nome': 'Meu nome é ChatBot',
    'quem ganhou a ultima copa': 'A última copa do mundo da FIFA, foi vencida pela Argentina.',
    'o que é var': 'var é uma tecnologia que permmite os árbitros de campo revisarem lances.',
    'quem é o melhor artilheiro da historia': 'O jogador com mais gols reconhecidos em partidas oficias é Cristiano Ronaldo, com mais de 800 gols na carreira.',
    'qual o melhor time': 'O vasco é o melhor time.',
    'qual o jogo mais emocionante': 'Concerteza a final de 2022, entre Argentina e França.',
    'tema': 'Futebol'
}
stats = {
    'interaction_total': 0,
    'learn': 0,
    'formal_keyword': 0,
    'pushy_keyword': 0,
    'cearense_keyword': 0
}
personalities = {
    'formal': {
        'greeting': "Olá",
        'welcome': "É um prazer te conhecer. Em que posso te ajudar?",
        'farewell': "{} foi um prazer te ajudar. Tenha um ótimo dia.",
        'default': "Não compreendi sua solicitação.",
        'prefix': "Em relação ao seu pedido, temos que: ",
        'suffix': "Espero que essa explicação tenha sido útil."
    },
    'pushy': {
        'greeting': "E aí o'que você quer?",
        'welcome': "Olha {}, por que você está me encomodando?",
        'farewell': "Vaza daqui. Esquece que eu existo.",
        'default': "Escreve direito, analfabeto.",
        'prefix': "Escuta aqui, a reposta é essa, não tem segredo: ",
        'suffix': "Agora que já sabe, pode me deixar em paz?"
    },
    'cearense': {
        'greeting': "Cuida pai, tudo bem hoje?",
        'welcome': "Bem-vindo {} a baixa da égua. Em que posso te ajudar?",
        'farewell': "{} vá pela sombra.",
        'default': "Eita, o que é isso, fi? Não entendi.",

        # subject text
        'prefix': "Vixe, pois tome aqui meu fi: ",
        'suffix': "Pronto, tá aí cumpadi."
    }
}

exit_keyword = ['sair', 'fechar', 'adeus', 'tchau']
continuation_keyword = ['mais', 'continue', 'detalhes']
formal_keyword = ['formal']
pushy_keyword = ['idiota', 'agressivo', 'animal']
cearense_keyword = ['oxe', 'cuida']

def load(file_path, default_data):
    data = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                clean = line.strip()
                if clean:
                    parts = clean.split('|', 1)
                    if len(parts) == 2:
                        key = parts[0].strip()
                        value_str = parts[1].strip()
                        if file_path == stats_file:
                            try:
                                data[key] = int(value_str)
                            except ValueError:
                                data[key] = value_str
                        else:
                            data[key] = value_str
            if not data:
                return default_data
            return data
    except FileNotFoundError:
        return default_data
    except Exception as e:
        print(f'Falha inesperada ao carregar {file_path}')
        return default_data

def save(data, file_path):
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            for key, value in data.items():
                f.write(f'{key}|{value}\n')
    except Exception as e:
        print(f'Falha ao salvar o arquivo {file_path}: {e}')

def report(stats, user, interaction_count):
    content = f"-- Relátorio --\n"
    content += f"Usuário: {user}\n"
    content += f"Interações nessa seção: {interaction_count}\n"
    content += f"Interações totais: {stats.get('interaction_total')}\n"

    for key, value in stats.items():
        if key not in ['interaction_total', 'learn', 'formal_keyword', 'pushy_keyword', 'cearense_keyword']:
            content += f'Uso de [{key}]: {value} \n'

    content += f"Forma ativado: {stats.get('formal_keyword', 0)}\n"
    content += f"Agressivo ativado: {stats.get('pushy_keyword', 0)}\n"
    content += f"Cearense ativado: {stats.get('cearense_keyword', 0)}\n"
    content += f"Respostas aprendidas: {stats.get('learn', 0)}\n"

    try:
        with open(report_file, 'w', encoding='utf-8') as file:
            file.write(content)
        print('Relatório salvo com sucesso')
    except Exception as e:
        print('Falha ao salvar relatório')
    print(content)

def run():
    global insight, stay
    insight = load(know_files, know)
    stay = load(stats_file, stats)

    conversation = {'user': '', 'topic': None, 'personality': 'formal'}
    session_interactions = 0
    personality = conversation['personality']
    print(personalities[personality]['welcome'].format(conversation['user']))
    name = str(input('Nome: '))
    conversation['user'] = name
    print(personalities[personality]['welcome'].format(conversation['user']))

    while True:
        send = str(input("Mensagem: ")).strip().lower()
        session_interactions += 1
        stats['interaction_total'] += 1
        handled = False

        # end the chat
        if any(word in send for word in exit_keyword):
            print(personalities[conversation['personality']]['farewell'].format(conversation['user']))
            save(know, know_files)
            save(stats, stats_file)
            report(stats, conversation['user'], session_interactions)
            break

        # personalities
        if any(word in send for word in formal_keyword) and conversation['personality'] != 'formal':
            conversation['personality'] = 'formal'
            stay['formal_keyword'] += 1
            handled = True
        elif any(word in send for word in pushy_keyword) and conversation['personality'] != 'pushy':
            conversation['personality'] = 'pushy'
            stay['pushy_keyword'] += 1
            handled = True
        elif any(word in send for word in cearense_keyword) and conversation['personality'] != 'cearense':
            conversation['personality'] = 'cearense'
            stay['cearense_keyword'] += 1
            handled = True

        personality = conversation['personality']
        if any(word in send for word in continuation_keyword) and not handled:
            topic = conversation['topic']
            neutral = know.get(topic, None)
            if neutral and topic:
                prefix = personalities[personality]['prefix']
                suffix = personalities[personality]['suffix']
                print(f'{prefix}{neutral}. {suffix}')
            else:
                print(personalities[personality]['default'])
                handled = True

        # machine learning
        if send in know and not handled:
            print(know[send])
            stay[send] = stay.get(send, 0) + 1
            conversation['topic'] = send
            handled = True
        if not handled:
            print(personalities[personality]['default'])
            learn = input('Qual a resposta?')
            if learn.lower() != 'nao':
                know[send] = learn
                print('Entendido.')

                stay[send] = 1
                stay['learn'] = stay.get('learn', 0) + 1
                conversation['topic'] = send

                save(know, know_files)


# program initialization
if __name__ == '__main__':
    run()
