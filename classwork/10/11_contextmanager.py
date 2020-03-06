class CM:

    def __exit__(self, *args):
        print("exit")
        print(*args)

    def __enter__(self):
        print("enter")
        return 1

cm = CM()

with cm as f:
    print(f)
    print("1111")


