def arithmetic_arranger(problems, logic=None):
    first = []
    second = []
    operator = []
    result = []
    first_line = ''
    second_line = ''
    point_line = ''
    result_line = ''

    if len(problems) > 5:
        return 'Error: Too many problems.'

    for i in range(len(problems)):
        problems[i] = problems[i].replace(' ', '')

        if '+' in problems[i]:
            operator.append('+')
            problems[i] = problems[i].split('+')

        elif '-' in problems[i]:
            operator.append('-')
            problems[i] = problems[i].split('-')

        else:
            return "Error: Operator must be '+' or '-'."

        if problems[i][0].isdigit() is False or problems[i][1].isdigit() is False:
            return "Error: Numbers must only contain digits."

        if len(problems[i][0]) > 4 or len(problems[i][1]) > 4:
            return "Error: Numbers cannot be more than four digits."

        if operator[i] == '+':
            result.append(int(problems[i][0]) + int(problems[i][1]))
        elif operator[i] == '-':
            result.append(int(problems[i][0]) - int(problems[i][1]))

        first.append(problems[i][0])
        second.append(problems[i][1])

        size = (max(len(first[i]), len(second[i])) + 2)
        first_line += first[i].rjust(size)
        second_line += operator[i] + second[i].rjust(size - 1)
        point_line += "-" * size
        result_line += str(result[i]).rjust(size)

        if len(problems) >= 1:
            if i < (len(problems) - 1):
                first_line += "    "
                second_line += "    "
                point_line += "    "
                result_line += "    "

            else:
                first_line += ""
                second_line += ""
                point_line += ""
                result_line += ""

    if logic:
        arranged_problems = first_line + '\n' + second_line + '\n' + point_line + '\n' + result_line
    else:
        arranged_problems = first_line + '\n' + second_line + '\n' + point_line

    return arranged_problems
