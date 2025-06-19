"""
Модуль для предварительной очистки и анализа табелей, полученных в Excel.
Цель — выявление типовых ошибок и отклонений ещё до загрузки в 1С.
"""

import pandas as pd

# Класс, обрабатывающий один файл табеля
class TabelCleaner:
    def __init__(self, filepath):
        self.filepath = filepath
        self.df = pd.read_excel(filepath)

def clean(self):
    # Удаляем полностью пустые строки (где вообще нет данных в строке)
    self.df.dropna(how='all', inplace=True)

    # Удаляем строки, где нет значений в первом столбце (например, нет ФИО или табельного номера)
    self.df.dropna(subset=[self.df.columns[0]], inplace=True)

    # Очищаем все ячейки от лишних пробелов в начале и в конце (если это строка)
    # Например, "  Я11 " -> "Я11"
    self.df = self.df.applymap(
        lambda x: x.strip() if isinstance(x, str) else x
    )

    # Печатаем в консоль сообщение — чтобы понимать, что метод отработал
    print("Очистка завершена.")

    def detect_anomalies(self):
        # TODO: реализовать выявление отклонений (например, короткие смены, Я11 вместо ВМ11 и пр.)
        pass

    def export_result(self, output_path):
        # TODO: сохранить очищенный файл или отчёт
        pass
