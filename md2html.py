import markdown

markdown_string = ""
with open('GMSrm.md', 'r') as file:
    markdown_string = file.read()


# Convert markdown to HTML

head = '''

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Great Myriad Scale</title>
    <style>
    body {background-color: lightgrey;
     font-family: Tahoma, sans-serif;
}
    h1   {color: black;}
    p    {color: black;}

    table, th, td {
  border: 1px solid;
  padding: 5px;
}
    </style>
</head>
<body>

'''
html_string = markdown.markdown(markdown_string, extensions=['tables'])

with open('index.html', 'w') as f:
    f.write(head + html_string + "\n</body>\n</html>")

