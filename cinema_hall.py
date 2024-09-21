class Star_Cinema:
    _hall_list = []

    @classmethod
    def entry_hall(cls, new_hall):
        for hall in Star_Cinema._hall_list:
            if hall._hall_no == new_hall._hall_no:
                print(f"{new_hall._hall_no} alreadey exists")
                return
        else:
            cls._hall_list.append(new_hall)
            print(
                f"***Hall '{new_hall._hall_no}' has been added to Star_cinema successfully***"
            )


class Hall:
    def __init__(self, rows, cols, hall_no):
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        self._showlist = []
        self._seats = {}

        Star_Cinema.entry_hall(self)

    def entry_show(self, show_id, movie_name, time):
        for show in self._showlist:
            if show_id == show[0]:
                print(f"The '{show_id}' no. show arleady exists!!\n")
                return
        self._showlist.append((show_id, movie_name, time))

        seats_layout = [[False for _ in range(self._cols)] for _ in range(self._rows)]
        self._seats[show_id] = seats_layout
        print(
            f"**Show '{movie_name}' at '{time}' has been added with ID '{show_id}'**\n"
        )

    def book_seats(self, show_id, seats_to_book):
        if show_id not in self._seats:
            print(f"Show ID {show_id} does not exist!!\n")
            return

        seats_layout = self._seats[show_id]

        for seat in seats_to_book:
            row, col = seat
            if row < 1 or row > self._rows or col < 1 or col > self._cols:
                print(f"Seat {row},{col} is invalid!!\n")
                continue
            if seats_layout[row - 1][col - 1]:
                print(f"Seat {row},{col} is already booked!!\n")
            else:
                seats_layout[row - 1][col - 1] = True
                print(f"**Seat {row},{col} has been booked successfully**\n")

    def view_show_list(self):
        if not self._showlist:
            print("No shows are currently available now!\n")
            return
        print(f"Shows in Hall {self._hall_no} :\n")
        print("Show_ID\t\tMovie_Name\t\tTime")
        for show in self._showlist:
            print(f"{show[0]}\t\t{show[1]}\t\t{show[2]}")

    def view_available_seats(self, show_id):
        if show_id not in self._seats:
            print(f"Show ID {show_id} does not exist!!\n")
            return

        seats_layout = self._seats[show_id]
        available_seats = []

        for i in range(self._rows):
            for j in range(self._cols):
                if not seats_layout[i][j]:
                    available_seats.append((i + 1, j + 1))

        if not available_seats:
            print(f"No available seats for show {show_id}!!\n")
            return

        print(f'Available seats for show "{show_id}":\n')
        print(available_seats)
        print("\n")


def get_hall(hall_no):
    for hall in Star_Cinema._hall_list:
        if hall_no == hall._hall_no:
            return hall
    return None


while True:
    print("\n----Star Cinema----")
    print("1. Add a Hall")
    print("2. Add a Show to a Hall")
    print("3. View Shows in a Hall")
    print("4. View Available Seats for a Show")
    print("5. Book Seats for a Show")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        rows = int(input("Enter number of rows : "))
        cols = int(input("Enter number of cols : "))
        hall_no = int(input("Enter hall no : "))
        hall = Hall(rows, cols, hall_no)

    elif choice == "2":
        hall_no = int(input("\nEnter Hall Number to add show: "))
        hall = get_hall(hall_no)
        if hall:
            show_id = input("Enter the show ID: ")
            movie_name = input("Enter the movie_name: ")
            time = input("Enter the time: ")
            hall.entry_show(show_id, movie_name, time)
        else:
            print(f"Hall {hall_no} does not exis!!\n")

    elif choice == "3":
        hall_no = int(input("\nEnter Hall Number to view showLists: "))
        hall = get_hall(hall_no)
        if hall:
            hall.view_show_list()
        else:
            print(f"{hall_no} does not exist!!\n")

    elif choice == "4":
        hall_no = int(input("\nEnter Hall Number : "))
        hall = get_hall(hall_no)
        if hall:
            show_id = input("Enter Show ID to view available seats: ")
            hall.view_available_seats(show_id)
        else:
            print(f"{hall_no} does not exist!!\n")

    elif choice == "5":
        hall_no = int(input("\nEnter Hall Number: "))
        hall = get_hall(hall_no)
        if hall:
            show_id = input("Enter Show ID to book seats: ")
            num_seats = int(input("Enter number of seats to book: "))
            seats_to_book = []
            for _ in range(num_seats):
                row = int(input("Enter Row Number: "))
                col = int(input("Enter Column Number: "))
                seats_to_book.append((row, col))
            hall.book_seats(show_id, seats_to_book)
        else:
            print(f"{hall_no} does not exist!!\n")

    elif choice == "6":
        print("---Thanks for using this service---")
        break
    else:
        print("Invalid choice number!!")
