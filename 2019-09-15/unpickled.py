from concurrent.futures import ProcessPoolExecutor


f = open('1.txt', 'a+')


def write(f, line):
    f.writeline(line)


with ProcessPoolExecutor() as executor:
    future = executor.submit(write, f, 'abc')
    print(f'RESULT: {future.result()}')
