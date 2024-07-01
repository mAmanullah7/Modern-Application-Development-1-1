# # formatatting printing using f string
Name = "Amanullah"
place = "Muzaffarpur"
# profession = "Software Development Engineer"

# text = f"My name is {Name}, I live in {place}, and i am {profession}."

# # print(text)

# # now we'll do this using jinjaa2

# from jinja2 import Template

# Name = "Divya"
# place = "Muzaffarpur"
# profession = "Software Development Engineer"


# # Step1 = text
# # step2 = Template
# # step3= render it info

# temp = "My name is {{name}}, i live in {{place}}"

# made_template = Template(temp)

# out = made_template.render(name=Name, place=place)
# # print(out)

# out = made_template.render(name="Aman", place="Bihar")
# # print(out)


# Working on some html data

# from jinja2 import Template

# Name = "Aman"
# Place = "Bihar"

# # Step1

# Temp = """

#             <!DOCTYPE html>
#             <html lang="en">
#             <head>
#                 <meta charset="UTF-8">
#                 <meta name="viewport" content="width=device-width, initial-scale=1.0">
#                 <title>Document</title>
#             </head>
#             <body>
#                 <h2>My name is {{name}}</h2>
#                 <h2>i live in {{place}}</h2>
#             </body>
#             </html>


#      """

# # step2

# made_temp = Template(Temp)

# # step 3
# out = made_temp.render(name=Name, place = Place)
# print(out)


# For in jinjaa2

from jinja2 import Template

Data = ["Programmer", "DSA", "Developer"]

# temp = """

#                 <!DOCTYPE html>
#             <html lang="en">

#             <head>
#                 <meta charset="UTF-8">
#                 <meta name="viewport" content="width=device-width, initial-scale=1.0">
#                 <title>Document</title>
#             </head>

#             <body>
#                 <h2>My name is {{name}} </h2>
#                 <h2>i live in {{place}}</h2>

#                 <p>{% for i in data %}
#                     {{i}}
#                     {% endfor %}
#                 </p>
                
#             </body>

#             </html>
# """

temp = "{% for i in data%} {{i}} {% endfor %}"

made_temp = Template(temp)

out = made_temp.render(data=Data)  #left hand data is the variable use in temp and right side is Actual Data located

print(out)