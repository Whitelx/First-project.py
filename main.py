import json

FILE_NAME = "products.json"

# نفتح ملف JSON ونقرأ البيانات
with open(FILE_NAME, "r") as file:
    products = json.load(file)

