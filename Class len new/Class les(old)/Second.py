class Human:
    def __init__(self,name,surname,place_of_birth,year_of_birth):
        self.name = name
        self.surname = surname
        self.place_fo_birth = place_of_birth
        self.year_of_birth = year_of_birth

    def get_age(self,this_year):
        print(f'age={this_year-self.year_of_birth}')

    def print_info(self,n):
        for i in range(n):
            print(f'Name {self.name}, Surname {self.surname}, Plase of birth {self.place_fo_birth}')

p1=Human('Elon','Musk','ЮАР',1971)


p2=Human('i_m','my_family','Novokuznesk',1900)




p1.print_info(1)
p2.print_info(4)
p1.get_age(2024)
p2.get_age(2024)
