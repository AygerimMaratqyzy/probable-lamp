import re
import json

def all_price(price_str):
    """
    Convert prices like '1 200,00' to float 1200.00
    """
    price_str = price_str.replace(" ", "").replace(",",".")
    return float(price_str)

def parse_receipt(text):
    data = {}
    # 1.Extract all prices
    price_pattern = r"\b\d{1,3}(?: \d{3})*,\d{2}\b"
    raw_prices = re.findall(price_pattern, text)
    prices = [all_price(p) for p in raw_prices]
    data["all_prices"] = prices

    # 2.Extract product names
    product_pattern = r"\d+\.\s*\n(.+)"
    products = re.findall(product_pattern,text)
    data["products"] = [p.strip() for p in products]

    # 3.Extract total amount
    total_pattern = r"ИТОГО:\s*\n?(\d{1,3}(?: \d{3})*,\d{2})"
    total_match = re.search(total_pattern, text)
    if total_match:
        data["total"] = all_price(total_match.group(1))
    else:
        data["total"] = None

    # 4. Extract date and time
    datetime_pattern = r"Время:\s*(\d{2}\.\d{2}\.\d{4})\s*(\d{2}:\d{2}:\d{2})"
    datetime_match = re.search(datetime_pattern,text)
    if datetime_match:
        data["date"] = datetime_match.group(1)
        data["time"] = datetime_match.group(2)
    else:
        data["date"] = None
        data["time"] = None
    
    # 5.Extraxt payment method
    payment_pattern = r"(Банковская карта)"
    payment_match = re.search(payment_pattern,text)
    if payment_match:
        data["payment_method"] = payment_match.group(1)
    else:
        data["payment_method"] = None
    
    # 6.Calculate total from products (optional validation)
    item_total_pattern = r"\n(\d{1,3}(?: \d{3})*,\d{2})\nСтоимость"
    item_totals = re.findall(item_total_pattern, text)
    item_totals_clean =[all_price(p) for p in item_totals]
    data["calculated_total"] = sum(item_totals_clean)

    return data

if __name__ == "__main__":
    with open("raw.txt","r", encoding="utf-8") as f:
        receipt_text = f.read()

    parsed_data = parse_receipt(receipt_text)

    print(json.dumps(parsed_data, indent=4, ensure_ascii=False))