# Importieren des Active Directory Moduls
Import-Module ActiveDirectory

# Definieren Sie hier die OU (Organizational Unit), in der sich die zu ändernden Gruppen befinden
$ou = "OU=Ihre OU,DC=Ihre Domäne,DC=Ihre TLD"

# Definieren Sie hier den Gruppenbereich, zu dem die Gruppen geändert werden sollen (Universal, Global oder DomainLocal)
$newGroupScope = "Universal"

# Holen Sie alle Gruppen in der definierten OU
$groups = Get-ADGroup -Filter * -SearchBase $ou

# Iterieren Sie durch jede Gruppe
foreach ($group in $groups) {
    # Ausgeben des Gruppennamens und der Distinguished Name
    Write-Output "Gruppe: $($group.Name) ( $($group.DistinguishedName) )"
    
    # Abfragen, ob die Gruppe geändert werden soll
    $response = Read-Host "Soll diese Gruppe geändert werden? (J)a / (N)ein / Für (A)lle / a(B)brechen"

    # Behandeln Sie die Antwort
    switch ($response) {
        # Bei "J", ändern Sie diese Gruppe
        "J" { 
            Set-ADGroup -Identity $group -GroupScope $newGroupScope -WhatIf
        }
        # Bei "N", überspringen Sie diese Gruppe
        "N" { 
            continue 
        }
        # Bei "A", ändern Sie alle Gruppen und beenden Sie das Skript
        "A" {
            foreach ($group in $groups) {
                Set-ADGroup -Identity $group -GroupScope $newGroupScope -WhatIf
            }
            return
        }
        # Bei "B", beenden Sie das Skript
        "B" { 
            return 
        }
        # Bei ungültiger Eingabe, fragen Sie erneut nach
        default {
            Write-Output "Ungültige Eingabe. Bitte antworten Sie mit 'J', 'N', 'A' oder 'B'."
            continue
        }
    }
}
# -whatif sollte bei der anwendung entfernt werden, -whatif stellt ein was-wäre-wenn-fall dar und führt keinen der kommandos aus!
