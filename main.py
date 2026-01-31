from pharmalens.pharma_analysis import PharmaManager

def main():
    manager = PharmaManager()

    while True:
        print("\n------ Pharma Management System ------")
        print("1. Add Medicine")
        print("2. View Medicines")
        print("3. Update Medicine")
        print("4. Remove Medicine")
        print("5. Show Stock Bar Graph")
        print("6. Show Sales Line Graph")
        print("7. Save & Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            manager.add_medicine()
        elif choice == "2":
            manager.view_medicines()
        elif choice == "3":
            manager.update_medicine()
        elif choice == "4":
            manager.remove_medicine()
        elif choice == "5":
            manager.plot_stock_bar()
        elif choice == "6":
            manager.plot_sales_line()
        elif choice == "7":
            manager.save_data()
            print("Data saved. Exiting system.")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()