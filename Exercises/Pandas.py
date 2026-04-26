import pandas as pd
#
#   1. From the given dataset print the first and last five rows
#
df = pd.read_csv("Automobile_data.csv")

print(df.head(5))
print(df.tail(5))

#
#   2. Clean the dataset and update the CSV file
#
df = pd.read_csv("Automobile_data.csv", na_values={
    'price':["?","n.a"],
    'stroke':["?","n.a"],
    'horsepower':["?","n.a"],
    'peak-rpm':["?","n.a"],
    'average-mileage':["?","n.a"]})

print(df)

df.to_csv("Automobile_data.csv")

#
#   3. Find the most expensive car company name
#
df = pd.read_csv("Automobile_data.csv")

df = df[['company', 'price']][df.price==df['price'].max()]

print(df)

#
#   4. Print All Toyota Cars details
#
df = pd.read_csv("Automobile_data.csv")

car_manufacturer = df.groupby('company')
toyota = car_manufacturer.get_group('toyota')

print(toyota)

#
#   5. Count total cars per company
#
df = pd.read_csv("Automobile_data.csv")

total_cars = df['company'].value_counts()

print(total_cars)

#
#   6. Find each company’s Higesht price car
#
df = pd.read_csv("Automobile_data.csv")

df = df.groupby('company')['price'].max()

print(df)

#
#   7. Find the average mileage of each car making company
#
df = pd.read_csv("Automobile_data.csv")

df = df.groupby('company')['average-mileage'].mean()

print(df)

#
#   8. Sort all cars by Price column
#
df = pd.read_csv("Automobile_data.csv")

df = df.sort_values(by=['price'], ascending=False)

print(df)

#
#   9. Concatenate two data frames using the following conditions
#
GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
car1 = pd.DataFrame.from_dict(GermanCars)

japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}
car2 = pd.DataFrame.from_dict(japaneseCars)

cars = pd.concat([car1, car2], keys=["Germany", "Japan"])

print(cars)

#
#   10. Merge two data frames using the following condition
#
Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
car1 = pd.DataFrame.from_dict(Car_Price)

car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]}
car2 = pd.DataFrame.from_dict(car_Horsepower)

cars = pd.merge(car1, car2, on="Company")

print(cars)