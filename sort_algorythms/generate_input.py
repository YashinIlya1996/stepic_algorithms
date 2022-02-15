def generate_input(length=10 ** 5, max_value=10 ** 9):
    import random
    with open('input.txt', 'w') as file:
        for i in range(length):
            file.write(str(random.randint(1, max_value)) + ' ')
