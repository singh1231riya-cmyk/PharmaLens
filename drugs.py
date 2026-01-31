class Drug:
    def __init__(
        self,
        name,
        category,
        manufacturer,
        price,
        stock,
        monthly_sales,
        adverse_events=0
    ):
        self.name = name
        self.category = category
        self.manufacturer = manufacturer
        self.price = price
        self.stock = stock
        self.monthly_sales = monthly_sales
        self.adverse_events = adverse_events

    def total_sales(self):
        return sum(self.monthly_sales)

    def average_sales(self):
        if not self.monthly_sales:
            return 0
        return sum(self.monthly_sales) / len(self.monthly_sales)