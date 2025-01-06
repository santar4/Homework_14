# Email_Message API

Цей проєкт реалізує простий API для відправки електронних листів і логування дій користувачів за допомогою FastAPI. API підтримує фонові завдання для ефективної обробки електронних листів та управління логами.

## Можливості

- **Відправка листів**: Надсилання електронних листів на вказані адреси.

- **Логування дій користувачів:** Збереження всіх дій користувачів у окремий файл.

- **Отримання логів**: Доступ до журналів дій користувачів для моніторингу та налагодження.
- 
- **Щоб отримати повідомлення**: Зайдіть та зареєйструйтесь на сайті https://mailmug.net/, потім перейдіть у вкладку "Inboxes", виберіть Inbox або створіть новий і перейдіть у вкладку settings(Credentials)
## Вимоги

- Python
- FastAPI
- Uvicorn
- smtplib
- Pydantic

## Встановлення
1. **Клонуйте репозиторій**:



    ```bash
    git clone https://github.com/santar4/Homework_14

    ```

2. **Встановіть залежності**:



    ```bash
    pip install -r requirements.txt
    ```

3. **Створіть файл .env у кореневій директорії з наступною конфігурацією SMTP **:
   ```bash
   SMTP_SERVER=smtp.mailmug.net
   SMTP_PORT=2525
   SMTP_LOGIN=your_mailmug_username
   SMTP_PASSWORD=your_mailmug_password
   SMTP_SENDER=your_email_adress  (** write your email adress)
    ```
4. **Запустіть сервер**:

    Запустіть сервер за допомогою Uvicorn:

    ```bash
    uvicorn main:app --reload
    ```