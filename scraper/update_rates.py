import os
import json
from supabase import create_client, Client

# Получаем ключи доступа из секретов GitHub Actions
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

# Инициализируем клиент Supabase, если ключи заданы
supabase: Client = None
if SUPABASE_URL and SUPABASE_KEY:
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def update_rates():
    # Путь к локальному файлу с курсами/ставками
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

    # Пример обновления данных
    data['status'] = "updated successfully"
    
    # Сохраняем обновленные данные обратно в rates.json
    with open(rates_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print("Rates updated successfully in local file!")

    # Отправляем данные в Supabase, если подключение настроено
    if supabase:
        print("Отправка данных в таблицу Supabase...")
        try:
            # Превращаем данные в формат для нашей таблицы rates_history
            # (Здесь мы отправляем статус или актуальные ставки)
            record = {
                "bank_name": "VoleFramvi Bot",
                "rate_value": 0.0, # Сюда позже можно подставить реальное числовое значение ставки
                "updated_at": "2026-10-29T12:19:00Z" # Или использовать актуальное время
            }
            response = supabase.table("rates_history").insert(record).execute()
            print(f"Успешно записано в Supabase: {response}")
        except Exception as e:
            print(f"Ошибка при отправке в Supabase: {e}")
    else:
        print("Предупреждение: Ключи Supabase не найдены, данные отправлены только локально.")

if name == "main":
    update_rates()
