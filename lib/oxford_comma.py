def oxford_comma(items):
    # add that "and " to last element
    if len(items) > 1:
        items[-1] = "and " + items[-1]

    # if greater than 2 items
    if len(items) > 2:
        return ', '.join(items)
    # if less than two items
    else:
        return ' '.join(items)

