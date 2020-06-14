import sys
import csv
import re


adjustments = {
    "^SOT-23": 180,
    "^LQFP-": 270,
    "^HTSSOP-": 270,
    "^SOIC-": 270,
    "^MSOP-": 270,
    "^CP_Elec": 180,
    "^CP_EIA": 180,
}
"""Adjustments for packages."""


with open(sys.argv[1], "r") as in_file, open(sys.argv[2], "w") as out_file:
    reader = csv.DictReader(in_file)

    writer = csv.DictWriter(
        out_file, fieldnames=["Designator", "Mid X", "Mid Y", "Layer", "Rotation"]
    )
    writer.writeheader()

    for row in reader:
        # check if any adjustment is required
        adjustment = 0
        for pkg_re, pkg_adjustment in adjustments.items():
            if re.match(pkg_re, row["Package"]):
                adjustment = pkg_adjustment
                print("Adjusting", row["Ref"], row["Package"], adjustment)
                break

        # place content in "JLC" format
        writer.writerow(
            {
                "Designator": row["Ref"],
                "Mid X": row["PosX"] + "mm",
                "Mid Y": row["PosY"] + "mm",
                "Layer": row["Side"].capitalize(),
                "Rotation": (int(float(row["Rot"])) + adjustment) % 360,
            }
        )
