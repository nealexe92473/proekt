class Person:
    def __init__(self, fam, name, otchestvo, rabdni, podr, zp):
        self.fam = fam
        self.name = name
        self.otchestvo = otchestvo
        self.rabdni = rabdni
        self.podr = podr      
        self.zp = zp

class Grup:
    def __init__(self):
        self.A = {}
        self.count = 0

    def __str__(self):
        s = ''
        for x in range(len(self.A)):  
            if x in self.A: 
                s += f'Person {x+1}:\n'
                s += str(self.A[x])
                s += '\n'
        return s

      


    def read_data_from_file(self, filename):
        self.A = {}
        x = 0
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                if line[-1] == '\n' : line = line[:-1] 
                parts = line.strip().split(" ")

                self.A[x] = Person(parts[0],parts[1],parts[2],parts[3],parts[4],parts[5])

                x += 1
                self.count += 1

       
