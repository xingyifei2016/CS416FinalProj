import re
import pandas as pd
from pdb import set_trace as st
us_state_to_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
    "District of Columbia": "DC",
}


us_info = pd.read_csv('./us_data.csv')

def get_state_value(state_name, info):
  # state_name is just an abbreviation
  state = None
  for i in us_state_to_abbrev:
    if re.match(us_state_to_abbrev[i], state_name):
      state = i
  if state is None:
    return None
  return us_info[us_info["Province_State"]==state][info].values[0]


write_file = []
with open('mapdata.js') as dataFile:
    data = dataFile.readlines()
    current_state = None
    for i in data:
      if re.match("\s*[A-Z][A-Z]\s*:\s*\{", i):
        current_state = re.findall(r'[A-Z][A-Z]', i)[0]
      if re.match("\s*description:.*", i) and current_state is not None:
        split_colon = i.split(":")
        split_comma = split_colon[1].split(",")
        current_confirmed = get_state_value(current_state, "Confirmed")
        if current_confirmed:
          split_comma[0] = '"Confirmed: '+str(current_confirmed)+' \\n Deaths: '+str(get_state_value(current_state, "Deaths"))+'"'
        split_colon[1] = ','.join(split_comma)
        write_file.append(':'.join(split_colon))
      else:
        write_file.append(i)


with open('mapdata1.js', 'w') as f:
  for i in write_file:
    f.write(i)








