
# coding: utf-8

# In[2]:


#Dictionaries: What they are
my_cats = ["Draco", "Bellatrix", "Voldemort"]
print(my_cats[0],my_cats[1])


# In[7]:


#Dictionaries: How to code one
customer_29876 = {"first name": "David", "last name": "Elliott", "address": "4803 Wellesley St."}

print(customer_29876)


# In[13]:


jobs_to_do_1st = ["email", "texting", "calls"]
jobs_to_do_1st = []
customer_29876 = {"first name": "David", "last name": "Elliott", "address": "4803 Wellesley St."}
print(jobs_to_do_1st,customer_29876)


# In[17]:


#Dictionaries: How to pick information out of them
customer_29876 = {"first name": "David", "last name": "Elliott", "address": "4803 Wellesley St."}
cities = ["Cheyenne", "Santa Fe", "Tucson",
"Great Falls", "Honolulu"]
city_to_check = cities[3]
print(city_to_check)
address_of_customer = customer_29876["address"]
print(address_of_customer)


# In[27]:


#Dictionaries: The versatility of keys and values
customer_29876 = {"first name": "David", "last name": "Elliott", "address": "4803 Wellesley St."}
rankings = {5: "Finland", 2: "Norway", 3: "Sweden", 7: "Iceland"}
second_ranking_country = rankings[2],customer_29876
print(second_ranking_country)
country_ranks_so_far = {"Finland": 5, "Norway": 2,"Sweden": 3, "Iceland": 7}
norway_ranking = country_ranks_so_far["Norway"]
print("norwar ranking is",norway_ranking)


# In[29]:


#Dictionaries: Adding items
address_of_customer = customer_29876["address"]
customer_29876["city"] = "Toronto"
print(customer_29876["city"])


# In[67]:


#Dictionaries: Removing and changing items
customer_29876 = {"first name": "David", "last name": "Elliott", "address": "4803 Wellesley St."}
cities = ["Cheyenne", "Santa Fe", "Tucson",
"Great Falls", "Honolulu"]
del customer_29876["address"]
customer_29876["address"] = "Winipeg"
print(customer_29876["address"])


# In[77]:


#Dictionaries: Looping through values
customer_29876 = {"first name": "David", "last name": "Elliott", "address": "4803 Wellesley St."}

print(customer_29876["first name"])
print(customer_29876["last name"])
print(customer_29876["address"])


# In[99]:


cities = ["Cheyenne", "Santa Fe", "Tucson","Great Falls", "Honolulu"]
print("cleanest_cities")
cleanest_cities= cities[3]
print(cleanest_cities)


# In[124]:


#Dictionaries: Looping through keys
customer_29876= {"first name": "David", "last name": "Elliott", "address": "4803 Wellesley St."}

for each_key in customer_29876.keys():
        print(each_key)


# In[121]:


#Dictionaries: Looping through keys
customer_29876 = {
    "first name": "David",
    "last name": "Elliott",
    "address": "4803 Wellesley St.",}
for each_value in customer_29876.values():
    print(each_value)


# In[111]:


#Dictionaries: Looping through keyvalue pairs
customer_29876 = {
    "first name": "David",
    "last name": "Elliott",
    "address": "4803 Wellesley St.",}
for each_key, each_value in customer_29876.items():
    print("The customer's " + each_key + " is " +
each_value)


# In[127]:


#Creating a list of dictionaries
customers = [
 {
 "customer id": 0,
 "first name":"John",
 "last name": "Ogden",
"address": "301 Arbor Rd.",
 },
    
 {
 "customer id": 1,
 "first name":"Ann",
 "last name": "Sattermyer",
 "address": "PO Box 1145",
 },
    
 {
 "customer id": 2,
 "first name":"Jill",
 "last name": "Somers",
 "address": "3 Main St.",
 },
    
]
print(customers)


# In[136]:


#How to pick information out of a list of dictionarie
customer_first_name = customer_29876["first name"]
print(customer_first_name)


# In[140]:


#Creating a dictionary that contains lists
customer_29876 = {
 "first name": "David",
 "last name": "Elliott",
 "address": "4803 Wellesley St.",
 "discounts": ["standard", "volume", "loyalty"],
}
if "brother-in-law" in customer_29876["discounts"]: discount_amount = .30
 elif "loyalty" in customer_29876["discounts"]: discount_amount = .15
 elif "volume" in customer_29876["discounts"]: discount_amount = .10
 elif "standard" in customer_29876["discounts"]: discount_amount = .05


# In[143]:


#Creating a dictionary that contains a dictionary
customers = {
 {
 "customer id": 0,
 "first name":"John",
 "last name": "Ogden",
 "address": "301 Arbor Rd.",
 },
 {
 "customer id": 1,
 "first name":"Ann",
 "last name": "Sattermyer",
 "address": "PO Box 1145",
 },
 {
 "customer id": 2,
 "first name":"Jill",
 "ast name": "Somers",
 "address": "3 Main St.",
 },
}


# In[147]:


#dictionary within another dictionary
customers = {
 0: {
 "first name":"John",
 "last name": "Ogden",
 "address": "301 Arbor Rd.",
 },
 1: {
 "first name":"Ann",
 "last name": "Sattermyer",
 "address": "PO Box 1145",
 },
 2: {
 "first name":"Jill",
 "last name": "Somers",
 "address": "3 Main St.",
 },
}
print(customers[2])
print(customers[2]["address"])


# In[155]:


#Functions
first_number = 2
second_number = 3
total = first_number + second_number
print(total)
def add_numbers():
    first_number = 2
    second_number = 3
    total = first_number + second_number
    print(total)


# In[185]:


#Functions: Passing them information
whatever = "Hello, there."
print(whatever)


# In[202]:


#Functions: Passing information to them a different way
 say_names_of_couple(husband_name="Bill",wife_name="Zelda")
    def say_names_of_couple(husband_name, wife_name):
    print("The names of the couple are " + husband_name + " and " + wife_name)


# In[4]:


#Functions: Assigning a default value to a parameter
calc_tax (sales_total=101.37, tax_rate=.05)
total=(sales_total*tax_rate)
    print(total)
    

