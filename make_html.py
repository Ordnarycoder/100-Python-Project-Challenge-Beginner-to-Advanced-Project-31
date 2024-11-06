import pandas as pd

df = pd.read_excel("products.xlsx")

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product List</title>
    <style>
        body { font-family: Arial, sans-serif; }
        .product { border: 1px solid #ddd; padding: 15px; margin: 10px; width: 250px; float: left; }
        .product img { width: 100%; height: auto; }
        .product h3 { font-size: 18px; margin: 5px 0; }
        .product .price { font-size: 16px; color: #28a745; font-weight: bold; }
        .product .battery-time, .product .review-count, .product .stars { margin-top: 5px; }
        .stars span { color: gold; }
        .container { display: flex; flex-wrap: wrap; }
    </style>
</head>
<body>
    <h1>Product List</h1>
    <div class="container">
"""

for _, row in df.iterrows():
    stars = ''.join(['<span>★</span>' for _ in range(int(row['star-count']))])  
    product_html = f"""
        <div class="product">
            <img src="{row['img-link']}" alt="{row['title']}">
            <h3>{row['title']}</h3>
            <p class="price">{row['price']}</p>
            <p class="battery-time">Battery: {row['battery-time']}</p>
            <p class="review-count">Reviews: {row['review-count']}</p>
            <p class="stars">Rating: {stars}</p>
        </div>
    """
    html_content += product_html

html_content += """
    </div>
</body>
</html>
"""

with open("products.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("HTML file created successfully!")
