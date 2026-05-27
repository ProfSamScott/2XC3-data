import csv

for year in range(1968, 2026):
    with open(f"atp_matches_{year}.csv") as file:
        r = csv.reader(file)
        with open(f"atp_results_{year}.txt","w") as f:
            skip = True
            for list in r:
                if not skip:
                    f.write(f"{list[10]}, {list[18]}\n")
                skip = False
            
for year in range(1968, 2026):
    with open(f"wta_matches_{year}.csv") as file:
        r = csv.reader(file)
        with open(f"wta_results_{year}.txt","w") as f:
            skip = True
            for list in r:
                if not skip:
                    f.write(f"{list[10]}, {list[18]}\n")
                skip = False