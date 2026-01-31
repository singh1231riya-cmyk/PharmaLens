import csv
from .drugs import Drug


def load_from_csv(file_path):
    medicines = []

    try:
        with open(file_path, newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                monthly_sales = [
                    int(x.strip()) for x in row["Monthly_Sales"].split(",")
                ]

                drug = Drug(
                    name=row["Drug_Name"],
                    category=row["Category"],
                    manufacturer=row["Manufacturer"],
                    price=float(row["Price"]),
                    stock=0,
                    monthly_sales=monthly_sales,
                    adverse_events=int(row["Adverse_Events"]),
                )
                medicines.append(drug)
    except FileNotFoundError:
        print("CSV file not found. Starting with empty data.")

    return medicines


def save_to_csv(file_path, medicines):
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Drug_Name",
            "Category",
            "Manufacturer",
            "Monthly_Sales",
            "Price",
            "Adverse_Events"
        ])

        for d in medicines:
            writer.writerow([
                d.name,
                d.category,
                d.manufacturer,
                ", ".join(map(str, d.monthly_sales)),
                d.price,
                d.adverse_events
            ])