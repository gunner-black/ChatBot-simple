# ChatBot-simple (Chatbot Simples com Personalidade e Aprendizado)
# Introdução
Este é um projeto acadêmico de um chatbot simples desenvolvido em Python. Ele foi criado para demonstrar habilidades fundamentais de programação, como o uso de estruturas de dados, laços de repetição e estruturas condicionais. O objetivo principal é simular um assistente de conversação capaz de interagir com o usuário, aprender novas informações e até mesmo mudar sua "personalidade".

# Utilização
Para rodar o chatbot, siga os passos abaixo:
1.  Clone este repositório para a sua máquina local.
2.  Navegue até a pasta do projeto.
3.  Execute o arquivo principal (`seu_projeto.py` ou o nome que você deu ao seu arquivo) no terminal.
```bash
python seu_projeto.py
```
# Pontos de Personalização
O projeto foi construído para ser altamente personalizável. Os principais pontos que podem ser alterados ou expandidos são:
**1. Personalidades:** Novas personalidades podem ser adicionadas facilmente, basta incluir um novo conjunto de textos e saudações no dicionário de personalidades.
**2. Base de Conhecimento:** O dicionário de conhecimento pode ser expandido com novos tópicos e respostas, seja editando o código diretamente ou ensinando o bot durante a interação.
**3. Estatísticas:** O sistema registra dados como o número de interações e a frequência de uso de cada personalidade, permitindo o acompanhamento do comportamento do bot.

# Acessibilidade
A interface do chatbot é baseada em texto, operando diretamente na linha de comando. Isso garante que o projeto seja leve, rápido e intrinsecamente acessível para usuários que dependem de leitores de tela e outras tecnologias assistivas. Não há elementos gráficos que possam complicar a interação.

# Aprimoramento
Este projeto serve como uma base sólida e pode ser aprimorado com diversas funcionalidades. As mais importantes são:
**1. Persistência de Dados:** Implementar a gravação dos dados em arquivos (como JSON ou texto simples) para que o bot se lembre de suas interações e do que aprendeu mesmo após ser reiniciado.
**2. Novas Personalidades:** Adicionar personalidades de outras regiões ou com traços de humor diferentes para enriquecer a experiência do usuário.
**3. Melhoria na Detecção de Entrada:** Refinar a lógica de verificação de palavras-chave para que o bot possa entender melhor a intenção do usuário, mesmo com erros de digitação.

# Lógica e Abertura para Implementações
A lógica do projeto utiliza dicionários para armazenar e organizar informações, como as diferentes personalidades e a base de conhecimento. Laços de repetição `while` mantêm o fluxo de conversa, e estruturas condicionais `if`/`elif`/`else` são usadas para tomar decisões com base nas entradas do usuário. A modularidade do código permite que novas funcionalidades sejam adicionadas sem comprometer a estrutura existente, abrindo espaço para futuras implementações, como um sistema de aprendizado mais avançado ou uma interface gráfica.
