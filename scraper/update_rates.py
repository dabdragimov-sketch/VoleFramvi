import json
import os

# Путь к файлу с курсами/ставками
rates_file = 'rates.json'

# Загружаем существующие данные или создаем пустые, если файла нет
if os.path.exists(rates_file):
    with open(rates_file, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = {}
else:
    data = {}

# Пример обновления данных (здесь можно добавить вашу логику парсинга)
data['status'] = "updated successfully"

# Сохраняем обновленные данные обратно в rates.json
with open(rates_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("Rates updated successfully!")
