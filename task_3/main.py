"""
3. Задание на закрепление знаний по модулю yaml.
 Написать скрипт, автоматизирующий сохранение данных
 в файле YAML-формата.
Для этого:

Подготовить данные для записи в виде словаря, в котором
первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа —
это целое число с юникод-символом, отсутствующим в кодировке
ASCII(например, €);

Реализовать сохранение данных в файл формата YAML — например,
в файл file.yaml. При этом обеспечить стилизацию файла с помощью
параметра default_flow_style, а также установить возможность работы
с юникодом: allow_unicode = True;

Реализовать считывание данных из созданного файла и проверить,
совпадают ли они с исходными.
"""

import yaml

# Подготовка данных для записи в файл
data = {
    "list": ["item1", "item2", "item3"],
    "number": 42,
    "nested_dict": {
        "key1": 100,
        "key2": 200,
        "key3": "€"
    }
}

with open('file.yaml', 'w', encoding='utf-8') as f:
    yaml.dump(data, f, allow_unicode=True, default_flow_style=False)

with open('file.yaml', 'r', encoding='utf-8') as f:
    loaded_data = yaml.safe_load(f)
print(loaded_data == data)  # True
