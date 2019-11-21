Extending OSRFramework
----------------------

Esta seção fornecerá informações sobre como estender as diferentes ferramentas
encontrado na estrutura.

### Criando novo usufy.py wrappers as plugins

Since OSRFramework 0.13.0, we have added the possibility of creating new
wrappers as plugins.

As coisas básicas que você deve saber para criar um novo wrapper são:
* A estrutura da URL vinculada ao perfil.
* A parte do código HTML que diz que o usuário NÃO existe.
* Um apelido válido que possui um perfil ativo no site.

Por exemplo, vamos usar uma rede social inventada:
`http://example.com/james` é a URL de um usuário chamado` james` na figura
plataforma. O erro retornado é `<title> 404 não encontrado </title>`. Vou ao
plugins/wrappers` folder in your home, copie e renomeie a pasta` wrapper.py.sample`
para `example.py`. Assim, você terá um modelo que poderá modificar.

Primeiro, mudaremos o nome do wrapper e as tags:
```
class Example(Platform):
    """
        A <Platform> object for Example.
    """
    def __init__(self):
        """
            Constructor...
        """
        self.platformName = "Example"
        self.tags = ["test"]
```

Diremos à estrutura que esta plataforma possui páginas de perfil no estilo habitual por
definindo como True a variável correspondente:
```
        ########################
        # Defining valid modes #
        ########################
        self.isValidMode = {}        
        self.isValidMode["phonefy"] = False
        self.isValidMode["usufy"] = True
        self.isValidMode["searchfy"] = False   
```

Forneceremos o padrão de URL:
```
        ######################################
        # Search URL for the different modes #
        ######################################
        # Strings with the URL for each and every mode
        self.url = {}        
        #self.url["phonefy"] = "http://anyurl.com//phone/" + "<phonefy>"
        self.url["usufy"] = "https://example.com/" + "<usufy>"       
        #self.url["searchfy"] = "http://anyurl.com/search/" + "<searchfy>"  
```

Saberemos se a plataforma precisa de credenciais para funcionar:
```
        ######################################
        # Whether the user needs credentials #
        ######################################
        self.needsCredentials = {}        
        #self.needsCredentials["phonefy"] = False
        self.needsCredentials["usufy"] = False
        #self.needsCredentials["searchfy"] = False
```

Em algumas plataformas, podemos agora que os nomes de usuário sempre correspondam a um determinado
expressão (por exemplo, o Twitter não permite '.' em um nome de usuário). Se isso é
Nesse caso, podemos modificar o atributo `validQuery`:
```
        #################
        # Valid queries #
        #################
        # Strings that will imply that the query number is not appearing
        self.validQuery = {}
        # The regular expression '.+' will match any non-empty query.
        #self.validQuery["phonefy"] = re.compile(".+")
        self.validQuery["usufy"] = re.compile(".+")   
        #self.validQuery["searchfy"] = re.compile(".+")
```

A última parte, é dizer à estrutura qual é a mensagem que aparece quando
o usuário não está presente. Esta é uma matriz, portanto, mais de uma mensagem pode ser usada
aqui.
```
        ###################
        # Not_found clues #
        ###################
        # Strings that will imply that the query number is not appearing
        self.notFoundText = {}
        #self.notFoundText["phonefy"] = []
        self.notFoundText["usufy"] = ["<title>404 not found</title>"]
        #self.notFoundText["searchfy"] = []  
```

E isso é quase tudo. Agora você pode testar o OSRFramework como de costume. Uma nova opção será
  esteja disponível na próxima vez que você executar o aplicativo.




