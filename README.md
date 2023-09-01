# OurAirports JSON

> Updated JSON version of the OurAirports Database.

## Usage
### Typescript
```ts
import * as airports from 'ourairports-json'
```

### Javascript
```js
const airports = require('airport-data')
```

## Format

Airports is an array of airports as follows:

```json
{
    "id": "4461",
    "ident": "LPPT",
    "type": "large_airport",
    "name": "Humberto Delgado Airport (Lisbon Portela Airport)",
    "latitude_deg": "38.7813",
    "longitude_deg": "-9.13592",
    "elevation_ft": "374",
    "continent": "EU",
    "iso_country": "PT",
    "iso_region": "PT-11",
    "municipality": "Lisbon",
    "scheduled_service": "yes",
    "gps_code": "LPPT",
    "iata_code": "LIS",
    "local_code": "",
    "home_link": "http://www.ana.pt/en-US/Aeroportos/lisboa/Lisboa/Pages/HomeLisboa.aspx",
    "wikipedia_link": "https://en.wikipedia.org/wiki/Lisbon_Portela_Airport",
    "keywords": "Lisboa"
}
```

## Updating

Running the updater will update the `./dist/airports.json` with the latest information in the [OurAirports database](https://davidmegginson.github.io/ourairports-data/airports.csv)

```shell
pip install -r requirements.txt
python3 updater.py
```


## Inspiration

Was inspired by [this outdated package](https://www.npmjs.com/package/airport-data)