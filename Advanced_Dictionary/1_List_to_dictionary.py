product_information = [("Desktop", "Electronics", 500),
                       ("Laptop", "Electronics", 100), ("Worker","People",20)]

print(f"Product info: {product_information}")

product_dict = {}
for product_name, product_cat, product_item in product_information:
    print("Before Dictionary Creating")
    print(f"name: {product_name}, category: {product_cat}, item: {product_item}")
    if product_cat not in product_dict:
        product_dict[product_cat] = {}
    product_dict[product_cat][product_name] = product_item

print("-------------------------------")
print("After Dictionary Creating")
print(f"Created Dictionary: {product_dict}")
print(product_dict["Desktop"])

"""product_dict["Electronics"]["Desktop"] = 500
will make
"Electronics": {
        "Desktop": 500
    }
A nested Dictionary
"""