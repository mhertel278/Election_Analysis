counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
#print(counties_dict)
#for county, voters in counties_dict.items():
 #   print(f"{county} county has {voters:,} registered voters")
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
#for county_dict in voting_data:
 #       print(f"{county_dict['county']} county has {county_dict['registered_voters']:,} registered voters")

import csv
dir(csv)
