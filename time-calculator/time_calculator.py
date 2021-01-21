def add_time(start, duration, day='None'):

    if "PM" in start:
        symbol = 'PM'

    elif "AM" in start:
        symbol = 'AM'

    if day != 'None':
        day = day.capitalize()

    global info

    # Separação dos termos
    start = start.split(" ")
    start = start[0].split(":")
    duration = duration.split(":")
    # Transformação em inteiros
    for i in range(len(start)):
        start[i] = int(start[i])
        duration[i] = int(duration[i])
    # Soma
    if symbol == 'PM':
        start[0] = 12 + start[0]

    hour = start[0] + duration[0]
    minutes = start[1] + duration[1]
    value = hour // 24

    # Condicional - Horas e minutos
    if hour >= 24:
        hour = hour - (24 * value)

    if minutes > 59:
        hour = hour + (minutes // 60)
        minutes = minutes % 60

    # Condicional - Resultado PM ou AM
    if hour == 24:
        hour = 12
        period = 'AM'

        if value < 1:
            info = '(next day)'
            num = 1

        elif value >= 1:
            info = f'({value + 1} days later)'
            num = value + 1

        else:
            info = ''
            num = 0

    elif hour > 11:
        period = 'PM'

    else:
        period = 'AM'

    # Número de dias
    if hour != 12:
        if value == 1:
            info = '(next day)'
            num = 1

        elif value > 1:
            info = f'({value} days later)'
            num = value

        else:
            info = ''
            num = 0
    # Dia da semana
    week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    if day in week:

        for k in range(7):
            if week[k] == day:
                count = k

        num += count

        while num > 6:
            num -= 7
    # Converter em String e ajustar minutos
    if hour > 12:
        hour = hour - 12
        hour = str(hour)

    if minutes < 10:
        minutes = str(minutes)
        minutes = '0' + minutes

    else:
        minutes = str(minutes)

    # Resultado
    if day not in week:
        if info == '':
            new_time = f"{hour}:{minutes} {period}"

        else:
            new_time = f"{hour}:{minutes} {period} {info}"

    elif day in week:
        if info == '':
            new_time = f"{hour}:{minutes} {period}, {week[num]}"

        else:
            new_time = f"{hour}:{minutes} {period}, {week[num]} {info}"

    return new_time
