# Chars to handle when dealing with a json string
QUOTE = '"'
COLON = ":"
COMMA = ","
TRUE_CHAR = "t"
FALSE_CHAR = "f"
NULL_CHAR = "n"
OPEN_BRACKET = "{"
CLOSE_BRACKET = "}"
OPEN_LIST = "["
CLOSE_LIST = "]"
EMPTY = " "


def main(s):
    index = 0

    def parse_value():
        """
        This is the generic entrypoint for the start and as well
        new entities within the json object

        This allows us to not have to make any clever tricks the initialization
        for the string, we can simply run through all the characters from the start
        """
        nonlocal index

        if s[index] == OPEN_BRACKET:
            return parse_object()
        if s[index] == QUOTE:
            return parse_string()
        if s[index].isdigit():
            return parse_int()

    def parse_int():
        nonlocal index
        res = ""
        while index < len(s):
            if s[index] in [COMMA, CLOSE_BRACKET, CLOSE_LIST]:
                break
            res += s[index]
            index += 1

        return int(res)

    def parse_object() -> dict:
        # Increment the index since we are currently on an opening bracket
        nonlocal index
        index += 1
        obj = {}

        while index < len(s):
            if s[index] == CLOSE_BRACKET:
                break

            # If we end up on a comma, we likely have more than one key so
            # we can skip over this index and continue
            #
            # The same can be done for spaces before keys
            if s[index] == COMMA or s[index] == EMPTY:
                index += 1
                continue

            key = parse_string()
            # Currently the strings won't contain any white space unless
            # it is within a string, so we can safely increment the index by
            # one to jump over the colon
            index += 1
            value = parse_value()

            obj[key] = value

        return obj

    def parse_string():
        nonlocal index
        index += 1
        res = ""
        while index < len(s):
            if s[index] == QUOTE:
                break
            res += s[index]
            index += 1

        # Increment once more so that we are off the quote index
        index += 1

        return res

    return parse_value()


if __name__ == "__main__":
    # Our test string to convert into a dictionary
    TEST = """
    {"key number 1":"hello","other":"world",  "int_value":123}
    """

    # Stripping the string will confirm that the first character in the string
    # will be the opening bracket for the entire object
    TEST = TEST.strip()

    ans = main(TEST)
    print(ans)
