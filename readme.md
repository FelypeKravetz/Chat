Chat Server e Client em Python - Resumo
Este repositório contém uma implementação simples de um servidor e cliente de chat em Python, utilizando sockets e threading. O servidor permite que múltiplos clientes se conectem e troquem mensagens em tempo real.

Como Usar
Clone o repositório em sua máquina local:

Para iniciar o servidor de chat, execute o seguinte comando no terminal:

python main.py > opção 2
Você será solicitado a inserir a porta de escuta do servidor. Informe um número de porta válido (por exemplo, 8080).

Execute o cliente:
Para se conectar ao servidor de chat, execute o aplicativo do cliente com o seguinte comando:



python main.py > opção 2
Você será solicitado a inserir o endereço IP do servidor e o número da porta. Informe o endereço IP onde o servidor de chat está em execução e o mesmo número de porta que você usou para o servidor (por exemplo, 8080).

Comece a conversar:
Assim que o cliente estiver conectado ao servidor, você poderá trocar mensagens com outros clientes conectados. Digite suas mensagens e pressione Enter para enviá-las. Para sair do chat, digite "/sair" (sem aspas) e pressione Enter.

Recursos
Mensagens em tempo real: As mensagens são trocadas instantaneamente entre os clientes conectados.
Múltiplos clientes: O servidor pode lidar com várias conexões de clientes simultaneamente.
Tratamento de erros: As aplicações do servidor e cliente lidam de forma adequada com erros de conexão comuns.

Comandos Disponíveis:

Iniciar o servidor: Inicia o servidor de chat. O servidor ficará aguardando conexões na porta especificada.

Conectar ao servidor: Conecta-se ao servidor de chat. Você precisa fornecer o endereço IP do servidor e o número da porta.

Créditos: Mostra os créditos da criação do programa.

Sair: Encerra o programa.

Créditos

Este programa foi criado por Felype Kravetz. A última atualização deste programa foi feita em 27/07/2023.

Divirta-se conversando com esta simples implementação de servidor e cliente de chat! Sinta-se à vontade para modificá-la e melhorá-la de acordo com suas necessidades. Boa programação!