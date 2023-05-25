# solar_activity.py 
# Joe Murray 
# gets solar activity from nasa.gov's public API

import requests
import json
import datetime

# solar energetic particle
def get_sep_activity():
    today = datetime.date.today() - datetime.timedelta(days=1)
    response = requests.get(f"https://api.nasa.gov/DONKI/SEP?startDate={today.year}-{today.month}-{today.day}&endDate={today.year}-{today.month}-{today.day}&api_key=DEMO_KEY")
    if response.status_code == 200:
        try:
            return json.loads(response.content)
        except json.decoder.JSONDecodeError:
            return None
    else:
        raise Exception("Error getting solar energetic particle (SEP) activity")

# geomagnetic storm
def get_gst_activity():
    today = datetime.date.today() - datetime.timedelta(days=1)
    response = requests.get(f"https://api.nasa.gov/DONKI/GST?startDate={today.year}-{today.month}-{today.day}&endDate={today.year}-{today.month}-{today.day}&api_key=DEMO_KEY")
    if response.status_code == 200:
        try:
            return json.loads(response.content)
        except json.decoder.JSONDecodeError:
            return None
    else:
        raise Exception("Error getting geomagnetic storm (GST) activity")

# solar flare
def get_flr_activity():
    today = datetime.date.today() - datetime.timedelta(days=1)
    response = requests.get(f"https://api.nasa.gov/DONKI/FLR?startDate={today.year}-{today.month}-{today.day}&endDate={today.year}-{today.month}-{today.day}&api_key=DEMO_KEY")
    if response.status_code == 200:
        try:
            return json.loads(response.content)
        except json.decoder.JSONDecodeError:
            return None
    else:
        raise Exception("Error getting solar flare (FLR) activity")

# coronal mass ejection
def get_cme_activity():
    today = datetime.date.today() - datetime.timedelta(days=1)
    response = requests.get(f"https://api.nasa.gov/DONKI/CME?startDate={today.year}-{today.month}-{today.day}&endDate={today.year}-{today.month}-{today.day}&api_key=DEMO_KEY")
    if response.status_code == 200:
        try:
            return json.loads(response.content)
        except json.decoder.JSONDecodeError:
            return None
    else:
        raise Exception("Error getting coronal mass ejection (CME) activity")

def main():
    sep_activity = get_sep_activity()
    if sep_activity is not None:
        if len(sep_activity) > 0:
            print(f"SEP activity for today: {json.dumps(sep_activity, indent=2)}")
        else:
            print("No SEP activity recorded today")
    else:
        print("No SEP activity recorded today")

    cme_activity = get_cme_activity()
    if cme_activity is not None:
        if len(cme_activity) > 0:
            print(f"CME activity for today: {json.dumps(cme_activity, indent=2)}")
        else:
            print("No CME activity recorded today")
    else:
        print("No CME activity recorded today")


    gst_activity = get_gst_activity()
    if gst_activity is not None:
        if len(gst_activity) > 0:
            print(f"GST activity for today: {json.dumps(gst_activity, indent=2)}")
        else:
            print("No GST activity recorded today")
    else:
        print("No GST activity recorded today")


    flr_activity = get_flr_activity()
    if flr_activity is not None:
        if len(flr_activity) > 0:
            print(f"FLR activity for today: {json.dumps(flr_activity, indent=2)}")
        else:
            print("No FLR activity recorded today")
    else:
        print("No FLR activity recorded today")

if __name__ == "__main__":
    main()