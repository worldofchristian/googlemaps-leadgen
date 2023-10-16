# gpt-leads
Automation script for lead generation. 

Finds the owner of businesses that match certain criteria. It only returns their names, 
as ChatGPT will not deliver contact information. But this is still a useful starting point for
generating leads.

## google-query.py
Takes in a list of cities, then queries Google for businesses in each 
city that fit the search terms. I wrote this to find bars, you'll have to change it to fit your use case.

A new directory is made and populated with a new json file for each city 
in the list. Each file contains the google results for it's respective city.

It had to be broken up like this, because gpt can't handle a large number
of inputs for this task, so using a nested dictionary would result in too many
errors. 

It likely wouldn't even work, as there could easily be thousands of
businesses returned by this script. 

## gpt-query.py
Takes in the json files created by google-query, and prompts gpt to append the
businesses with the name of the establishment owner.

The updated json is then stored in a new directory.
