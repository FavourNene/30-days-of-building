import random, string
def generate_random_id():
    characters = string.ascii_letters + string.digits
    random_id = ''.join(random.choice(characters) for _ in range(6))
    return random_id

print(generate_random_id())

def user_id_gen_by_user_input():
   
        num_ids = int(input("Enter the number of user IDs to generate: "))
        id_length = int(input("Enter the length of each user ID: "))
        
        characters = string.ascii_letters + string.digits
        user_ids = [''.join(random.choice(characters) for _ in range(id_length)) for _ in range(num_ids)]
        
        return user_ids

print(user_id_gen_by_user_input())


def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r}, {g}, {b})"

print(rgb_color_gen())


def hexa_color_gen():
    
    characters = string.hexdigits[:16].lower()  # 0-9 and a-f
    return '#' + ''.join(random.choice(characters) for _ in range(6))
    return hexa_color


print(
    hexa_color_gen())


def list_of_rgb_colors():
     r = random.randint(0, 255)
     g = random.randint(0, 255)
     b = random.randint(0, 255)

     num =input("How many RGB numbers do you want to generate?: ")
     num =int(num)
     RGB_List =[(r, g, b) for _ in range(num)]
     return RGB_List

print(list_of_rgb_colors())


def gen_colors(mode, count):
    colors = []
    if mode == 'hexa':
        for _ in range(count):
            colors.append(hexa_color_gen())
    elif mode == 'rgb':
        for _ in range(count):
            colors.append(rgb_color_gen())
    return colors     

def shuffle_list(items):
    """Return a new shuffled copy of `items`. The original list is unchanged."""
    shuffled = items.copy()
    random.shuffle(shuffled)
    return shuffled

import random

def shuffle_list(items):
    """Return a new shuffled copy of `items`. The original list is unchanged."""
    shuffled = items.copy()
    random.shuffle(shuffled)
    return shuffled