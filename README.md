≡ Краткое руководство 

# Описание проекта "API для Yatube"

Проект "API для Yatube" является небольшой социальной сетью. Пользователи могут писать посты, оставлять комментарии к постам других пользователей, а также подписываться/отписываться на них.

***

## Установка
Для работы проекта достаточно установить:
- [Python](https://www.python.org/)
- Любой текстовый редактор кода (опционально). Например, [Visual Studio Code](https://code.visualstudio.com/download)
- Если вы пользователь Windows, то нужно установить [Git](https://git-scm.com/)

#### Команда клонирования репозитория:
    git clone https://github.com/phpstal/api_final_yatube

### Подготовка проекта
В консоле переходите в папку с проектом. Далее нужно:  
- активировать виртуальное окружение:

    source /venv/script/activate - для Windows
    source . /venv/bin/activate - для Linux

- установить необходимые компоненты для работы проекта:

    pip install -r requirements.txt

Затем нужно сделать миграции:

    python manage.py migrate

После этого, когда все будет установлено, запустите сервер командой:

    python manage.py runserver

Всё! Ваш сервер запущен и по адресу **http://127.0.0.1:8000** вам будет достна главная страница проекта.
Если хотите сервер остановить, то просто нажмите сочетание клавиш `Ctrl` + `C`
***

### Создание суперпользователя

Для администрирования вашего проекта, созданию дополнительных категорий, жанров и т.д. Нужно создать суперпользователя:

    python manage.py createsuperuser

Далее указываете имя пользователя, потом пишите его e-mail, два раза пароль. И вуаля, суперюзер создан!
***

### Информация про технологии в этом проекте
Тут, собственно, все по классике. Вот такие технологии использовались:
- python - язык программирования, на нем написан фрейморк Django
- django - фрейморк, на основе которого создан проект
- github - чтобы работать с кодом в разных частях света, причем не один, а целой командой.


### Автор проекта
Автор проекта - Владимир. Студент онлайн-школы Яндекс.Практикум. Студент курса Python-разработчик.