#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    def not_built_in(str):
        if str[0:2] == '__':
            return False
        return True

    names = sorted(filter(not_built_in, dir(hidden_4)))
    for name in names:
        print(name)
