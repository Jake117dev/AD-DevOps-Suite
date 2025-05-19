# Importieren des Active Directory Moduls
Import-Module ActiveDirectory

# Legen Sie den Pfad zur Organisationseinheit (OU) fest, in der die Benutzer erstellt werden sollen
$ouPath = ""

# Legen Sie die vollständigen Namen der Benutzer fest, die erstellt werden sollen
$usernames = @("")

# Durchlaufen Sie jeden vollständigen Namen in der Liste
foreach ($fullname in $usernames) {
    # Teilen Sie den vollständigen Namen in Vor- und Nachnamen auf
    $splitName = $fullname.Split(',')
    $lastname = $splitName[0].Trim()
    $firstname = $splitName[1].Trim()

    # Option 1: Erzeugen Sie den SamAccountName durch Verbindung von Vor- und Nachname
    # $samAccountName = "$lastname.$firstname"

    # Option 2: Erzeugen Sie den SamAccountName durch Verwendung der ersten beiden Buchstaben von Vor- und Nachname
    # Hinweis: Bitte nur eine der beiden Optionen auswählen und die andere auskommentieren
    $samAccountName = $lastname.Substring(0, 2) + $firstname.Substring(0, 2)

    # Erstellen Sie den neuen Benutzer
    # Wichtige Hinweise: 
    # - Ersetzen Sie "yourdomain.com" durch Ihre tatsächliche Domain
    # - Aktualisieren Sie das Passwort auf ein sicheres Passwort oder implementieren Sie eine Methode zur Generierung sicherer Passwörter
    New-ADUser -SamAccountName $samAccountName -UserPrincipalName "$samAccountName@yourdomain.com" -Name $fullname -GivenName $firstname -Surname $lastname -Enabled $True -Path $ouPath -AccountPassword (ConvertTo-SecureString -AsPlainText "heli1+" -Force) -PassThru 
}
