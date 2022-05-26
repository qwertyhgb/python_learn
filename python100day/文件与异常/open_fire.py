def main():
    f = open('test.txt', 'r', encoding='utf-8')  # ‘r’为读取的意思
    print(f.read())
    f.close()


if __name__ == '__main__':
    main()
