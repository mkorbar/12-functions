
def print_greeting():
    print('Hello!')


def print_greeting_for_user(user_name):
    print("Hello " + user_name )


def print_many_times_greeting_for_user(user_name, num):
    for x in range(num):
        print("Hello " + user_name)


def construct_greeting_for_user(user_name):
    return "Hello " + user_name


if __name__ == '__main__':
    hello = print_greeting_for_user("Marjan")

    print_many_times_greeting_for_user("Gasper", 5)
    greeting = construct_greeting_for_user('Micka')

    print(greeting)
