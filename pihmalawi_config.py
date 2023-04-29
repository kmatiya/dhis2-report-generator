config = {
    "base_file_path": "./DHIS2 report",
    "endpoints": [
        {
            "base": "https://neno.pih-emr.org/dhis/api",
            "username": "",
            "password": "",
            "org_units": [
                {
                    "id": "Rmh4wKR794k",
                    "name": "Neno District Hospital"
                }
            ],
            "periods": [
                {
                    "period":"",
                    "reporting_format": ""
                }
            ]
        },
    ],
    "reports": [
        {
            "resource": "pihmalawi/report/moh-regimen-switch",
            "name": "Regimen Switch Report",
            "assigned_to": "Bright",
        },
    ]
}
