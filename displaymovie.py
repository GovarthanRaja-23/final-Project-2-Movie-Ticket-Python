def display_movies():
        movies = {
        "1": {"name": "Aranmanai 4", "timings": ["10:00 AM", "2:00 PM", "6:00 PM"]},
        "2": {"name": "PT Sir", "timings": ["11:00 AM", "3:00 PM", "7:00 PM"]},
        "3": {"name": "Bad Boys For Life", "timings": ["9:30 AM", "1:30 PM", "5:30 PM"]},
        "4": {"name": "Garudan", "timings": ["10:00 AM", "2:00 PM", "6:00 PM"]},
        "5": {"name": "Kalki", "timings": ["11:00 AM", "3:00 PM", "7:00 PM"]},
        "6": {"name": "Maharaja", "timings": ["9:30 AM", "1:30 PM", "5:30 PM"]}
    }
        print("Today's Movie Details :")
        for key,movie in movies.items():
            print(f"{key}.{movie['name']}")
        return movies  
  
