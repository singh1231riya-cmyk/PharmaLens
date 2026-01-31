import matplotlib.pyplot as plt
from .drugs import Drug
from .data_handler import load_from_csv, save_to_csv


class PharmaManager:
    def __init__(self, csv_file="pharma_data.csv"):
        self.csv_file = csv_file
        self.medicines = load_from_csv(csv_file)

    # ================= ADD =================
    def add_medicine(self):
        print("\n--- Add Medicine ---")
        name = input("Name: ")
        category = input("Category: ")
        manufacturer = input("Manufacturer: ")
        price = float(input("Price: "))
        stock = int(input("Stock: "))
        sales = input("Monthly sales (comma separated): ")
        monthly_sales = [int(x.strip()) for x in sales.split(",")]
        adverse = int(input("Adverse events: "))

        drug = Drug(
            name, category, manufacturer, price, stock, monthly_sales, adverse
        )
        self.medicines.append(drug)
        print("Medicine added successfully")

    # ================= VIEW =================
    def view_medicines(self):
        if not self.medicines:
            print("No medicines available")
            return

        print("\n--- Medicine List ---")
        for i, d in enumerate(self.medicines, 1):
            print(
                f"{i}. {d.name} | {d.category} | {d.manufacturer} | "
                f"Price: {d.price} | Stock: {d.stock} | "
                f"Sales: {d.monthly_sales}"
            )

    # ================= UPDATE =================
    def update_medicine(self):
        self.view_medicines()
        if not self.medicines:
            return

        idx = int(input("Enter medicine number to update: ")) - 1
        d = self.medicines[idx]

        d.name = input(f"Name ({d.name}): ") or d.name
        d.category = input(f"Category ({d.category}): ") or d.category
        d.manufacturer = input(f"Manufacturer ({d.manufacturer}): ") or d.manufacturer

        price = input(f"Price ({d.price}): ")
        if price:
            d.price = float(price)

        stock = input(f"Stock ({d.stock}): ")
        if stock:
            d.stock = int(stock)

        sales = input(f"Monthly sales ({d.monthly_sales}): ")
        if sales:
            d.monthly_sales = [int(x.strip()) for x in sales.split(",")]

        print("Medicine updated")

    # ================= REMOVE =================
    def remove_medicine(self):
        self.view_medicines()
        if not self.medicines:
            return

        idx = int(input("Enter medicine number to remove: ")) - 1
        removed = self.medicines.pop(idx)
        print(f"{removed.name} removed")

    # ================= GRAPHS =================
    def plot_stock_bar(self):
        names = [d.name for d in self.medicines]
        stocks = [d.stock for d in self.medicines]

        plt.bar(names, stocks)
        plt.title("Medicine Stock Levels")
        plt.xlabel("Medicine")
        plt.ylabel("Stock")
        plt.xticks(rotation=45)
        plt.show()

    def plot_sales_line(self):
        for d in self.medicines:
            plt.plot(d.monthly_sales, label=d.name)

        plt.title("Monthly Sales Trend")
        plt.xlabel("Month")
        plt.ylabel("Units Sold")
        plt.legend()
        plt.show()

    # ================= SAVE =================
    def save_data(self):
        save_to_csv(self.csv_file, self.medicines)
