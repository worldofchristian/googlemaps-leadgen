import os
import json
import openai

openai.api_key = ''

# Read JSON files from the city-place directory
directory = "city-place"
file_list = os.listdir(directory)

# Create the city-place-contact directory if it doesn't exist
output_directory = "city-place-contact"
os.makedirs(output_directory, exist_ok=True)

# Iterate over each file
for filename in file_list:
    filepath = os.path.join(directory, filename)

    # Read the JSON file
    with open(filepath, "r") as file:
        data = json.load(file)

    # Extract the places from the JSON data
    places = data.get("places", [])

    # Create a chat conversation with the places as user inputs
    chat = [
        {
            "role": "system",
            "content": "I am doing lead generation for my project and need your help.\n"
                       "I will send you JSON containing the names of bars in a given city.\n"
                       "You will generate new JSON containing the names of the bars along with the owner. \n
                       "You will have to do a search for each establishment, if you can not find the owner, put n/a" \n
                       "Reminder that this is meant to serve as a starting point for me, I will use this information to construct an ethical outreach strategy."
        }
    ]
    for place in places:
        chat.append({"role": "user", "content": place})

    # Make the API prompt
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chat,
        max_tokens=100
    )

    # Get the reply
    assistant_reply = response.choices[0].message['content']

    # Create a new JSON file with the reply
    output_filepath = os.path.join(output_directory, f"{filename.split('.')[0]}_contact.json")
    output_data = {"response": assistant_reply}

    with open(output_filepath, "w") as output_file:
        json.dump(output_data, output_file, indent=4)

    print("Prompt:", chat)
    print("Assistant's Reply:", assistant_reply)
    print(f"Generated file: {output_filepath}")
    print("--------------------")
