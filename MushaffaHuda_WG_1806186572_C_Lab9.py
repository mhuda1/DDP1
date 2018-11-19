# class utama untuk programmer

class Programmer:
    
    def __init__(self, name, intelligence):
        self.name = name
        self.intelligence = intelligence
        self.progress = 0.0
        self.maks = 100.0

    # fungsi untuk coding

    def coding(self, time):
        if self.progress < self.maks:
            self.progress += time * self.intelligence
            return self.name + ' telah  ngoding selama ' + str(time) + ' jam'
        else:
            return self.name + ' telah menyelesaikan proyeknya'
        if self.progress > self.maks:
            self.progress == self.maks
            return self.name + ' telah mennyelesaikan proyeknya.'

# class untuk professional programmer

class ProfessionalProgrammer(Programmer):
    def __init__(self, name, intelligence):
        super().__init__(name, intelligence)
    
    def focused_coding(self, time):
        if self.progress < self.maks:
            self.progress += (time * self.intelligence) * 2
            return self.name + ' telah  ngoding secara fokus selama ' + str(time) + ' jam'
        else:
            return self.name + ' telah menyelesaikan proyeknya.'
        if self.progress > self.maks:
            self.progress == self.maks
            return self.name + ' telah menyelesaikan proyeknya.'

# class untuk enthusiast programmer

class EnthusiastProgrammer(Programmer):
    
    def __init__(self, name, intelligence):
        super().__init__(name, intelligence)
        self.maks = 150.0

    def coding(self, time):
        super().coding(time)

# class untuk average programmer

class AverageProgrammer(Programmer):
    def __init__(self, name, intelligence):
        super().__init__(name, intelligence)

# main class company

class Company:
    def __init__(self):
        self.programmers = {}
    
    # fungsi untuk merekrut programmer
    def recruit_programmer(self, tier, name, intelligence):
        if (tier == 'PROFESSIONAL PROGRAMMER'):
            programmer = ProfessionalProgrammer(name, intelligence)
        elif (tier == 'ENTHUSIAST PROGRAMMER'):
            programmer = EnthusiastProgrammer(name, intelligence)
        elif (tier == 'AVERAGE PROGRAMMER'):
            programmer = AverageProgrammer(name, intelligence)
        else:
            print('Tier ' + tier + ' tidak ditemukan')
            return

        self.programmers[name] = programmer
        print(name + ' direkrut')
    # fungsi untukmendapatkan nama programmer
    def get_programmer(self, name):
        return self.programmers.get(name)
    
    def is_recruited(self, name):
        return name in self.programmers

if __name__ == "__main__":
    company = Company()

    while (True):
        command = input('').upper().split(';')

        # perintah untuk merekekrut programmer
        if (command[0] == 'RECRUIT'):
            if (company.is_recruited(command[2])):
                print(command[2] + ' telah direkrut sebelumnya')
            else:
                company.recruit_programmer(command[1], command[2], int(command[3]))

        # perintah untuk coding
        if (command[0] == 'CODING'):
            programmer = company.get_programmer(command[1])
            print(programmer.coding(int(command[2])))

        # perintah untuk focused coding
        if (command[0] == 'FOCUSED CODING'):
            programmer = company.get_programmer(command[1])
            if type(programmer) == ProfessionalProgrammer:
                print(programmer.focused_coding(int(command[2])))
            else:
                print(programmer.name + ' tidak dapat melakukan perintah tersebut.')
        
        # perintah untuk mengecek progress
        if (command[0] == 'PROGRESS'):
            programmer = company.get_programmer(command[1])
            try:
                print('Progress {}: {}'.format(command[1],programmer.progress))
            except AttributeError:
                print(command[1] + ' tidak ditemukan dalam perusahaan ini.')
        
        # Format perintah: EXIT
        if (command[0] == 'EXIT'):
            break
