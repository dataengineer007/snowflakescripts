from datetime import datetime

today = datetime.now()
date_str = today.strftime("%d%b%Y")

#print result
print(f"Today is {date_str}")
