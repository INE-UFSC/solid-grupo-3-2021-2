"""
Single Responsibility Principle
Uma classe deve ter somente uma responsabilidade
ou
Uma classe deve ter somente um motivo para mudar
"""

'''class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        pass

    # salva no DB
    def save(self, animal: Animal):
        pass'''

class Animal:
    def __init__(self, name: str, system: Sistema):
        self.name = name
        self.system = system
    
    def get_name(self) -> str:
        pass

class Sistema:
    def __init__(self):
        pass
    
    def save(self,animal: Animal):
        pass
