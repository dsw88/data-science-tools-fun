import requests
import datetime
import shutil

this_year = datetime.datetime.today().year

for start_year in range(this_year-1, this_year-29, -1):
    end_year = str((start_year+1) % 100).zfill(2)
    start_year = str(start_year % 100).zfill(2)

    url = "http://www.dougstats.com/{start_year}-{end_year}RD.Team.txt".format(start_year=start_year, end_year=end_year)
    print("Downloading {}".format(url))
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open("{start_year}-{end_year}.Team.txt".format(start_year=start_year, end_year=end_year), 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
    else:
        url = "http://www.dougstats.com/{start_year}-{end_year}RD.Team.html".format(start_year=start_year, end_year=end_year)
        r = requests.get(url, stream=True)
        print("Downloading {}".format(url))
        if r.status_code == 200:
            with open("{start_year}-{end_year}.Team.html".format(start_year=start_year, end_year=end_year), 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
        else:
            print("Error downloading: {}".format(r.status_code))