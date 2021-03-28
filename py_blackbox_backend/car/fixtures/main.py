import json


def main():

    cars = [
        ("Aston Martin Vantage V12 GT3 2013", "amr_v12_vantage_gt3"),
        ("Audi R8 LMS 2015", "audi_r8_lms"),
        ("Bentley Continental GT3 2015", "bentley_continental_gt3_2016"),
        ("Bentley Continental GT3 2018", "bentley_continental_gt3_2018"),
        ("BMW M6 GT3 2017", "bmw_m6_gt3"),
        ("Jaguar G3 2012", "jaguar_g3"),
        ("Ferrari 488 GT3 2018", "ferrari_488_gt3"),
        ("Honda NSX GT3 2017", "honda_nsx_gt3"),
        ("Lamborghini Gallardo G3 Reiter 2017", "lamborghini_gallardo_rex"),
        ("Lamborghini Huracan GT3 2015", "lamborghini_huracan_gt3"),
        ("Lamborghini Huracan ST 2015", "lamborghini_huracan_st"),
        ("Lexus RCF GT3 2016", "lexus_rc_f_gt3"),
        ("McLaren 650S GT3 2015", "mclaren_650s_gt3"),
        ("Mercedes AMG GT3 2015", "mercedes_amg_gt3"),
        ("Nissan GTR Nismo GT3 2015", "nissan_gt_r_gt3_2017"),
        ("Nissan GTR Nismo GT3 2018", "nissan_gt_r_gt3_2018"),
        ("Porsche 991 GT3 R 2018", "porsche_991_gt3_r"),
        ("Porsche9 91 II GT3 Cup 2017", "porsche_991ii_gt3_cup"),
        ("Aston Martin V8 Vantage GT3 2019", "amr_v8_vantage_gt3"),
        ("Audi R8 LMS Evo 2019", "audi_r8_lms_evo"),
        ("Honda NSX GT3 Evo 2019", "honda_nsx_gt3_evo"),
        ("Lamborghini Huracan GT3 EVO 2019", "lamborghini_huracan_gt3_evo"),
        ("McLaren 720S GT3 2019", "mclaren_720s_gt3"),
        ("Porsche 911 II GT3 R 2019", "porsche_991ii_gt3_r"),
        ("Ferrari 488 GT3 Evo 2020", "ferrari_488_gt3_evo"),
        ("Mercedes AMG GT3 Evo 2020", "mercedes_amg_gt3_evo"),
        ("Alpine A110 GT4 2018", "alpine_a110_gt4"),
        ("Aston Martin Vantage AMR GT4 2018", "amr_v8_vantage_gt4"),
        ("Audi R8 LMS GT4 2016", "audi_r8_gt4"),
        ("BMW M4 GT42 018", "bmw_m4_gt4"),
        ("Chevrolet Camaro GT4 R 2017", "chevrolet_camaro_gt4r"),
        ("Ginetta G55 GT4 2012", "ginetta_g55_gt4"),
        ("Ktm Xbow GT4 2016", "ktm_xbow_gt4"),
        ("Maserati Gran Turismo MC GT4 2016", "maserati_mc_gt4"),
        ("McLaren 570s GT4 2016", "mclaren_570s_gt4"),
        ("Mercedes AMG GT4 2016", "mercedes_amg_gt4"),
        ("Porsche 718 Cayman GT4 MR 2019", "porsche_718_cayman_gt4_mr"),
    ]
    entries = []
    counter = 1
    for name, keyname in cars:
        entry = {
            "model": "car.car",
            "pk": counter,
            "fields": {
                "name": name,
                "keyname": keyname
            }
        }
        entries.append(entry)
        counter += 1

    with open("./cars.json", 'w') as f:
        json.dump(entries, f)


if __name__ == "__main__":
    main()
