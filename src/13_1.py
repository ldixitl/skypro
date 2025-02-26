import csv
import json

import pandas as pd

# with open("Книга1.csv") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

# rows = [
# ['Name', 'Age', 'Gender'],
# ['Kolya', '35', 'male'],
# ['Masha', '33', 'female'],
# ['Petya', '25', 'male']
# ]
#
# with open('write.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(rows)

# with open("Книга1.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row['Name'], row['Age'], row['Gender'])
#
# rows = [{'Name': 'Alice', 'Age': '25', 'Gender': 'Female'},
#         {'Name': 'Bob', 'Age': '30', 'Gender': 'Male'},
#         {'Name': 'Charlie', 'Age': '35', 'Gender': 'Male'}]
#
# with open('write.csv', 'w', newline='') as file:
#     fieldnames = ['Name', 'Age', 'Gender']
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#     writer.writeheader()
#     for row in rows:
#         writer.writerow(row)

# with open('../data/students.csv') as file:
#     reader = csv.reader(file)
#     next(reader)
#     for row in reader:
#         if float(row[2]) > 4.5:
#             print(row)

#
# with open('../data/students.csv') as file:
#     reader = csv.DictReader(file)
#
#     for row in reader:
#         if float(row['avg_grade']) > 4.5:
#             print(f"Средний балл студента {row['name']} ({row['age']} лет) - {row['avg_grade']}")

# df = pd.DataFrame({'Yes': [50, 21], 'No': [131, 2], '50/50': [20, 39]})
# print(df)
# s = pd.Series([1, 2, 3, 4, 5])
# print(s)

wine_reviews = pd.read_csv("../data/winemag-data-130k-v2.csv")

# country_wine = wine_reviews.groupby('country')
# print(country_wine.price.mean())
#
# wine_reviews.sort_values(by='price', inplace=True, ascending=False)
# print(wine_reviews.head().price)

# sorted_by_price_and_country = wine_reviews.groupby("country").apply(
#     lambda x: x.sort_values(by="price", ascending=False)
# )
# print(sorted_by_price_and_country.price)

# expensive_wines = wine_reviews[wine_reviews['price'] > 100]
# expensive_wines = wine_reviews.query('price > 100')
# print(expensive_wines)


# italian_wines = wine_reviews[wine_reviews['country'] == 'Italy']
#
# expensive_italian_wines = italian_wines[italian_wines['price'] > 100]
# print(expensive_italian_wines.price)

# for index, row in wine_reviews.iterrows():
#     print(f'Index: {index}, Country: {row["country"]}, Price: {row["price"]}')
#
# for column_name, column_data in wine_reviews.items():
#     print(f"Column: {column_name}, Data: {column_data.tolist()}")

# new_df = wine_reviews.groupby("country").agg({
#     'price': 'mean',
#     'points': 'mean'
# })
#
# print(new_df)

# italy_reviews = wine_reviews.loc[(wine_reviews.country == "Italy") & (wine_reviews.points >= 90)]
# italy_or_france = wine_reviews.loc[wine_reviews.country.isin(["Italy", "France"])]
# not_null = wine_reviews.loc[wine_reviews.price.notnull()]
# complex_reviews = wine_reviews.loc[
#     ((wine_reviews.country == "Italy") | (wine_reviews.points >= 90)) &
#     (wine_reviews.price.notnull())
# ]
# wine_reviews["critic"] = "everyone"
# wine_reviews["index_backwards"] = range(len(wine_reviews), 0, -1)
# print(wine_reviews.points.describe())
# print(wine_reviews.taster_name.describe())
# print(wine_reviews.points.mean())
# print(wine_reviews.taster_name.unique())
# print(wine_reviews.taster_name.value_counts())
# review_points_mean = wine_reviews.points.mean()
# wine_reviews.points = wine_reviews.points.map(lambda p: round((p - review_points_mean), 2))
# print(wine_reviews.loc[[1, 9, 130, 739], "points"])
#
# wine_reviews["description_lenght"] = wine_reviews.description.map(len)
# # print(wine_reviews.loc[[1, 9, 130, 739], "description_lenght"])
# print(wine_reviews.description_lenght.describe())

# def calc_avg(points):
#     return sum(points) / len(points)
#
#
# print(wine_reviews.points.apply(lambda x: calc_avg([x])))

# df = wine_reviews
# print(df.iloc[2:5, 1:5])
# print(df.loc[[1, 3, 5], ['country', 'price', 'taster_name']])
# print(wine_reviews.shape)
# print(wine_reviews.head(3))

# df = pd.DataFrame({'Yes': [130, 50, 25], "No": [50, 56, 100]})
# print(df)

# df = pd.read_excel("../data/winemag-data-130k-v2.xlsx")

# df.set_index("title", inplace=True, drop=False)
#
# print(df.iloc[0])
# print(df.loc['Nicosia 2013 Vulkà Bianco  (Etna)'])

#
# print(df.head(2))
#
# df_index = pd.read_excel("../data/winemag-data-130k-v2.xlsx", index_col=0)
#
# print(df_index.head(2))

# df = pd.DataFrame({
#     'Bob': ['Мне это понравилось.', 'Это было ужасно.', 'Мне это понравилось.'],
#     'Sue': ['Довольно хорошо.', 'Без вкуса.', 'Мне это понравилось.']
# }, index=['Товар A', 'Товар B', 3])
# print(df)

# data = {
#     'student_id': ['001', '002', '003'],
#     'name': ['Alice', 'Bob', 'Charlie'],
#     'grade': [87, 92, 78]
# }
#
# df = pd.DataFrame(data)
#
# # Установить 'student_id' в качестве индекса
# df.set_index('student_id', inplace=True)
#
# # Легкий доступ к данным конкретного студента
# print(df.loc[['001', '002']])

# df = pd.DataFrame({
#     'A': [1, 2, 3],
#     'B': [4, 5, 6],
#     'C': [7, 8, 9]
# })
#
# # result = df.apply(pd.Series.mean)
# result = df.sum(axis=1)
# print(result)

# # Создаем DataFrame
# df = pd.DataFrame({
#     'A': [1, 2, 3],
#     'B': [4, 5, 6],
#     'C': [7, 8, 9]
# })
#
# # Функция, которую мы хотим применить
# def multiply_by_two(column):
#     return column * 2
#
# # Применяем функцию к каждому столбцу
# df_applied = df.apply(multiply_by_two, axis=0)
# print(df_applied)
#
# # Функция, которую мы хотим применить
# def sum_row(row):
#     return row.sum()
#
# df_applied_sum = df.apply(sum_row, axis=1)
# print(df_applied_sum)
# df_applied_sum = df.apply(sum_row, axis=0)
# print(df_applied_sum)

# df = pd.DataFrame({
#     'country': ['France', 'Italy', 'Spain', 'France', 'Italy', 'Spain'],
#     'price': [20, 15, 30, 22, 18, 25]
# })
#
# # Группировка данных по странам
# country_grouped = df.groupby('country')
#
# # Вычисление средней цены для каждой страны
# mean_price_by_country = country_grouped['price'].mean()
# print(mean_price_by_country)

# data = {
#     'country': ['France', 'Italy', 'Spain', 'France', 'Italy', 'Spain'],
#     'price': [20, 15, 30, 22, 18, 25]
# }
#
# df = pd.DataFrame(data)
#
# # Сортировка по столбцу 'price' в порядке возрастания
# sorted_by_price = df.sort_values(by='price', ignore_index=True)
# print(sorted_by_price)

# data = {
#     'country': ['France', 'Italy', 'Spain', 'France', 'Italy', 'Spain'],
#     'region': ['Bordeaux', 'Tuscany', 'Rioja', 'Bordeaux', 'Sicily', 'Rioja'],
#     'price': [20, 15, 30, 22, 18, 31]
# }
#
# df = pd.DataFrame(data)
#
# # Сортировка по столбцам 'country' и 'price'
# sorted_by_country_price = df.sort_values(by=['country', 'price'])
# print(sorted_by_country_price)

# data = {
#     'country': ['France', 'Italy', 'Spain', 'France', 'Italy', 'Spain', None],
#     'price': [20, 15, 30, 22, 18, 25, 17]
# }
#
# df = pd.DataFrame(data)
#
# # Сортировка по столбцу 'country' с размещением NaN в начале
# sorted_with_nan_first = df.sort_values(by='country', na_position='last')
# print(sorted_with_nan_first)

# data = {
#     'country': ['FRANCE', 'italy', 'Spain', 'france', 'ITALY', 'spain'],
#     'price': [20, 15, 30, 22, 18, 25]
# }
#
# df = pd.DataFrame(data)

# # Сортировка по столбцу 'country' с использованием лямбда-функции
# sorted_case_insensitive = df.sort_values(by='country', key=lambda x: x.str.lower())
# print(sorted_case_insensitive)

# data = {
#     'country': ['France', 'Italy', 'Spain', 'France', 'Italy', 'Spain'],
#     'price': [20, 15, 30, 22, 18, 25]
# }
#
# df = pd.DataFrame(data)
# # Группировка данных по странам и сортировка по цене внутри каждой группы
# sorted_by_price_and_country = df.groupby('country').apply(lambda x: x.sort_values('price', ascending=False))
# print(sorted_by_price_and_country.head())

titanic_passengers = pd.read_csv("../data/titanic.csv")

# gender_of_passengers = titanic_passengers.groupby("Sex").agg({
#     "Age": "mean"
# })
# print(gender_of_passengers.to_json(orient='records'))

# def average_age_by_gender(dataframe):
#     average_age_male = dataframe[dataframe['Sex'] == 'male'].Age.mean()
#     average_age_female = dataframe[dataframe['Sex'] == 'female'].Age.mean()
#     result = {'Male': average_age_male, 'Female': average_age_female}
#
#     return json.dumps(result)
#
# def filter_passengers(dataframe):
#     result = dataframe[((dataframe['Sex'] == 'male') & (dataframe['Age'] > 50)) |
#                        ((dataframe['Sex'] == 'female') & (dataframe['Age'] < 30))]
#     return result.to_json(orient='records')

# def avg_fare(dataframe):
#     class_passengers = dataframe.groupby("Pclass").Fare.mean()
#     return json.dumps(class_passengers.to_dict())


def get_survived(dataframe: pd.DataFrame) -> int:
    survived_df = dataframe[dataframe["Survived"] == 1]
    survived_df.to_json("../data/survived.json", indent=4, orient="records")
    return survived_df.count()


print(get_survived(titanic_passengers))
