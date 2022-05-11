import pyAesCrypt
import os


# функция дешифрования
def decryption(file, password):
    # задаём размер буфера
    buffer_size = 512 * 1024

    # вызываем метод дешифрования
    pyAesCrypt.decryptFile(
        infile=str(file),
        outfile=str(os.path.splitext(file)[0]),
        passw=password,
        bufferSize=buffer_size
    )

    # чтобы видеть резуультат выводим на экран имя зашифр. файла
    print(''.join(['Файл: ', str(os.path.splitext(file)[0]), ' дешифрован']))

    # удаляем исходный файл
    os.remove(file)


# Функция обхода директорий
def walking_by_dirs(dir, password):
    # перебираем все дочерние директории в указанной директории
    for i_name in os.listdir(dir):
        path = os.path.join(dir, i_name)

        # если находим файл, то дешифруем его
        if os.path.isfile(path):
            try:
                decryption(path, password)
            except Exception as error:
                print(error)
        # если попалась директория, то рекурсивно ныряем в неё
        else:
            walking_by_dirs(path, password)


password = input('Введите пароль для дешифрования: ')
work_dir_path = input('Введите путь для рабочей директории: ')
walking_by_dirs(work_dir_path, password)