# Um pai de familia precisa de um software
#que calcule o momento de trocar o óleo.

class Veiculo:
    def __init__(self,descricao):
        self.descricao = descricao

    def get_descricao(self):
        return self.descricao
def main():
    obj1 = Veiculo ("Prisma")
    print(f"descrição: {obj1.get_descricao()}")

if __name__ == "__main":
    main()