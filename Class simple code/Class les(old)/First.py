class Human:
    def get_age(self,this_year):
        print(2024-self.year_of_birth)

    def print_info(self,n):
        for i in range(n):
            print(f'Name {self.name}, Surname {self.surname}, Plase of birth {self.place_fo_birth}')

p1=Human()

p1.name='Elon'
p1.surname='Musk'
p1.place_fo_birth='Юар'
p1.year_of_birth=1970

p2=Human()

p2.name='i_m'
p2.surname='my_famuly'
p2.place_fo_birth='Novokuznesk'
p2.year_of_birth=1900

p1.print_info(1)
p2.print_info(4)
p1.get_age(2024)
p2.get_age(2024)
