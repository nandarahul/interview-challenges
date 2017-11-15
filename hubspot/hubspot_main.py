"""
Author: Rahul Nanda
9th October 2017

*** Python 2.7 ***
"""

import requests
import sys
import json
import datetime
GET_URL = "https://candidate.hubteam.com/candidateTest/v2/partners?userKey=e418b67ecc80abceb128933bb27c"
POST_URL = "https://candidate.hubteam.com/candidateTest/v2/results?userKey=e418b67ecc80abceb128933bb27c"


def get_info():
    r = requests.get(GET_URL)
    if r.status_code != 200:
        print ("Initial call to the API: [%s] returned status code:[%d]. Please fix this. Exiting now.." % (URL, r.status_code))
        sys.exit()
    return r.json()


def send_data(data):
    r = requests.post(POST_URL, data=json.dumps(data))
    print r.status_code
    print r.text


# Specific to a country
def compute_country_event_info(country_name, country_partner_list):
    date_email_dict = {}
    for partner in country_partner_list:
        for date_str in partner["availableDates"]:
            if date_str in date_email_dict:
                date_email_dict[date_str].append(partner["email"])
            else:
                date_email_dict[date_str] = [partner["email"]]
    date_count_list = []
    for date_str in date_email_dict:
        date_parse_list = map(int, date_str.split('-'))
        date_obj = datetime.date(date_parse_list[0], date_parse_list[1], date_parse_list[2])
        date_count_list.append((date_obj, date_email_dict[date_str]))

    date_count_list = sorted(date_count_list, key=lambda dc: dc[0])
    max_attendees_count, max_date_obj, max_attendees_emails = 0, None, []
    for i in xrange(len(date_count_list)-1):
        time_difference = date_count_list[i+1][0] - date_count_list[i][0]
        if time_difference.days == 1:
            both_days_attendees = set(date_count_list[i][1]).intersection(set(date_count_list[i+1][1]))
            if len(both_days_attendees) > max_attendees_count:
                max_attendees_count = len(both_days_attendees)
                max_attendees_emails = list(both_days_attendees)
                max_date_obj = date_count_list[i][0]

    start_date_str = None
    if max_attendees_count > 0:
        start_date_str = max_date_obj.isoformat()

    country_event_info = {"attendeeCount": max_attendees_count,
                          "attendees": sorted(max_attendees_emails),
                          "name": country_name,
                          "startDate": start_date_str}

    #print country_event_info
    return country_event_info


if __name__ == "__main__":
    data = get_info()
    country_dict = {}
    for partner in data["partners"]:
        if partner["country"] in country_dict:
            country_dict[partner["country"]].append(partner)
        else:
            country_dict[partner["country"]] = [partner]

    final_result = {"countries":[]}
    for country_name in country_dict:
        country_event_info = compute_country_event_info(country_name, country_dict[country_name])
        final_result["countries"].append(country_event_info)
    print final_result
    send_data(final_result)
