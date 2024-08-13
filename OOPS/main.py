from OOPS.Item import Item
from OOPS.Phone import Phone


def main():
    # Instantiate items from CSV file
    Item.instantiate_from_csv("items.csv")

    # Display all items instantiated from the CSV
    for item in Item.store_list:
        print(item)

    # Create a Phone instance
    phone = Phone(
        name="iPhone 13",
        price=999.99,
        _quantity=5,
        _category="Electronics",
        _weight=0.5,
        _brand="Apple",
        broken_phones=1,
        year_of_manufacture=2021,
        usage_hours=50,
    )

    # Display the created Phone instance
    print(phone)

    # Apply discount to the phone
    phone.apply_discount()
    print(f"After discount: {phone}")

    # Calculate the total price of the phone
    total_price = phone.calculate_total_price()
    print(f"Total price: ${total_price:.2f}")

    # Update the battery life of the phone based on usage
    phone.update_battery_life()
    print(f"Updated battery life: {phone.battery_life}%")

    # Calculate the depreciation and resale value of the phone
    depreciation = phone.calculate_depreciation()
    resale_value = phone.calculate_resale_value()
    print(f"Depreciation: ${depreciation:.2f}")
    print(f"Resale value: ${resale_value:.2f}")

    # Check if the phone is outdated
    is_outdated = phone.is_outdated()
    print(f"Is the phone outdated? {'Yes' if is_outdated else 'No'}")

    # Send an email regarding the phone (simulated)
    phone.send_email()


if __name__ == "__main__":
    main()
