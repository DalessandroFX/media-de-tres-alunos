class nota:
    qaluno = 0
    def __init__(self,pnota):
        self.pnota = pnota
        nota.qaluno +=1
    def media (self, snota):
        mf = (self.pnota + snota)/2
        print("o aluno ",nota.qaluno,"º foi", mf)
aluno1 = nota(float(input("qual a sua primeira nota:")))
aluno1.media(float(input("qual a sua segunda nota:")))
aluno2 = nota(float(input("qual a sua primeira nota:")))
aluno2.media(float(input("qual a sua segunda nota:")))
aluno3 = nota(float(input("qual a sua primeira nota:")))
aluno3.media(float(input("qual a sua segunda nota:")))