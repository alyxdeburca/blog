from firebase import firebase as fb
import json
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.dates
import datetime as dt
item_name = "Recoil Case"
db = fb.FirebaseApplication("https://pricetrack-csgo-default-rtdb.europe-west1.firebasedatabase.app/", None)
allRecords = db.get(item_name, None)
records = []
for i in allRecords:
    records.append(float(allRecords[i]))
recordTime = db.get('time', None)
times = []
for i in recordTime:
    times.append(int(dt.datetime.utcfromtimestamp(float(recordTime[i])).strftime('%H%M')))
plt.plot(records)
plt.ylim(ymax = max(records), ymin= 0)
plt.yticks(np.arange(0, max(records)+1, 0.5))
plt.xticks(np.arange(min(times), max(times), min(times) -max(times)))
plt.title(f"Price of {item_name}")
plt.savefig(f'{item_name}.png')