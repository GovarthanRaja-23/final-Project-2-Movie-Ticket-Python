from datetime import datetime
import mysql.connector
import displaymovie
import mail

# Function to initialize the database and table
def initialize_database():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
    )
    cursor = conn.cursor()
    
    # Create database if not exists
    cursor.execute("CREATE DATABASE IF NOT EXISTS movie_booking_db")
    
    # Switch to the movie_booking_db database
    cursor.execute("USE movie_booking_db")

    # Drop the bookings table if it exists
    cursor.execute("DROP TABLE IF EXISTS bookings")
    
    # Create bookings table if not exists
    cursor.execute('''CREATE TABLE IF NOT EXISTS bookings (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        movie_name VARCHAR(255),
                        tickets INT,
                        snacks VARCHAR(3),
                        row_no INT,
                        seat_no INT,
                        gst_amt DECIMAL(10, 2),
                        total_amt DECIMAL(10, 2),
                        booking_time DATETIME)''')
    
    conn.commit()
    cursor.close()
    conn.close()


#Function to Book Tickets
def booking_tickets():
    initialize_database() #call this function to initialize database if not present

    movies=displaymovie.display_movies()
    choice_movie=input("Enter the Number Associated with the Movie you want to watch : ")
    if choice_movie not in movies:
        print("Invalid Movie Selection...! Enter only from the Displayed movies...")
        return
    selected_movie=movies[choice_movie]
    print(f"Selected Movie Title : {selected_movie['name']}")
    print("Available Timings :")
    for i,timing in enumerate(selected_movie['timings'],start=1):
        print(f"{i}.{timing}")
    choice_timing=int(input("Enter the Index number Associated with the Timing you Want : "))
    if choice_timing < 1 or choice_timing>len(selected_movie['timings']):
        print("Invalid Timing you have Chosen...!")
        return
    timing_selected=selected_movie['timings'][choice_timing-1]
    print(f"Selected Timing : {timing_selected}")

    #Seat selection
    rows=12
    seats_per_row=15

    row_choice=int(input(f"Choose a Row (1-{rows}) : "))
    if row_choice<1 or row_choice>rows:
        print("Invalid Row Choice...!")
        return
    elif row_choice>=1 and row_choice<=3:
        ticket_price=180
        num_tickets=int(input("Enter the Number of Tickets You want :" ))
        total_cst=num_tickets*ticket_price
        gst_rate=0.19
        gst_amt=total_cst*gst_rate
        total_amt=total_cst+gst_amt
        snacks_choice = input("Would you like Popcorn as your Snacks (yes/no)? ").lower()
        snacks_cost = 80
        if snacks_choice == "yes":
            snacks_cost = snacks_cost * num_tickets  # Assume each snack costs $5

        total_amt += snacks_cost

    elif row_choice>=4 and row_choice<=9:
        ticket_price=190
        num_tickets=int(input("Enter the Number of Tickets You want :" ))
        total_cst=num_tickets*ticket_price
        gst_rate=0.19
        gst_amt=total_cst*gst_rate
        total_amt=total_cst+gst_amt
        snacks_choice = input("Would you like Popcorn as your Snacks (yes/no)? ").lower()
        snacks_cost = 80
        if snacks_choice == "yes":
            snacks_cost = snacks_cost * num_tickets  # Assume each snack costs $5
            
        total_amt += snacks_cost
    else:
        ticket_price=200
        num_tickets=int(input("Enter the Number of Tickets You want :" ))
        total_cst=num_tickets*ticket_price
        gst_rate=0.19
        gst_amt=total_cst*gst_rate
        total_amt=total_cst+gst_amt
        snacks_choice = input("Would you like Popcorn as your Snacks (yes/no)? ").lower()
        snacks_cost = 80
        if snacks_choice == "yes":
            snacks_cost = snacks_cost * num_tickets  # Assume each snack costs $5
            
        total_amt += snacks_cost
    seat_choice=int(input(f"Choose a Seat (1-{seats_per_row}) : "))
    if seat_choice<1 or seat_choice>seats_per_row:
        print("Invalid Seat Choice...!")
        return
    
    print("\nBooking Summary:")
    print(f"Movie: {selected_movie['name']}")
    print(f"Timing: {timing_selected}")
    print(f"Seat: Row {row_choice}, Seat {seat_choice}")
    print(f"Number of Tickets: {num_tickets}")
    if snacks_choice == "yes":
        print("Snacks: Yes")
    else:
        print("Snacks: No")
    print(f"Total Cost: ${total_amt:.2f}")
    with open('bill.txt', 'w') as bill_file:
        bill_file.write("")
    with open('bill.txt', 'a') as bill_file:
        bill_file.write(f"\nDate and Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        bill_file.write(f"Movie: {selected_movie['name']}\n")
        bill_file.write(f"Timing: {timing_selected}\n")
        bill_file.write(f"Seat: Row {row_choice}, Seat {seat_choice}\n")
        bill_file.write(f"Number of Tickets: {num_tickets}\n")
        if snacks_choice == "yes":
            bill_file.write(f"Snacks: Yes\n")
        else:
            bill_file.write(f"Snacks: No\n")
        bill_file.write(f"Total Cost: ${total_amt:.2f}\n")
    mail.mail()

    conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="movie_booking_db"
)
    cursor = conn.cursor()

    insert_query = '''INSERT INTO bookings 
                  (movie_name, tickets, snacks, row_no, seat_no, gst_amt, total_amt, booking_time) 
                  VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'''

    booking_data = (selected_movie['name'], num_tickets, snacks_choice[:3], row_choice, seat_choice, gst_amt, total_amt, datetime.now())
    cursor.execute(insert_query, booking_data)

    conn.commit()
    cursor.close()
    conn.close()

print("\nYour tickets have been booked. Enjoy the movie!")
# Main function to initiate the program
def main():
    print("Welcome to Movie Ticket Booking System\n")
    booking_tickets()
    cont=input("Do you want to Book Ticket for Another movie (yes/no) : ")
    if cont=="yes":
        print("Welcome to Movie Ticket Booking System\n")
        booking_tickets()
    else:
        print("<----THANK YOU !!!---->")
if __name__ == "__main__":
    main()
