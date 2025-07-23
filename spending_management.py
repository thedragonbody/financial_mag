def load_expenses(filename):
    expenses = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(' - ')
                if len(parts) == 2:
                    amount, desc = parts
                    expenses.append((int(amount), desc))
    except FileNotFoundError:
        pass 
    return expenses

def save_expense(filename, amount, desc):
    with open(filename, 'a') as file:
        file.write(f"{amount} - {desc}\n")

def show_expenses(expenses):
    if not expenses:
        print("هنوز هزینه‌ای ثبت نشده.")
        return
    total = 0
    print("\n📋 لیست هزینه‌ها:")
    for amount, desc in expenses:
        print(f"{amount} تومان - {desc}")
        total += amount
    print(f"\n💰 مجموع کل هزینه‌ها: {total} تومان\n")

def main():
    filename = "expenses.txt"
    expenses = load_expenses(filename)

    while True:
        print("\n📌 منو:")
        print("1. افزودن هزینه جدید")
        print("2. نمایش همه هزینه‌ها")
        print("3. خروج")

        choice = input("انتخاب شما: ")

        if choice == "1":
            try:
                amount = int(input("مبلغ هزینه (تومان): "))
                desc = input("توضیح هزینه: ")
                expenses.append((amount, desc))
                save_expense(filename, amount, desc)
                print("✅ هزینه با موفقیت ثبت شد.")
            except ValueError:
                print("❌ لطفاً یک عدد معتبر وارد کنید.")
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "3":
            print("👋 خداحافظ!")
            break
        else:
            print("❌ گزینه نامعتبر است.")

if __name__ == "__main__":
    main()