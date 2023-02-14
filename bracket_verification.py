def verify_bracket(string):
    open_brack = ["[", "{", "("]
    close_brack = ["]", "}", ")"]

    stack = []  # stack for keeping income open_brackets
    for i in string:
        if i in open_brack:
            stack.append(i)
        elif i in close_brack:
            pos = close_brack.index(i)
            if ((len(stack) > 0) and
                    (open_brack[pos] == stack[len(stack) - 1])):
                stack.pop()
            else:
                return "False"
    if len(stack) == 0:
        return "True"
    else:
        return "False"


string_verif = "{{}{}()}()[])"  # string to verify

if __name__ == '__main__':
    print(string_verif, 'is', verify_bracket(string_verif))
