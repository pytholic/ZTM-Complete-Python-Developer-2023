def do_stuff(num=0):
    try:
        if num:
            return int(num) + 5
        else:
            result = "please enter number"
            return result
    except ValueError as e:
        return e
