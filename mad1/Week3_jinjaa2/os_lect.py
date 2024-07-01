from jinja2 import Template

Name = "Aman"
Place = "Bihar"

# Step1

Temp = """

            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Document</title>
            </head>
            <body>
                <h2>My name is {{name}}</h2>
                <h2>i live in {{place}}</h2>
            </body>
            </html>


     """

# step2

made_temp = Template(Temp)

# step 3
out = made_temp.render(name=Name, place = Place)
print(out)


# # formatatting printing using f string
# Name = "Amanullah"
# place = "Muzaffarpur"
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

# from jinja2 import Template

# Data = ["Programmer", "DSA", "Developer"]

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

# temp = "{% for i in data%} {{i}} {% endfor %}"

# Sub = "Mad 1"

# temp = """
#             {% for i in data%}
#               {% if "D" in i %}
#                  {{i}}
#                {%endif%}
#             {%endfor%}

# """

# made_temp = Template(temp)

# out = made_temp.render(data=Data)  #left hand data is the variable use in temp and right side is Actual Data located

# print(out)

# from string import Template
# from jinja2 import Template

# temp = Template("Today is $today and tomorrow is $tomorrow") 
# #jinjaa --> {{}}, string --> $
# both Template()
# jinjaa --> render(), string --> substitue()
# jinjaa--> no values of variable->blank, string--> throws an error ---> use safe_substitute --> blank

# OUT = temp.substitute(today="Monday", tomorrow="Tuesday")
# print(OUT)

# t = Template("Numbers divisible by 2:{% for n in range(0,100,2)%} {{n}} {% endfor %}")
# print(t.render())