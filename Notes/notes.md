## project guidelines:
minimum project requirements:
1. A CLI application that solves a real-world problem and adheres to best practices.
2. A database created and modified with SQLAlchemy ORM with 2+ related tables.
3. A well-maintained virtual environment using Pipenv.
4. Proper package structure in your application.
5. Use of lists and dicts.

# Consider these stretch goals as you progress through your project:

> A database created and modified with SQLAlchemy ORM with 3+ related tables.
> Use of many-to-many relationships with SQLAlchemy ORM.
> Use of additional data structures, such as ranges and tuples.

## "Submitted project pitch"
Main idea: Trip cost Calculator (calculating the expenses spend on the trip by a person)

user story: calculating total expense of a person going on a trip. Enter name of person on trip and mode of travel car, give location details (from and to places), if person travel by car calculate travel cost based on fuelcost, if person travel by flight get travel cost based on flight ticket. Now get accommodation cost, food cost and other expenses cost add them in total trip cost. 

tables/ class (based on many to many relationship)

person class: attributes( id , name, ..)

expense class(id, category, travelid, personid) (relationship expense to travel, expense to accommodation, expense to food) (one to many relationship)

trip class(id, from and to location , travel mode) method based calculate distance, miles, fuel cost.
accomodation cost, food cost 


most challenging: calculate distance based on to and from location picking API, querying to get  details like expense. travel_cost , person.expense_details
