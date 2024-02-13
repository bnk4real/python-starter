# Create a basic HTML page
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

    <h1>This is HTML by Python</h1>
    <p>This is a simple HTML page generated using Python.</p>
    
</body>
</html>
"""

# Write the HTML content to a file
with open("index.html", "w") as file:
    file.write(html_content)
    print("Create success.")