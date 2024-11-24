import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

path = "height_weight.csv"
df = pd.read_csv(path)

height = df['Рост(см.)'].to_numpy()
weight = df['Вес(кг.)'].to_numpy()
int_height = height.astype(int)
int_weight = weight.astype(int)

print("Колонки:", df.columns)
print(df)

print("\nСтатистика роста:")
print("Средний рост:", np.mean(int_height))
print("Медианный рост:", np.median(int_height))

print("\nСтатистика веса:")
print("Средний вес:", np.mean(int_weight))
print("Медианный вес:", np.median(int_weight))

plt.figure(figsize=(8, 6))
plt.hist(df['Рост(см.)'], bins=20, color='green', edgecolor='black', alpha=0.7)
plt.title('Распределение роста', fontsize=14)
plt.xlabel('Рост (см)', fontsize=12)
plt.ylabel('Частота', fontsize=12)
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 6))
plt.scatter(df['Рост(см.)'], df['Вес(кг.)'], alpha=0.7, color='blue')
plt.title('Зависимость веса от роста', fontsize=14)
plt.xlabel('Рост (см)', fontsize=12)
plt.ylabel('Вес (кг)', fontsize=12)
plt.grid(True)
plt.show()