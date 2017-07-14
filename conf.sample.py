configuration = {
    # "targetURL": "https://www.nordakademie.de/die-nordakademie/einrichtungen-und-service/wohnheime/",
    "targetURL": "http://localhost:8000/Wohnheime.html",
    "cache": {
        "file": "/tmp/accommodationBot",
        "defaults": {
            "hash": "nothing!"
        }
    },
    "mail": {
        "recipient": ["noah.peeters@icloud.com"],
        "subject": "Hello world!",
        "body": "I AM A POTATO!!!! And different...",
        "server": {
            "hostname": "smtp.gmail.com",
            "port": 587,
            "username": "someUser",
            "password": "somePassword"
        }
    }
}