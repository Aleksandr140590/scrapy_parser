# Проект парсинга pep

### 1. Описание проекта

Парсер информации с сайта:
1. https://peps.python.org/

### 2. Подготовка проекта

Для начала работы с проектом необходимо его склонировать командой:
```
git clone git@github.com:Aleksandr140590/scrapy_parser_pep.git
```
или
```
git clone https://github.com/Aleksandr140590/scrapy_parser_pep.git
```
Следующим шагом будет установка виртуального окружения
```
python3 -m venv venv
```
активация виртуального окружение
```
source venv/bin/activate
```
и установка зависимостей
```
pip install -r requirements.txt
```

### 3. Запуск парсера

Для запуска необходимо запустить паука
```
scrapy crawl pep
```

Данная команда запустит "паука" рер и сохранит результаты в папке results в формате CSV

### Автор

<a href='https://github.com/Aleksandr140590/'>Федорович Александр</a>

