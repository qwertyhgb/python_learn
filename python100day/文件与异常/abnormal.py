def main():
    f = None
    try:
        f = open('C:/Users/LM216/Desktop/1.txt', 'r', encoding = 'utf-8')
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定文件')
    except LookupError:
        print('指定未知编码!')
    except UnicodeDecodeError:
        print('读取文件解码时错误!')
    finally:
        if f:
            f.close()


if __name__ == '__main__':
    main()




























