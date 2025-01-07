def getWorldContext():
    from datetime import datetime
    world_context = ""

    # Get the current date and time
    now = datetime.now()

    # Format it to a readable string
    date_format = now.strftime("%A, %B %d, %Y")
    time_format = now.strftime("%I:%M %p")

    world_context = f"Today the date is {date_format} and the time is {time_format}."
    return world_context
