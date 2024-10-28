product_dict = {
    "Electronics": {
        "Desktop": 500,
        "Laptop": 100
    },
    "People": {
        "Worker": 20
    }
}

for category, item in product_dict.items():
    print(f"Category: {category}")
    for item, value in  item.items():
        print(f"Item: {item} and price: {value}")