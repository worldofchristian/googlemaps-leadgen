import pickle

# 173 Canadian cities, listed in descending order by population
cities = [
    "Toronto",
    "Montreal",
    "Vancouver",
    "Calgary",
    "Edmonton",
    "Ottawa",
    "Mississauga",
    "Winnipeg",
    "Québec City",
    "Hamilton",
    "Brampton",
    "Surrey",
    "Laval",
    "Halifax",
    "London",
    "Markham",
    "Vaughan",
    "Gatineau",
    "Longueuil",
    "Burnaby",
    "Saskatoon",
    "Kitchener",
    "Windsor",
    "Regina",
    "Richmond",
    "Richmond Hill",
    "Oakville",
    "Burlington",
    "Greater Sudbury",
    "Sherbrooke",
    "Oshawa",
    "Saguenay",
    "Lévis",
    "Barrie",
    "Abbotsford",
    "Coquitlam",
    "Trois-Rivières",
    "St. Catharines",
    "Guelph",
    "Cambridge",
    "Whitby",
    "Kelowna",
    "Kingston",
    "Ajax",
    "Langley",
    "Saanich",
    "Terrebonne",
    "Milton",
    "St. John's",
    "Thunder Bay",
    "Waterloo",
    "Delta",
    "Chatham-Kent",
    "Red Deer",
    "Strathcona County",
    "Brantford",
    "Saint-Jean-sur-Richelieu",
    "Cape Breton",
    "Lethbridge",
    "Clarington",
    "Pickering",
    "Nanaimo",
    "Kamloops",
    "Niagara Falls",
    "North Vancouver",
    "Victoria",
    "Brossard",
    "Repentigny",
    "Newmarket",
    "Chilliwack",
    "Maple Ridge",
    "Peterborough",
    "Kawartha Lakes",
    "Drummondville",
    "Saint-Jérôme",
    "Prince George",
    "Sault Ste. Marie",
    "Moncton",
    "Granby",
    "Wood Buffalo",
    "Norfolk County",
    "Belleville",
    "Saint-Hyacinthe",
    "North Bay",
    "Kanata",
    "Rouyn-Noranda",
    "Moose Jaw",
    "Saint John",
    "Guelph/Eramosa",
    "Caledon",
    "Centre Wellington",
    "Spruce Grove",
    "Dollard-des-Ormeaux",
    "New Westminster",
    "Terrace",
    "North Cowichan",
    "St. Albert",
    "Stratford",
    "Halton Hills",
    "Airdrie",
    "North Bay",
    "Thunder Bay",
    "Red Deer",
    "Chatham-Kent",
    "Kamloops",
    "Nanaimo",
    "Fredericton",
    "Lethbridge",
    "Granby",
    "Belleville",
    "Sarnia",
    "Rimouski",
    "Prince Albert",
    "Newmarket",
    "Caledon",
    "Wood Buffalo",
    "Lloydminster",
    "Chilliwack",
    "Jonquière",
    "Rivière-du-Loup",
    "Maple Ridge",
    "Courtenay",
    "Mascouche",
    "Salaberry-de-Valleyfield",
    "Penticton",
    "Joliette",
    "Mirabel",
    "Sorel-Tracy",
    "Spruce Grove",
    "Campbell River",
    "Terrace",
    "Peterborough",
    "Cornwall",
    "Fort Erie",
    "Boisbriand",
    "Midland",
    "Saint-Bruno-de-Montarville",
    "Sept-Îles",
    "Salmon Arm",
    "Port Alberni",
    "Brockville",
    "Sylvan Lake",
    "Leduc",
    "Thetford Mines",
    "Collingwood",
    "Pembroke",
    "Vaudreuil-Dorion",
    "Tillsonburg",
    "Orillia",
    "Bathurst",
    "Baie-Comeau",
    "Saint-Constant",
    "Oakville",
    "Sainte-Julie",
    "Whitehorse",
    "Welland",
    "Miramichi",
    "Prince Rupert",
    "Leamington",
    "Fort Saskatchewan",
    "Brandon",
    "Moose Jaw",
    "Strathmore",
    "Langford",
    "Woodstock",
    "Dartmouth",
    "Esquimalt",
    "Burlington",
    "Conception Bay South",
    "Sydney",
    "North Perth",
    "Glace Bay",
    "Montréal-Est"
]

# export
with open("cities.pickle", "wb") as file:
    pickle.dump(cities, file)