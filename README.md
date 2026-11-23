# world-countries-csv

Every ISO 3166-1 country as one clean CSV: alpha-2, alpha-3, numeric code,
common name, official name, and flag emoji. 249 rows, UTF-8, generated from the
[iso-codes](https://salsa.debian.org/iso-codes-team/iso-codes) database via
[pycountry](https://pypi.org/project/pycountry/).

```csv
alpha_2,alpha_3,numeric,name,official_name,flag
AD,AND,020,Andorra,Principality of Andorra,🇦🇩
```

## Use

```python
import csv
countries = list(csv.DictReader(open("countries.csv", encoding="utf-8")))
```

## Regenerate

```sh
pip install pycountry
python generate.py
```

## License

Data: ISO 3166-1 (public standard, via iso-codes / pycountry). Code: MIT.
