# Quality Demo - Автоматизация контроля качества ПО

[![Quality Pipeline](https://github.com/Angeldroid122/quality-demo/actions/workflows/quality.yml/badge.svg)](https://github.com/Angeldroid122/quality-demo/actions/workflows/quality.yml)

## 📊 Результаты проверки качества

| Проверка | Результат |
|----------|-----------|
| ✅ Модульные тесты | 5 passed |
| ✅ Покрытие кода | 92% (≥70%) |
| ✅ Линтер (pylint) | 10.00/10 |
| ✅ Безопасность (bandit) | No issues |

## 🚀 Запуск локально

```bash
# Установка зависимостей
pip install pylint pytest pytest-cov bandit

# Запуск тестов
pytest tests/ -v

# Проверка покрытия
pytest tests/ --cov=src

# Проверка линтером
pylint src/

# Проверка безопасности
bandit -r src/