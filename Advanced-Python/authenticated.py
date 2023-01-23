user1 = {"name": "Sorna", "valid": True}
user2 = {"name": "Sorna", "valid": False}


def authenticated(fn):
    def is_valid(*args, **kwargs):
        if args[0]["valid"] == True:
            fn(*args, **kwargs)

    return is_valid


@authenticated
def message_friends(user):
    print("message has been sent.")


message_friends(user1)
