def mode(x):
    return {
        'software': 1,
        'cuda': 2,
        'opencl': 3
    }.get(x, 1)


def mode_img(x):
    return {
        'rgb': 1,
        'rgba': 2,
        'hsb': 3
    }
