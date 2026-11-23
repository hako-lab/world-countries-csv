"""Regenerate countries.csv from the iso-codes database via pycountry."""
import csv
import pycountry

FIELDS = ["alpha_2", "alpha_3", "numeric", "name", "official_name", "flag"]

def rows():
    for c in sorted(pycountry.countries, key=lambda c: c.alpha_2):
        yield {
            "alpha_2": c.alpha_2,
            "alpha_3": c.alpha_3,
            "numeric": c.numeric,
            "name": c.name,
            "official_name": getattr(c, "official_name", ""),
            "flag": getattr(c, "flag", ""),
        }

if __name__ == "__main__":
    with open("countries.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(rows())
    print("wrote countries.csv")
