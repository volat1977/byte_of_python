


def invert_dict(**kwargs):
    my_inverted_dict = dict()
    for k, v in kwargs.items():
        my_inverted_dict.setdefault(v, list()).append(k)
    return my_inverted_dict

print(invert_dict(c=1233, b=2222, d=23333))