def check_brackets(brackets_row: str) -> bool:
    """
    Проверьте, является ли входная строка допустимой последовательностью скобок

    :param brackets_row: Входная строка для проверки
    :return: True, если последовательность корректна, False в противном случае
    """
    ...  # TODO реализовать проверку скобочной группы
    stack = []
    open_brackets = ['(', '{', '[']
    close_brackets = [')', '}', ']']
    if not brackets_row:
        return True
    elif brackets_row[0] in close_brackets:
        return False
    for i in brackets_row:
        if i in open_brackets:
            stack.append(open_brackets.index(i))
        elif i in close_brackets:
            if len(stack) != 0 and stack[-1] == close_brackets.index(i):
                stack.pop()
            else:
                return False
    return len(stack) == 0


if __name__ == '__main__':
    print(check_brackets("()()"))  # True
    print(check_brackets(")("))  # False
