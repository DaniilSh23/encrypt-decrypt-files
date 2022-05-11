import pyAesCrypt
import os


# функция шифрования
def encryption(file, password):

    # задаём размер буфера
    buffer_size = 512 * 1024

    # вызываем метод шифрования
    pyAesCrypt.encryptFile(
        infile=str(file),
        outfile=''.join([str(file), '.crp']),
        passw=password,
        bufferSize=buffer_size
    )

    # чтобы видеть резуультат выводим на экран имя зашифр. файла
    print(''.join(['Файл: ', str(os.path.splitext(file)[0]), ' зашифрован']))

    # удаляем исходный файл
    os.remove(file)


# Функция обхода директорий
def walking_by_dirs(dir, password):

    # перебираем все дочерние директории в указанной директории
    for i_name in os.listdir(dir):
        path = os.path.join(dir, i_name)

        # если находим файл, то шифруем его
        if os.path.isfile(path):
            try:
                encryption(path, password)
            except Exception as error:
                print(error)
        # если попалась директория, то рекурсивно ныряем в неё
        else:
            walking_by_dirs(path, password)


password = input('Введите пароль для шифрования: ')
work_dir_path = input('Введите путь для рабочей директории: ')
walking_by_dirs(work_dir_path, password)