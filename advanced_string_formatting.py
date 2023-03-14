#!/usr/bin/env python3

def main():
    # data
    cars = [
        ['Toyota', 'Corolla', 2022, 22900],
        ['Honda', 'Civic', 2022, 21950],
        ['Ford', 'Mustang', 2022, 28200],
        ['Tesla', 'Model 3', 2022, 39890],
    ]

    row = "| {make:<10s} | {model:<10s} | {year:<10s} | {price:<10s} |".format

    # print header row
    print("-" * 47)
    print(row(make="Make", model="Model", year="Year", price="Price"))
    print("-" * 47)

    # print data rows
    for car in cars:
        print(row(make=car[0], model=car[1], year=str(car[2]), price=str(car[3])))

    print("-" * 47)

if __name__ == "__main__":
    main()
