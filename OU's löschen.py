Get-ADOrganizationalUnit -Filter 'Name -like "OrganizationUnit" | Set-ADOrganizationalUnit -ProtectedFromAccidentalDeletion $false


Remove-ADOrganizationalUnit -Identity "OrganisationUnit"






# Liste der OUs, die gelöscht werden sollen. Fügen Sie weitere Pfade hinzu oder entfernen Sie diese, wie benötigt.
$OUsToRemove = @(
    "OU=,OU=,DC=,DC=",
    "OU=,OU=,DC=,DC=",
    "OU=,OU=,DC=,DC=",
    "OU=,OU=,DC=,DC=",
    "OU=,OU=,DC=,DC="
)

# Für jede OU in der Liste...
foreach ($OU in $OUsToRemove) {
    # Versuchen Sie, den Schutz vor versehentlichem Löschen für die OU aufzuheben.
    try {
        Get-ADOrganizationalUnit -Identity $OU | Set-ADOrganizationalUnit -ProtectedFromAccidentalDeletion $false
        Write-Output "Schutz vor versehentlichem Löschen für OU $OU aufgehoben."
    } catch {
        Write-Error "Fehler beim Aufheben des Schutzes vor versehentlichem Löschen für OU $OU."
        continue
    }

    # Versuchen Sie, die OU zu löschen.
    try {
        Remove-ADOrganizationalUnit -Identity $OU -Confirm:$false
        Write-Output "OU $OU gelöscht."
    } catch {
        Write-Error "Fehler beim Löschen der OU $OU."
    }
}
