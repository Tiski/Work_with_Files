import logging
import time
import json
from pathlib import Path
import chardet

# Функция для определения кодировки файла
def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']

# Настройка логирования
project_root = Path('/Users/timurmajerle/Downloads/Python_Rabota_Failami/project_root')
log_file_path = project_root / 'logs' / 'script_log.log'
logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Скрипт запущен.")

# Начало работы: отметим время
start_time = time.perf_counter()

# Отслеживание времени для каждого задания
task_times = {}

# Логирование и время выполнения создания директорий
logging.info("Создание директорий начато.")
task_start = time.perf_counter()
dirs_to_create = [
    project_root / 'data' / 'raw',
    project_root / 'data' / 'processed',
    project_root / 'logs',
    project_root / 'backups',
    project_root / 'output'
]
for directory in dirs_to_create:
    directory.mkdir(parents=True, exist_ok=True)
    logging.info(f"Директория создана: {directory}")
task_times["Создание директорий"] = (time.perf_counter() - task_start) * 1000  # Время в миллисекундах
logging.info("Создание директорий завершено.")

# Логирование и время выполнения создания файлов с кодировками
logging.info("Создание файлов с кодировками начато.")
task_start = time.perf_counter()
raw_files = {
    'utf8_file.txt': ("Текст на русском языке.", 'utf-8'),
    'iso8859_file.txt': ("Texto en español con ISO-8859-1.", 'ISO-8859-1'),
    'utf8_file_jp.txt': ("日本語のテキスト。", 'utf-8')
}
for filename, (content, encoding) in raw_files.items():
    file_path = project_root / 'data' / 'raw' / filename
    with open(file_path, 'w', encoding=encoding) as f:
        f.write(content)
    logging.info(f"Файл создан: {filename} с кодировкой {encoding}")
task_times["Создание файлов с кодировками"] = (time.perf_counter() - task_start) * 1000  # Время в миллисекундах
logging.info("Создание файлов с кодировками завершено.")

# Логирование и время выполнения преобразования файлов
logging.info("Преобразование файлов начато.")
task_start = time.perf_counter()
raw_data_dir = project_root / 'data' / 'raw'
processed_data_dir = project_root / 'data' / 'processed'
for raw_file in raw_data_dir.iterdir():
    if raw_file.is_file():
        encoding = detect_encoding(raw_file)
        with open(raw_file, 'r', encoding=encoding) as f:
            content = f.read()
        transformed_content = content.swapcase()
        processed_file_name = raw_file.stem + '_processed' + raw_file.suffix
        processed_file_path = processed_data_dir / processed_file_name
        with open(processed_file_path, 'w', encoding='utf-8') as processed_file:
            processed_file.write(transformed_content)
        logging.info(f"Файл обработан: {processed_file_name}")
task_times["Преобразование файлов"] = (time.perf_counter() - task_start) * 1000  # Время в миллисекундах
logging.info("Преобразование файлов завершено.")

# Логирование и время выполнения создания отчёта
logging.info("Создание отчёта начато.")
task_start = time.perf_counter()
report_data = {
    "description": "Отчет о выполнении заданий проекта.",
    "difficulties": [
        "1. Ошибка с выбором интерпретатора Python была решена выбором правильного интерпретатора в VSCode.",
        "2. Модуль 'chardet' не был установлен в системе, что исправлено установкой через pip."
    ],
    "task_times": task_times,
    "conclusion": "Все задания выполнены успешно. Предложение: добавить больше автоматизированного логирования и контроль версий."
}



# Завершение работы
total_time = (time.perf_counter() - start_time) * 1000  # Время в миллисекундах
logging.info(f"Скрипт завершён. Общее время выполнения: {total_time:.2f} миллисекунд")
print(f"Общее время выполнения скрипта: {total_time:.2f} миллисекунд")
