"""
Mid Term Exam Cinema Hall Seat booking system.
Md Ahasanul Alam

"""

class Start_Cinema:
    hall_list = []
    @classmethod
    def entry_hall(self, hall):
        self.hall_list.append(hall)

class Hall:
    def __init__(self, rows, cols, hall_no) -> None:
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no

        self.__seats = {}
        self.__show_list = []
        Start_Cinema.entry_hall(self)
    
    def entry_show(self, id, movie_name, show_time):
        show_data = (id, movie_name, show_time)
        self.__show_list.append(show_data)
        
        seats = [[0 for _ in range(self.__cols)] for _ in range(self.__rows)]
        self.__seats[id] = seats 

    def book_seats(self, show_id, seats_to_book):
        if show_id not in [show[0] for show in self.__show_list]:
            raise ValueError(f'\t{show_id} is an Invalid Show ID!! ')
        
        seats = self.__seats.get(show_id)
        if seats is None:
            raise ValueError(f'\tThis {show_id} Show is not Scheduled!! ')
        
        for seat in seats_to_book:
            row, col = seat
            if not (0 <= row < self.__rows and 0 <= col < self.__cols):
                raise ValueError('\tInvalid Seat!! ')
            
            if seats[row][col] == 1:
                raise ValueError('\tSeat Already Booked!! ')
            
            seats[row][col] = 1

    def view_show_list(self):
        show_len = len(self.__show_list)
        try:
            if show_len == 0:
                raise ValueError(f'\tNo Shows are Scheduled!! ')
            else:
                print('\tAvailable Shows in Cinema:: \n')
                for show in self.__show_list:
                    print(f'\tMovie Name:{show[1]} || Show ID:{show[0]} || Show Time:{show[2]}')
        except ValueError as error:
            print((f'\tAlert: {error}'))
        
    def view_available_seats(self, show_id):
        seats = self.__seats.get(show_id)
        if seats is None:
            raise ValueError(f'\tThis {show_id} Show is not Scheduled!! ')
        
        print(f'\n\tAvailable Seats of the Show {show_id} as below: [ 0 = Available & 1 = Booked ] \n')
        for i in range(self.__rows):
            for j in range(self.__cols):
                print(f'\t{seats[i][j]} ', end='')
            print()
    

print(f'\n------------------ Create a Hall -------------------\n')
hall_no = input('\tEnter the Hall Number: ')
rows = int(input('\tEnter The Available Rows for the Hall: '))
cols = int(input('\tEnter The Available Columns for the Hall: '))
hall = Hall(rows, cols, hall_no)
print(f'\n\tA New HALL : [ {hall_no} ] has been created successfully!!\n')

while True:
    print(f'\n---------------- Select your Choice -----------------\n')
    print('\t1 : Schedule a Show!')
    print('\t2 : Book Your Seats!')
    print('\t3 : View all Show List!')
    print('\t4 : View Available Seats for the Show!')
    print('\t5 : Exit from System..!\n')

    choice = int(input('\tENTER YOUR CHOICE: '))

    if choice == 1:
        id = input('\tEnter the Show ID: ')
        movie_name = input('\tEnter the Movie Name: ')
        show_time = input('\tEnter the Show Time ( hh:mm ): ')
        hall.entry_show(id, movie_name, show_time)
        print(f'\n\t{movie_name} show Scheduled Successfully at {show_time} !!\n')

    elif choice == 2:
        show_id = input('\tEnter the Show ID: ')
        try:
            no_of_tickets = int(input(f'\tEnter Number of Seats to Book for the Show {show_id}: '))
            rows = no_of_tickets
            cols = no_of_tickets
            seats_to_book = [(int(input(f'\tEnter ROW number for Seat {i + 1} to Book: ')) - 1, int(input(f'\tEnter COLUMN number for Seat {i + 1} to Book: ')) - 1) for i in range(rows)]

            hall.book_seats(show_id, seats_to_book)
            print(f'\n\t{no_of_tickets} Seats Booked Successfully!!\n')

        except ValueError as error:
            print(f'\n\tAlert! {error}\n')

    elif choice == 3:
        hall.view_show_list()

    elif choice == 4:
        show_id = input('\tEnter the Show ID: ')
        try:
            hall.view_available_seats(show_id)
        except ValueError as error:
            print(f'\n\tAlert! {error}\n')

    elif choice == 5:
        break

    else:
        print(f'\n\tAlert: [ {choice} ] is an invalid choice! Please Try again the correct Choice!! \n')
