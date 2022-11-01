def serialize(file):
    output = ""
    with open(file, 'w') as f:
        for line in f:
            line = line[::-1]
            output += "\n"
            for char in line:
                if line.count(char) > 0:
                    output += str(line.count(char)) + char
                    line = line.replace(char, '')
                else:
                    continue
        return output


def deserialize(file: object) -> object:
    with open(file, 'r') as f:
        output = ''
        des = ''
        for row in f:
            des = ''
            for char in row:
                if char.isdigit():
                    des += char
                else:
                    output += int(des) * char
                    des = ''
            output += '\n'
        return output


def conversion_table(t, input_num, table):
    with open(t, 'r') as t:
        with open(t, 'w') as t:
            content = t.read()
            for char in content:
                if char in table:
                    content = content.replace(char, table[char][input_num - 1])
                elif char != '\n':
                    content = content.replace(char, 'X')
            return serialize(t.write(content))


def rotation(file, angle):
    with open(file, 'r') as t:
        content = t.read()
        if angle == 180:
            return rotation(content[::-1], 360)
        elif angle == 270:
            return rotation(content[::-1], 90)
        lines = t.readlines()
        rot = ''
        if angle == 360:
            for line in lines:
                rot += line[::-1] + '\n'
            return rot[:-1:]
        if angle == 90:
            content = ''
            for i in range(len(lines[0])):
                for line in lines[::-1]:
                    content += line[i]
                content += '\n'
            return content


def main():
    ser_ascii = False
    con_ascii = False

    file = str(input(r"enter your file path: "))
    tempfile = str(input(r"where would you like to save a temp file? (file destination) -  "))
    try:
        f = open(file, 'r')
        f.close()
        t = open(tempfile, 'w')
        f.close()
    except FileNotFoundError:
        print("can't find your file.. , try again\n   :")
        main()
        return None
    choice = str(input('would you like to serialize / deserialize (s / d)?   :'))
    if choice in ['serialize', 's']:
        t = open(tempfile, 'w')
        t.write(serialize(choice))
        print(serialize(choice))
        ser_ascii = True
        t.close()
    elif choice in ['deserialize', 'd']:
        if not ser_ascii:
            t.write(serialize(choice))
        t = open(tempfile, 'r')
        print(str(deserialize(t)))
        t.close()
    else:
        print('not one of the choices,\n try again')
        main()
        return None
    table = {'(': ['^', '$'], '$': [';', '!'], '*': ['|', 'o']}
    print("The conversion table is", table)
    input_num = int(input("How would you like to convert the characters using the conversion table? [0, 1, 2]: "))
    if input_num in [0, 1, 2]:
        if ser_ascii:
            t = open(tempfile, 'w')
            t.write(deserialize(t))
            t.close()
        t = open(tempfile, 'w')
        t.write((conversion_table(t, input_num, table)))
        t.close()
        print(str(conversion_table(t, input_num, table)))
    r = str(input('would you like to rotate the image? (True / False(T/F): '))
    while not r in ['T', 'F', 'True', 'False']:
        r = str(input('Error, try again: \n rotate image? (True / False): '))
    if r in ['T', 'True']:
        angle = int(input('enter rotate angle: '))
        while not angle in [90, 180, 270, 360]:
            angle = int(input('Error, try again \n enter rotate angle: '))
        print(rotation(file, angle))

if __name__ == '__main__':
    main()


