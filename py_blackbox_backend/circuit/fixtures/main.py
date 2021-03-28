import json


def main():
    template = {
        "model": "circuit.circuit",
        "pk": 0,
        "fields": {
            "name": "",
            "keyname": ""
        }
    }

    circuits = [
        ("Circuit De Barcelona - Catalunya", "barcelona"),
        ("Brands Hatch Circuit", "brands_hatch"),
        ("Hungaroring", "hungaroring"),
        ("Misano World Circuit", "misano"),
        ("Monza Circuit", "monza"),
        ("Nurburgring", "nurburgring"),
        ("Paul Ricard", "paul_ricard"),
        ("Silverstone", "silverstone"),
        ("Circuit De Spa-Francorchamps", "spa"),
        ("Circuit Zandvoort", "zandvoort"),
        ("Circuit Zolder", "zolder"),
        ("Kyalami Grand Prix Circuit", "kylami"),
        ("Suzuka Circuit", "suzuka"),
        ("Weathertech®️ Raceway Laguna Seca", "laguna_seca"),
        ("Mount Panorama Circuit", "bathurst"),
        ("Autodromo Internazionale Enzo e Dino Ferrari – Imola", "imola"),
        ("Donington Park Circuit", "donington_park"),
        ("Oulton Park Circuit", "oulton_park"),
        ("Snetterton Circuit", "snetterton"),
    ]
    entries = []
    counter = 1
    for name, keyname in circuits:
        entry = {
            "model": "circuit.circuit",
            "pk": counter,
            "fields": {
                "name": name,
                "keyname": keyname
            }
        }
        entries.append(entry)
        counter += 1
    print(json.dumps(entries))


if __name__ == "__main__":
    main()
