with open('message.txt', 'r') as file:
    file.seek(15)
    string = file.read(5)
    print(string)
    