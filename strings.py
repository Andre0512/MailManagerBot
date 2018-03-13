CREATE='Adresse erstellen'
MAIL_NAME = 'Welche Adresse soll angelegt werden?'
MESSAGE="""*Erstellte Adressen:*
{ADDRESSES}

*IMAP*
Server: `{SERVER}`
Port: `993`
SSL/TLS: `Ja, aber kein STARTTLS`
Benutzername: `{NAME}@{MAIL}`
Passwort: `{PASSWORD}`

*POP3* (Besser IMAP verwenden)
Server: `{SERVER}`
Port: `995`
SSL/TLS: `Ja, aber kein STARTTLS`
Benutzername: `{NAME}@{MAIL}`
Passwort: `{PASSWORD}`

*SMTP*
Server: `{SERVER}`
Port: `587`
SSL/TLS: `STARTTLS`
Benutzername: `{NAME}@{MAIL}`
Passwort: `{PASSWORD}`

*Webmail*
URL: {WEBMAIL}
Benutzername: `{NAME}@{MAIL}`
Passwort: `{PASSWORD}`
"""
