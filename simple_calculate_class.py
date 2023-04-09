class Calculate:
    def add(self, a: int, b: int, c: int=0, debug=False) -> int:
        if debug:
            print(f'a: {a}, b: {b}, c: {c}')
        return a + b + c

    def sub(self, a: int, b: int, debug=False) -> int:
        if debug:
            print(f'a: {a}, b: {b}')
        return a - b

if __name__ == '__main__':
    c = Calculate()
    print('test:')
    print(f'5 + 8 = {c.add(5, 8)}')
    print(f'5 - 8 = {c.sub(5, 8)}')
    print(f'5 + 8 + 1 = {c.add(5, 8, 1)}')
    print(f'5 + 8 = {c.add(5, 8, debug=True)}')
