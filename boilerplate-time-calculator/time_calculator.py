def add_time(start, duration,weekday='none'):

  weekday = weekday.lower()
  weekdays = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']

  duration_splited = duration.split(":")

  duration_hour = int(duration_splited[0])
  duration_minute = int(duration_splited[1])

  if duration_hour == 0 and duration_minute == 0:
    message = start
  else:
    day = 0

    start_splited = start.split()
    time = start_splited[0]
    stripe = start_splited[1]

    time_splited = time.split(":")

    start_hour = int(time_splited[0])
    start_minute = int(time_splited[1])

    if stripe == "PM":
      start_hour = start_hour + 12

    add_to_final_hour = 0

    for i in range(duration_minute):
      start_minute = start_minute + 1
      if start_minute == 60:
        start_minute = 0
        add_to_final_hour = 1

    start_hour =  start_hour + add_to_final_hour

    if start_hour == 24:
      start_hour = 12
      day = day + 1

    for i in range(duration_hour):
      start_hour = start_hour + 1
      if start_hour == 24:
        start_hour = 0
        day = day + 1

    final_minute = start_minute

    final_hour = start_hour

    if final_hour > 12 and final_hour < 24 or day == 0:
      stripe = "PM"
    else:
      stripe = "AM"

    if day == 0:
      if final_hour != 12:
        final_hour = final_hour - 12

    if final_minute < 10:
      final_minute = "0" + str(final_minute)
    else:
      final_minute = str(final_minute)

    if weekday == "none":
      if day == 0:
        message = str(final_hour) + ":" + final_minute + " " + stripe
      elif day == 1:
        message = str(final_hour) + ":" + final_minute + " " + stripe + " " + "(next day)"
      else:
        message = str(final_hour) + ":" + final_minute + " " + stripe + " " + "(" + str(day) + " days later)"
    else:
      index = weekdays.index(weekday)

      for i in range(index):
        weekdays.append(weekdays.pop(0))

      if day > 7:
        move = day % 7
        weekday = weekdays[move]
      else:
        weekday = weekdays[day]

      if day == 0:
        message = str(final_hour) + ":" + final_minute + " " + stripe + ", " + weekday.capitalize()
      elif day == 1:
        message = str(final_hour) + ":" + final_minute + " " + stripe + ", " + weekday.capitalize() + " " + "(next day)"
      else:
        message = str(final_hour) + ":" + final_minute + " " + stripe + ", " + weekday.capitalize() + " " + "(" + str(day) + " days later)"

  return message
