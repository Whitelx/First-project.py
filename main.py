import json

FILE_NAME = "products.json"

# نفتح ملف JSON ونقرأ البيانات
with open(FILE_NAME, "r") as file:
    products = json.load(file)

# نطبع كل منتج في القائمة
for product in products:
    print(f"ID: {product['id']}")
    print(f"Name: {product['name']}")
    print(f"Price: {product['price']}")
    print("-" * 20)

# البحث عن منتج معين باستخدام ID
search_id = input("Enter the product ID to search: ")
for product in products:
    if product['id'] == search_id:
        print(f"Product found: {product['name']}, Price: {product['price']}")
        break
else:
    print("Product not found.")

#اضافه منتج الى السلة للشراء
cart = []
while True:
    product_id = input("Enter the product ID to add to cart (or 'done' to finish): ")
    if product_id.lower() == 'done':
        break
    for product in products:
        if product['id'] == product_id:
            cart.append(product)
            print(f"Added {product['name']} to cart.")
            break
    else:
        print("Product not found.")

# عرض محتويات السلة
print("\nItems in your cart:")
for item in cart:
    print(f"- {item['name']}: ${item['price']}")

# حساب إجمالي السعر
total_price = sum(item['price'] for item in cart)

print(f"Total price: ${total_price}")

# حفظ السلة في ملف JSON
with open("cart.json", "w") as cart_file:
    json.dump(cart, cart_file, indent=4)

print("Cart saved to cart.json")

# يمكنك الآن تشغيل هذا البرنامج وسيقوم بقراءة المنتجات من ملف JSON، والبحث عن المنتجات، وإضافة المنتجات إلى السلة، وعرض محتويات السلة، وحساب إجمالي السعر، وأخيرًا حفظ السلة في ملف JSON.