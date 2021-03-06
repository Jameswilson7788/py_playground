import faker


def print_received():
    received = None
    while True:
        received = yield received
        print("Hello,", received)


def name_generator(times):
    fake = faker.Faker()
    for _ in range(times):
        yield fake.name()
    return 'Hello from name generator'


def generate_10_names():
    result = yield from name_generator(10)
    print("yield from statement received:", result)


if __name__ == '__main__':
    print_received_generator = print_received()
    next(print_received_generator)
    for name in generate_10_names():
        caller_received = print_received_generator.send(name)
        print("Caller received:", caller_received)
