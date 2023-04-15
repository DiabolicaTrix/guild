import csv
import random

# List of fake names
names = ["John Smith", "Jane Doe", "Robert Johnson", "Karen Davis", "David Brown", "Sarah Wilson",
         "Michael Miller", "Emily Taylor", "William Adams", "Amanda Lee", "Christopher Moore", "Ashley Wright",
         "Matthew Martin", "Stephanie King", "Daniel Turner", "Rachel Campbell", "Anthony Scott", "Lauren Evans",
         "Kevin Robinson", "Melissa Hall", "Richard Young", "Olivia Perez", "Mark Hernandez", "Megan Garcia",
         "Thomas Sanchez", "Laura Lewis", "Charles Cooper", "Samantha Ramirez", "Brian Peterson", "Catherine Lee",
         "Jason Flores", "Christine Parker", "Erica Stewart", "Timothy Lee", "Nicole Collins", "Edward Ortiz",
         "Hannah Torres", "George Davis", "Victoria Mitchell", "Ronald Green", "Maria Wood", "Frank Baker",
         "Christina Phillips", "Benjamin Coleman", "Margaret Wright", "Christopher Long", "Amy Morris",
         "Steven Reed", "Christina Richardson", "Joseph Howard", "Katherine Nelson", "Brandon Jackson",
         "Tiffany Scott", "Scott Kelly", "Brittany Allen", "Andrew Adams", "Natalie Ross", "Douglas Turner",
         "Angela Cook", "Peter Bailey", "Kristen Sanders", "Jesse Cooper", "Elizabeth Ward", "Sean Perez",
         "Julie Rogers", "Phillip Bell", "Molly Foster", "Keith Parker", "Vanessa Flores", "Bryan Murphy",
         "Cassandra Ramirez", "Patrick Hill", "Monica Foster", "Russell James", "Chelsea Reyes", "Adam Scott",
         "Rebecca Ward", "Derek Mitchell", "Miranda Hernandez", "Kyle Phillips", "Cynthia Ortiz", "Jordan Peterson",
         "Leah Richardson", "Jonathan Kelly", "Erica Howard", "Craig Gonzalez", "Meredith Coleman", "Tyler Baker",
         "Claire Cooper", "Ethan Green", "Caroline Torres", "Chad Wood", "Sara Lee", "Travis Perez", "Morgan King",
         "Dustin Campbell", "Brianna Long", "Raymond Martinez", "Alyssa Young", "Gregory Garcia", "Heather Brown"]

# List of fake domains
domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "aol.com"]

# List of fake roles
roles = ["Project Manager", "Lead Developer", "Backend Developer", "Frontend Developer",
         "Designer", "Marketing Manager", "Sales Manager", "Quality Assurance Engineer"]

# Generate a list of dictionaries with fake people information
people = []
for i in range(100):
    name = random.choice(names)
    first_name, last_name = name.split()
    email = f"{first_name.lower()}.{last_name.lower()}@{random.choice(domains)}"
    role = random.choice(roles)
    people.append({"Name": name, "Email": email, "Role": role})

# Write the list of dictionaries to a CSV file
with open("fake_people.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["Name", "Email", "Role"])
    writer.writeheader()
    for person in people:
        writer.writerow(person)
