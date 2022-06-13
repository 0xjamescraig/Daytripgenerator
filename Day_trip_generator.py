import random

def choose_destination():
    destinations = ['The park', 'The movies', 'The library', 'Staying home', 'The gym']
    return random.choice(destinations)

def choose_restaurant():
    restaurants = ['Sushi', 'Burger Shack', 'Pizza', 'Teppanyaki']
    return random.choice(restaurants)

def choose_transportation():
    mode_of_transportation = ['car', 'train', 'bus', 'bike']
    return random.choice(mode_of_transportation)

def choose_entertainment():
    entertainments = ['Golf', 'Bowling', 'Scrabble', 'Gaming']
    return random.choice(entertainments)


def trip_generator():
    i = 0
    while(i < 4):
        i = 0
        print('-----Generating Trip-----')
        destination = choose_destination()
        print('Chosen Destination:', destination)
        y_n = input('Do you like the Destination ?: Y (Yes) N (No)')
        if y_n == 'Y':
            i += 1
            restaurant = choose_restaurant()
            print('Chosen Restaurant:', restaurant)
            y_n = input('Do you like the Restaurant ?: Y (Yes) N (No)')
            if y_n == 'Y':
                i += 1
                transportation = choose_transportation()
                print('Chosen Transportation:', transportation)
                y_n = input('Do you like the Transportation ?: Y (Yes) N (No)')
                if y_n == 'Y':
                    i += 1
                    entertainment = choose_entertainment()
                    print('Chosen Entertainment:', entertainment)
                    y_n = input('Do you like the Entertainment ?: Y (Yes) N (No)')
                    if y_n == 'Y':
                        i += 1
                        print('Trip Completed')
                    else:
                        continue
                else:
                    continue
            else:
                continue
        else:
            continue
            
            
trip_generator()
