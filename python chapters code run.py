
# coding: utf-8

# In[3]:


#print statement
print("hello world" )
print("Drop shadow")


# In[12]:


#Variables for Strings
Name="kavish"
Fathername="Saeed"
print(Name,Fathername,floogle)
floogle="Mark"
name="Mark"



# In[15]:


lesson_author = "Mark"
guy_who_keeps_saying_his_own_name = "Mark"
x = "Mark"
print(lesson_author)


# In[18]:


print("Hello World!")
Thanx="Thanks for ur input!"
print(Thanx)


# In[30]:


#Variables for Numbers
original_num = 23
num_to_be_added = 7
new_num = original_num + num_to_be_added
print(new_num)



# In[31]:


original_num = 1.002
num_to_be_added = 0.0005
new_num = original_num + num_to_be_added
print(new_num)


# In[40]:


#Math expressions: Familiar operators
popular_num = 2
popular_um = 2+2
print(2+2)
lose=30-50
print("lose in ur bussiness",lose)
dozen=50/10
print(dozen)


# In[43]:


num = 10/30
another_num = 1.5
sum_of_numbers = num + another_num
print(sum_of_numbers)


# In[52]:


#Math expressions: Unfamiliar operators
whats_left_over = 10 % 3
print(whats_left_over)
age = 12
amount_to_increment = 3
age += amount_to_increment
print(age)
age = 12
age -= 2
print(age)


# In[56]:


#Math expressions: Eliminating ambiguity
total_cost = (1 + 3) * 4
print(total_cost)
result_of_computation = (2 * 4) * 4 + 2
print(result_of_computation)
result_of_computation = ((2 * 4) * 4) + 2
print(result_of_computation)
result_of_computation = (2 * 4) * (4 + 2)
print(result_of_computation)


# In[62]:


#Concatenating text strings
greeting = "wellcome to pakistan!"
addressee = "  pakistan Zindabad"
New_statement=greeting + addressee
print(New_statement)
greeting = "Pakistan"
separators = ", "
addressee = "Zindabad"
punc = "!"
whole_greeting = greeting + separators + addressee + punc
print(whole_greeting)
print(greeting + separators + addressee + punc)
print("The sum of 2 plus 2 is " + "4")


# In[72]:


#if statements
if number_of_husbands == 1:
print("So far so good.")
print("Congratulations.")
print("All done")


# In[76]:


#Comparison operators
if full_name == "Mark" + " " + "Myers":
if full_name == first_name + " " + "Myers":
if full_name == first_name + " " + last_name:
if total_cost == 81.50 + 135:
if total_cost == materials_cost + 135:
if total_cost == materials_cost + labor_cost:
if x + y == a - b:

if your_ticket_number != 487208:
    print("Better luck next time.",your_ticket_number)


# In[1]:


#else and elif statements
 if species == "cat"
    print("Yep, it's cat.")
else:
    print("Nope, not cat.")


# In[3]:


#Testing sets of conditions
if weight > 300 and time < 6:
status = "try to recruit him"
if weight > 300 and time < 6 and age > 17 and
height < 72:
status = "try to recruit him"
if SAT > avg or GPA > 2.5 or parent == "alum":
message = "Welcome to Leeds College!"

print()


# In[4]:


if (age > 65 or age < 21) and res == "U.K.":


# In[8]:


#if statements nested
if c == d:
    if x == y:
        g = h
    elif a == b:
        g = h
    else:
        e = f
    else:
        e = f
        print()


# In[15]:


#comment
if first_name == "Harry":
    if last_name == "Potter":
        if interest == "wizardry":
            print("Welcome back to Hogwarts, Harry!")
                


# In[16]:


print("Hello, world!") # Greet the world


# In[22]:


#Lists
city_0 = "Atlanta"
city_1 = "Baltimore"
city_2 = "Chicago"
city_3 = "Denver"
city_4 = "Los Angeles"
city_5 = "Seattle"
print("Welcome to " + city_3  + city_4)


# In[34]:


cities = ["Atlanta", "Baltimore", "Chicago",
"Denver", "Los Angeles", "Seattle"]
print("Welcome to " + cities[0]    + cities[5])


# In[39]:


#Lists: Adding and changing elements
cities = ["Atlanta", "Baltimore", "Chicago",
"Denver", "Los Angeles", "Seattle"]
cities.append("New York")
scores.append(47)
cities = cities + ["Dubuque", "New Orleans"]
longer_list_of_cities = cities + ["Dubuque", "New
Orleans"]
todays_tasks = []
todays_tasks = todays_tasks + ["Walk dog", "Buy
groceries"]
cities[0] is "Atlanta"
cities[1] is "Baltimore"
cities[2] is "Chicago"
cities[3] is "Denver"
cities[4] is "Los Angeles"
cities[5] is "Seattle
cities.insert(0, "New York")
                               cities.insert(2, "Dallas")


# In[40]:


cities[0] is "Atlanta"
cities[1] is "Baltimore"
cities[2] is "Chicago"
cities[3] is "Denver"
cities[4] is "Los Angeles"
cities[5] is "Seattle


# In[41]:


#Lists: Taking slices out of them


# In[46]:


#Lists: Deleting and removing elements


# In[ ]:


#Lists: popping elements


# In[65]:


#Tuples
states_in_order_of_founding = ["Delaware","Pennsylvania", "New Jersey", "Georgia"]
second_state_founded = states_in_order_of_founding[2]
    print("The second state founded was " +
second_state_founded)
    


# In[77]:


#for loops
cleanest_cities = ["Cheyenne", "Santa Fe", "Tucson",
"Great Falls", "Honolulu"]
city_to_check = "Tucson"
if city_to_check == cleanest_cities[0]:
    print("It's one of the cleanest cities")
elif city_to_check == cleanest_cities[1]:
    print("It's one of the cleanest cities")
elif city_to_check == cleanest_cities[2]:
    print("It's one of the cleanest cities")
elif city_to_check == cleanest_cities[3]:
    print("It's one of the cleanest cities")
elif city_to_check == cleanest_cities[4]:
    print("It's one of the cleanest cities")


# In[78]:


for a_clean_city in cleanest_cities:
    if city_to_check == a_clean_city:
        print("It's one of the cleanest cities")


# In[86]:


#for loops nested
first_names = ["BlueRay ", "Upchuck ", "Lojack ",
"Gizmo ", "Do-Rag "]
last_names = ["Zzz", "Burp", "Dogbone", "Droop"]
full_names = []
    for a_first_name in first_names:
        for a_last_name in last_names:
            full_names.append(first_name + " " +a_last_name)
            print()



# In[ ]:


#Getting information from the user and converting strings and numbers
city_to_check = input("Enter the name of a city: ")


# In[ ]:


monthly_income = input("Enter your monthly income:")


# In[ ]:


city_to_check = input("Enter the name of a city: ")


# In[ ]:


#Changing case
city_to_check = input("Enter your city: ")
city_to_check = city_to_check.lower()
cleanest_cities = ["cheyenne", "santa fe",
"tucson", "great falls", "honolulu"]
for a_clean_city in cleanest_cities:
    if city_to_check == a_clean_city:
        print("It's one of the cleanest cities")


# In[ ]:


city_to_check = input("Enter your city: ")
city_to_check = city_to_check.lower()
lowercase_city_to_check = city_to_check.lower()
city_to_check = city_to_check.lower()
 city_to_check = city_to_check.lower()
    city_to_check = city_to_check.lower()
    city_to_check = city_to_check.upper()
    print("Great news! " + city_to_check + " is one of
the cleanest cities.")


# In[ ]:


#Dictionaries: What they are
my_cats = ["Draco", "Bellatrix", "Voldemort"]
print(my_cats[0])

