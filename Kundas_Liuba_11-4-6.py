class Centre:
    def __init__(self, patient, start=1):
        self.patient = patient
        self.ID = start

    def __iter__(self):
        return self

    def __next__(self):
        self.ID += 1
        return self.ID

    def Worker(self):
        dict_1 = {self.ID: self.patient}
        return dict_1

class Claim(Centre):
    def __init__(self):
        self.gene = gene

class Result(Centre):

    def __init__(self, genotype):
        self.genotype = genotype

class Document(Centre):
    def __init__(self, price):
        self.act = act
        self.price = price

patient_1 = Centre("Иванович Иван")
patient_2 = Centre("Иванович Иван2")
print(patient_2.Worker())
