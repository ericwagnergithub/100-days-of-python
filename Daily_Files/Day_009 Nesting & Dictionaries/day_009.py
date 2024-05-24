#Dictionary
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

#Nesting a list in a dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
    }


#Nesting a dictionary in a dictionary

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total visits":  12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total visits":  5}
    }

#Nesting a dictionary in a list
#useful if index needed
[{
    Key: [List],    
    Key2: {Dict}
},
{
    Key: Value,
    Key2: Value
}]

travel_log = [
    {
        "country":"France", 
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total visits": 12},
    {
        "country": "Germany", 
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
        "total visits": 5}
]