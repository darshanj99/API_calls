import requests
import pprint

try:
# create an empty list to store the records
    all_records = []

    params={"limit": 100, "offset": 1}
# loop until we fetch 500 records
    while params.get("offset") < 500:
    # make the API request with the current limit and offset
        response = requests.get(
            "https://globalmart-api.onrender.com/mentorskool/v1/sales",
            headers={"access_token": "fe66583bfe5185048c66571293e0d358"},
            params=params
        ).json()

    all_records.append(response)
    params["offset"] = int(response.get("next").split("=")[1][:3])
    pprint.pprint(all_records)
    print(len(all_records))

except requests.exceptions.RequestException as r:
    print(r)
