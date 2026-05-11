import json

FILE_NAME = "products.json"

# قراءة المنتجات من ملف JSON
with open(FILE_NAME, "r") as file:
    products = json.load(file)

# عرض كل المنتجات
print("Available Products:")
print("-" * 30)

for product in products:
    print(f"ID: {product['id']}")
    print(f"Name: {product['name']}")
    print(f"Stock: {product['stock']}")
    print(f"Price: {product['price']} SAR")
    print("-" * 30)

# البحث عن منتج باستخدام ID
search_input = input("Enter the product ID to search: ")

if search_input.isdigit():
    search_id = int(search_input)

    for product in products:
        if product["id"] == search_id:
            print(f"Product found: {product['name']}, Price: {product['price']} SAR")
            break
    else:
        print("Product not found.")
else:
    print("Invalid ID. Please enter a number.")

# إضافة منتجات إلى السلة
cart = []

while True:
    product_input = input("Enter the product ID to add to cart (or 'done' to finish): ")

    if product_input.lower() == "done":
        break

    if not product_input.isdigit():
        print("Invalid input. Please enter a product ID number.")
        continue

    product_id = int(product_input)

    for product in products:
        if product["id"] == product_id:
            cart.append(product)
            print(f"Added {product['name']} to cart.")
            break
    else:
        print("Product not found.")

# عرض محتويات السلة
print("\nItems in your cart:")
print("-" * 30)

for item in cart:
    print(f"- {item['name']}: {item['price']} SAR")

# حساب السعر الإجمالي
total_price = sum(item["price"] for item in cart)

print("-" * 30)
print(f"Total price: {total_price} SAR")

# حفظ السلة في ملف JSON
with open("cart.json", "w") as cart_file:
    json.dump(cart, cart_file, indent=4)

print("Cart saved to cart.json")