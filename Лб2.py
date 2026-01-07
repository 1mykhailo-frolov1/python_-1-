import hashlib
import os

def generate_folder_hashes(folder_path, block_size=65536):
    """
    Считает SHA-256 для всех .txt файлов в указанной папке.
    Возвращает словарь с полными путями и хешами.
    """
    hashes = {}

    if not os.path.exists(folder_path):
        print(f"Папка не найдена: {folder_path}")
        return hashes

    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            full_path = os.path.join(folder_path, filename)
            try:
                sha256 = hashlib.sha256()
                with open(full_path, 'rb') as f:
                    while True:
                        data = f.read(block_size)
                        if not data:
                            break
                        sha256.update(data)
                file_hash = sha256.hexdigest()
                hashes[full_path] = file_hash
                print(f"Обработан файл: {full_path}")
            except IOError as e:
                print(f"Ошибка чтения файла {full_path}: {e}")

    return hashes


if __name__ == "__main__":
    folder_path = r"C:\Python"

    print("Обчисление SHA-256 хешей файлов...\n")
    file_hashes = generate_folder_hashes(folder_path)

    if file_hashes:
        print("\nРезультаты хешей файлов:")
        for path, h in file_hashes.items():
            print(f"{path}: {h}")
    else:
        print("Хеши не были рассчитаны ни для одного файла.")