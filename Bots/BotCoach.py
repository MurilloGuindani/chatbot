from Bots.Bot import Bot

class BotZangado(Bot):
    def __init__(self, comandos):        
        super().__init__(comandos)
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,nome):
        self.__nome = nome

    def apresentacao(self):
        return "Eu sou o BotCoach e estou aqui para despertar o seu potencial evolutivo e girar a chave da sua vida"
 
    def mostra_comandos(self):
        c = 0
        for key in self.__comandos:
            c += 1
            return str(c) + " - " + key
    
    def executa_comando(self,cmd):
        return self.__comandos[cmd]

    def boas_vindas(self):
        return "Oi, quer mudar a sua vibraçao? Eu posso mudar o seu DNA quantico da quinta dimensao por apenas R$ 40.000,00"

    def despedida(self):
        return "Adeus, pena que não consegui mudar seu mindset ;////"