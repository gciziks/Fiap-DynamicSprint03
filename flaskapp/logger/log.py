
class LogClass:
    def __init__(self, file_name='desenvolvimento_log.txt'):
        self.file_name = file_name
        # Criando File de log caso ela não exista ainda
        with open(self.file_name, 'a') as file:
            file.write("Inicializando Log!.\n")
    
    def add_log(self, log_msg):
        # Adicionando o log no arquivo .txt gerado
        with open(self.file_name, 'a') as file:
            file.write(log_msg + '\n')
