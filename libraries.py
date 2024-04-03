from rich.console import Console
from rich.table import Table
from faker import Faker
import plotly.graph_objs as go

def generate_fake_data(num_entries=10):
    fake = Faker()  # Создание объекта Faker
    data = []
    for _ in range(num_entries):
        name = fake.name()  # Генерация случайного имени
        email = fake.email()  # Генерация случайного адреса электронной почты
        phone = fake.phone_number()  # Генерация случайного номера телефона
        age = fake.random_int(min=18, max=90)  # Генерация случайного возраста
        data.append((name, email, phone, str(age)))  # Добавление кортежа в список данных
    return data

def display_table(data):
    console = Console()  # Создание объекта Console для вывода в консоль
    table = Table(title="Выборка людей, посещавших сайт последние 20 минут")  # Создание таблицы
    table.add_column("Имя")  # Добавление столбца
    table.add_column("Email")  # Добавление столбца
    table.add_column("Телефон")  # Добавление столбца
    table.add_column("Возраст")  # Добавление столбца

    for row in data:
        table.add_row(*row)  # Добавление строки в таблицу

    console.print(table)  # Вывод таблицы в консоль

def display_plot(data):
    ages = [entry[3] for entry in data]  # Создание списка возрастов из данных
    email_lengths = [len(entry[1]) for entry in data]  # Создание списка длин электронной почты из данных

    fig = go.Figure(data=go.Scatter(x=ages, y=email_lengths, mode='lines+markers'))  # Создание графика
    fig.update_layout(title="График зависимости Длинны почтового адресса от Возраста", xaxis_title="Возраст", yaxis_title="длинна Email")  # Обновление макета графика
    fig.show()  # Отображение графика

def main():
    fake_data = generate_fake_data(num_entries=5)  # Генерация фальшивых данных
    display_table(fake_data)  # Вывод таблицы фальшивых данных
    display_plot(fake_data)  # Построение графика

if __name__ == "__main__":
    main()
