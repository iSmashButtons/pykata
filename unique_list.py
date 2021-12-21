def unique_list(l):
    """Removes duplicate elements from a list.
    list -> unique list."""
    ul = []
    for i in l:
        if i not in ul:
            ul.append(i)
    return ul

alist = [
    'peepee',
    'poopoo',
    'bing',
    'bong'
]

duped_list = [
    'pee',
    'pee',
    'poo',
    'poo',
    'bing',
    'bong',
    'bing',
    'bing'
]

print(unique_list(alist))
print(unique_list(duped_list))