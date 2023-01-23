import sys
import requests
import hashlib

# Response api function
def request_api_data(query_char):
    url = "https://api.pwnedpasswords.com/range/" + query_char
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(
            f"Error fetching: {response.status_code}, check the API and try again."
        )
    return response


# def read_response(response):
#     print(response.text)

# Match count function
def get_leaks_count(hashes, hash_to_check):
    hashes = (line.split(":") for line in hashes.text.splitlines())
    for h, count in hashes:
        # print(h, count)
        # check if match is found
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    # grab first 5 characters
    first5_char, tail = sha1password[:5], sha1password[5:]
    # get API response
    response = request_api_data(first5_char)
    # return count
    return get_leaks_count(response, tail)


# pwned_api_check("123")
# request_api_data("123")


def main(args):
    """
    Main function to loop through all passwords and
    return count.
    """
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(
                f"{password} was found {count} times...\nYou should probably change your password."
            )
        else:
            print(f"{password} was NOT found. Carry on!")

    return "Check completed!"


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
