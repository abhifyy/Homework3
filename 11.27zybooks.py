"""

Abhmanyu Kidarithil Meethal
PSID:2105385

"""
roster = {}
for i in range(1, 6):
    jersey_number = int(input("Enter player {}'s jersey number:\n".format(i)))
    rating = int(input("Enter player {}'s rating:\n".format(i)))
    if i != 5:
        print()
    roster[jersey_number] = rating
sorted_roster = sorted(roster.items())
print("\nROSTER")
for jersey_number, rating in sorted_roster:
    print("Jersey number: {}, Rating: {}".format(jersey_number, rating))
choice = ''
while choice != 'q':
    print("\nMENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit")
    choice = input("\nChoose an option:\n")

    if choice == 'o':
        print("\nROSTER")
        for jersey_number, rating in sorted_roster:
            print("Jersey number: {}, Rating: {}".format(jersey_number, rating))
    elif choice == 'a':
        jersey_number = int(input("\nEnter a new player's jersey number: "))
        rating = int(input("Enter the player's rating: "))
        roster[jersey_number] = rating
        sorted_roster = sorted(roster.items())
    elif choice == 'd':
        jersey_number = int(input("\nEnter a jersey number: "))
        if jersey_number in roster:
            del roster[jersey_number]
            sorted_roster = sorted(roster.items())
    elif choice == 'u':
        jersey_number = int(input("\nEnter a jersey number: "))
        if jersey_number in roster:
            new_rating = int(input("Enter a new rating for player: "))
            roster[jersey_number] = new_rating
            sorted_roster = sorted(roster.items())
    elif choice == 'r':
        rating_threshold = int(input("\nEnter a rating: "))
        print("\nABOVE", rating_threshold)
        for jersey_number, rating in sorted_roster:
            if rating > rating_threshold:
                print("Jersey number: {}, Rating: {}".format(jersey_number, rating))
