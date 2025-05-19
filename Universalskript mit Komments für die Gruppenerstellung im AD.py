# Hier geben Sie den Namen Ihrer Root-Organisationseinheit (OU) an.
$rootOU = "OU=IhreRootOU,DC=IhrDomainController,DC=IhrDomain"

# Hier können Sie eine Liste der OUs angeben, die ausgeschlossen werden sollen. 
# Fügen Sie einfach weitere OUs hinzu, die Sie ausschließen möchten.
$excludedOUs = @("OU=AusgeschlosseneOU1,DC=IhrDomainController,DC=IhrDomain", "OU=AusgeschlosseneOU2,DC=IhrDomainController,DC=IhrDomain")

# Diese Funktion erstellt den Namen der Gruppe basierend auf dem Namen der OU und der Berechtigungsart.
function createGroupName($ouName, $permission) {
    $groupName = "IhrPräfix_" + $ouName.Replace(" ","").Replace("/","_").Replace("-","_") + "_" + $permission
    return $groupName
}

# Diese Funktion überprüft, ob eine OU in der Liste der ausgeschlossenen OUs enthalten ist.
function isExcluded($ouDN) {
    return $excludedOUs -icontains $ouDN
}

# Dieser Teil des Skripts durchläuft alle OUs unter der angegebenen Root-OU.
Get-ADOrganizationalUnit -Filter * -SearchBase $rootOU | ForEach-Object {
    # Es überprüft, ob die aktuelle OU nicht in der Liste der ausgeschlossenen OUs enthalten ist.
    if (-not (isExcluded $_.DistinguishedName)) {
        # Es erstellt die Namen der Lese- und Schreibgruppen.
        $readGroupName = createGroupName $_.Name "lesen"
        $writeGroupName = createGroupName $_.Name "lesen_schreiben"

        # Versucht, die Lese-Gruppe zu erstellen.
        try {
            New-ADGroup -Name $readGroupName -Path $_.DistinguishedName -GroupCategory Security -GroupScope DomainLocal -ErrorAction Stop
            Write-Host "Successfully created group $readGroupName in ${_}"
        } catch {
            Write-Host "Error creating group $readGroupName in ${_}: ${_}"
        }

        # Versucht, die Schreib-Gruppe zu erstellen.
        try {
            New-ADGroup -Name $writeGroupName -Path $_.DistinguishedName -GroupCategory Security -GroupScope DomainLocal -ErrorAction Stop
            Write-Host "Successfully created group $writeGroupName in ${_}"
        } catch {
            Write-Host "Error creating group $writeGroupName in ${_}: ${_}"
        }
    }
}


# Vergessen Sie nicht, Ihre spezifischen Werte für $rootOU, $excludedOUs und den Präfix in der createGroupName Funktion anzupassen. Dieses Skript sollte auf jedem System funktionieren, das PowerShell und Active Directory hat. Es ist wichtig, dass Sie Ihre spezifischen OU- und DC-Namen korrekt eintragen, um sicherzustellen, dass das Skript korrekt funktioniert.




