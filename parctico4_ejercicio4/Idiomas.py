from Dialogo import Dialogo

class Ingles(Dialogo):
    def __init__(self,saludo,despedida,disculpa,cafe,precio,ubicacion):
        super().__init__()
        self.saludo="hi! how are you?"
        self.despedida="good bye!"
        self.disculpa="my fault, so sorry my nigga"
        self.cafe="can u give me a coofe,plis?"
        self.precio="what is the price my nigga?"
        self.ubicacion="where is this location bro?"
    
    def saludar(self):
        return self.saludo
    
    def despedirse(self):
        return self.despedida
    
    def perdon(self):
        return self.disculpa
    
    def pedirCafe(self):
        return self.cafe
    
    def cuantoCuesta(self):
        return self.precio
    
    def dondeQueda(self):
        return self.ubicacion

class Frances(Dialogo):
    def __init__(self,saludo,despedida,disculpa,cafe,precio,ubicacion):
        super().__init__()
        self.saludo="Salut! comment vas-tu?"
        self.despedida="Au revoir!"
        self.disculpa="Je suis désolé"
        self.cafe="Pourriez-vous me donner un café s’il vous plaît ?"
        self.precio="Combien cela coûte-t-il?"
        self.ubicacion="Pourriez-vous me dire où se trouve cet endroit, s’il vous plaît?"
    
    def saludar(self):
        return self.saludo
    
    def despedirse(self):
        return self.despedida
    
    def perdon(self):
        return self.disculpa
    
    def pedirCafe(self):
        return self.cafe
    
    def cuantoCuesta(self):
        return self.precio
    
    def dondeQueda(self):
        return self.ubicacion

class Portugues(Dialogo):
    def __init__(self,saludo,despedida,disculpa,cafe,precio,ubicacion):
        super().__init__()
        self.saludo="Olá! como estás?"
        self.despedida="Adeus;!"
        self.disculpa="Peço desculpa"
        self.cafe="Você poderia me dar um café, por favor?"
        self.precio="Quanto custa?"
        self.ubicacion="Você poderia me dizer onde este lugar está localizado, por favor?"
    
    def saludar(self):
        return self.saludo
    
    def despedirse(self):
        return self.despedida
    
    def perdon(self):
        return self.disculpa
    
    def pedirCafe(self):
        return self.cafe
    
    def cuantoCuesta(self):
        return self.precio
    
    def dondeQueda(self):
        return self.ubicacion