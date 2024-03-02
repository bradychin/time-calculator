# Declare variables 
start_time = "11:06 PM" # HH:MM AM/PM
duration = "08:02" # HH:MM
start_day = "TueSDay" # Optional

# Add duration to start time
def add_time(start, duration, start_day=None):

  # Define days of the week
  days_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
  days_later = 0
  day_index = 0
  
  # Parse the time
  start_time, period = start.split()
  start_time_components = start_time.split(':')
  duration_components = duration.split(':')

  # Calculate final time
  final_minute = int(start_time_components[1]) + int(duration_components[1])
  final_hour = int(start_time_components[0]) + int(duration_components[0])
  final_days_later = ''

  if final_minute >= 60:
    final_minute -= 60
    final_hour += 1
  
  while final_hour >= 12:
    if period == 'AM':
      period = 'PM'
      final_hour -= 12
    elif period == 'PM':
      period = 'AM'
      final_hour -= 12
      days_later += 1
  
  if days_later == 1:
    final_days_later = '(next day)'
  elif days_later > 1: 
    final_days_later = f'({days_later} days later)'

  # Determine day of the week
  if start_day is not None:
    start_day = start_day.capitalize()
    day_index = days_of_the_week.index(start_day)
    day_index += days_later
  
    while day_index > 6:
      day_index -= 7

  final_week_day = days_of_the_week[day_index]
  
  # Format the final time
  if final_hour == 0:
    final_hour = 12

  final_time = f"{final_hour}:{final_minute:02d} {period}"
  if days_later > 0:
    if start_day is not None:
      return f"{final_time}, {final_week_day} " + final_days_later
    else:
      return f"{final_time} " + final_days_later
  else:
    if start_day is not None:
      return f"{final_time}, {final_week_day}"
    else:
      return f"{final_time}"

# Print result 
print("\n" + add_time(start_time, duration, start_day) + "\n")