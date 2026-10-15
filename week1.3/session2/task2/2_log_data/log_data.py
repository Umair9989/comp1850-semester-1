# Week 1.3, Session 2: Log Data Filtering

# We want to find all failed login attempts based on Request and Status code 
# (i.e., POST /login with the response 401) in a log file and print these out in a
# human-readable format.


# open and read the file

# find all failed login attempts (POST /login with the response 401)
# and print these out in a human-readable format:
# IP address 192.168.1.17 failed to login at 10:42:12 on 2024-10-20
try:
    with open(site.log, mode='r', encoding='utf-8') as file:
        # Read all lines and skip the header
        lines = file.readlines()
        data_lines = lines[1:] 
        
        for line in data_lines:
            # Splits line by commas (change to line.split() if separated by whitespace)
            row = line.strip().split(',')
            
            if len(row) >= 6:
                date, time, ip_address, user_agent, request, status_code = row[:6]
                
                if request == 'POST /login' and status_code == '401':
                    print(f"IP address {ip_address} failed to login at {time} on {date}")
except FileNotFoundError:
    print(f"Error: '{site.log}' not found.")


# Hints:
# - Remember to handle file errors
# - The first row is headers - you'll need to skip it
# - Each row has: Date, Time, IP_Address, User_Agent, Request, Status_Code
# - You need to find rows where Request = "POST /login" AND Status_Code = "401"
# - You can use list comprehension or loops to filter the data