
from jinja2 import Template


Products = [
    {'product_id':'101', 'prod_name':'Legion','type':'Laptop','Producer':'Lenevo'},
    {'product_id':'102', 'prod_name':'S21PRO','type':'Cellphone','Producer':'Samsung'},
    {'product_id':'103', 'prod_name':'iphone13','type':'cellphone','Producer':'Apple'},
    {'product_id':'104', 'prod_name':'TabA7','type':'TABLET','Producer':'Samsung'},
    {'product_id':'105', 'prod_name':'iPad','type':'TABLET','Producer':'Apple'},
    {'product_id':'106', 'prod_name':'Ideapad','type':'Tablet','Producer':'Lenevo'},
    {'product_id':'107', 'prod_name':'NoteA7','type':'Cellphone','Producer':'Xiomi'},
    {'product_id':'108', 'prod_name':'Tab4','type':'TABLET','Producer':'Lenevo'},
    {'product_id':'109', 'prod_name':'Macbook','type':'Laptop','Producer':'Apple'},
    {'product_id':'110', 'prod_name':'miNotebook','type':'Laptop','Producer':'Xiomi'},
    {'product_id':'111', 'prod_name':'M21','type':'Laptop','Producer':'Samsung'},
    {'product_id':'112', 'prod_name':'A7000','type':'Laptop','Producer':'Lenevo'}
]


# step 1

File = open('mad1/Week3_jinjaa2/product.html', 'r')

temp = File.read()
File.close()


# step2 
made_temp =  Template(temp)

# step3

output = made_temp.render(Products=Products)
# print(output)

File = open('output.html', 'w')
File.write(output)
File.close()
