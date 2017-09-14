configuration = {
    "targetURL": "https://www.nordakademie.de/die-nordakademie/einrichtungen-und-service/wohnheime/",
    "cache": {
        "file": "/tmp/accommodationBot",
        "defaults": {
            "hash": "nothing!",
            "mailSent": False,
            "smtpTestSent": False
        }
    },
    "details": [
        {
            "quarter": "Q2",
            "targetYear": "2018",
            "location": "Musterstadt",
            "streetAndCity": "Musterstraße 9, 21502 Musterstadt",
            "name": "Max Mustermann",
            "phone": "00987654321",
            "mail": "<Your Mail>",
            "matrikelnr": "1234567890",
            "footnote": "Sofern möglich würde ich ein Zimmer im E-Gebäude bevorzugen."
        }
    ],
    "mail": {
        "recipient": [],  # TODO Insert actual target mail
        "notificationRecipient": ["til.blechschmidt@gmail.com", "noah.peeters@icloud.com"],
        "subject": "Antrag auf ein Wohnheimzimmer %quarter% %year%",
        "body": "Hallo Frau Conrad,\nim Anhang finden Sie meinen Antrag für ein Zimmer in dem Wohnheim der Nordakademie.\n\nFür den Fall, dass Sie den Anhang nicht öffnen können, habe ich Ihnen hier meine Daten noch einmal zusammengefasst:\n\nName: %name%\nAdresse: %streetAndCity%\nMail: %mail%\nTelefone: %phone%\nMatrikelnummber: %matrikelnr%\nIch würde ein Zimmer der höheren Preisklasse im E-Gebäude bevorzugen.\n\n\n- %name%",
        "server": {
            "hostname": "smtp.gmail.com",
            "port": 587,
            "username": "<Your User Name>",
            "password": "<Your password>"
        }
    }
}
