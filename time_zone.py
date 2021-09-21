import  pytz
from datetime import datetime

ist = pytz.timezone("Asia/Kolkata")
et= pytz.timezone('America/New_York')
bst= pytz.timezone('Europe/London')

print("Time zone in New Delhi = ",datetime.now(tz=ist))
print("Time in New York =",datetime.now(tz=et))
print("Time zone in London = ",datetime.now(tz=bst))
