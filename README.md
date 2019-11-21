OSRFramework
============

OSRFramework: Open Sources de Pesquisa Framework

1 - Descrição
---------------

OSRFramework é um conjunto de bibliotecas GNU AGPLv3 + desenvolvido para executar
Tarefas de inteligência de código aberto. Eles incluem referências a um monte de diferentes
aplicativos relacionados à verificação de nome de usuário, pesquisas de DNS, pesquisa de vazamento de informações
, pesquisa profunda na Web, extração de expressões regulares e muitas outras.
Ao mesmo tempo, por meio de transformações ad-hoc de Maltego, o OSRFramework fornece
uma maneira de fazer essas consultas graficamente, bem como várias interfaces para
interagir com o OSRFConsole ou uma interface da Web.

2 - Instalação
----------------
Maneira rápida de fazer isso em qualquer sistema para um usuário com privilégios de administrador:
```
pip3 install osrframework
```
Você pode atualizar para a versão mais recente da estrutura com:
```
pip3 install osrframework --upgrade
```
Isso gerenciará todas as dependências para você e instalará a versão mais recente do
framework.

Se você precisar de mais informações sobre como instalar OSRFramework em certas
sistemas, observe que pode ser necessário adicionar `export PATH=$PATH:$HOME/.local/bin` para
seu `~/.bashrc_profile`). Isso foi confirmado em algumas distribuições,
Incluindo MacOS. De qualquer forma, recomendamos que você dê uma olhada no
[INSTALL.md](doc/INSTALL.md) arquivo onde fornecemos detalhes adicionais para esses
casos.

3 - Uso básico
---------------

Se tudo correu corretamente (esperamos que sim!), É hora de tentar usufy.py,
mailfy.py e assim por diante. Mas nós somos eles? Eles são instalados no seu caminho, o que significa
você pode abrir um terminal em qualquer lugar e digitar o nome do programa (parece
para melhorar as instalações anteriores ...). Exemplos:
```
osrf --help
usufy -n marrocamp febrezo yrubiosec -p twitter facebook
searchfy -q "marrocamp"
mailfy -n marrocamp
```

Tipo -h ou --help para obter mais informações sobre quais são os parâmetros de cada
aplicação.

Você pode encontrar os arquivos de configuração em uma pasta criada em sua página inicial do usuário para
defina o comportamento padrão dos aplicativos:
```
# Arquivos de configuração para Linux e MacOS
~/.config/OSRFramework/
# Arquivos de configuração para Windows
C:\Users\<User>\OSRFramework\
```

OSRFramework procurará as definições de configuração armazenadas lá. Você pode adicionar
novas credenciais e, se algo der errado, você sempre poderá restaurar o
arquivos armazenados no `defaults` subfolder.

Se você estiver enfrentando problemas, poderá obter informações relevantes no
(FAQ Section)[doc/FAQ.md].

4 - HACKING
-----------

Se você deseja estender as funcionalidades do OSRFramework e você não sabe
por onde começar, verifique o Arquivo [HACKING.md](doc/HACKING.md) 


