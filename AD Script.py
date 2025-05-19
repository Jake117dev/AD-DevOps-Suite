# Verzeichnisstruktur
$RootFolder = "C:\Data"
$SubFolder = "Sales","Marketing","IT"

# Active Directory
$ADServer = "DC1.contoso.com"
$ADUser = "Administrator"
$ADPassword = "Passw0rd"
$ADBaseDN = "OU=Departments,DC=contoso,DC=com"

# Active Directory-Verbindung herstellen
$ADCredential = New-Object System.Management.Automation.PSCredential($ADUser, ($ADPassword | ConvertTo-SecureString -AsPlainText -Force))
$ADSession = New-PSSession -ComputerName $ADServer -Credential $ADCredential
Import-Module ActiveDirectory -Session $ADSession

# Ordnerstruktur erstellen
ForEach ($Folder in $SubFolder)
{
    $FolderPath = "$RootFolder\$Folder"
    New-Item -ItemType Directory -Path $FolderPath -Force
}

# Ordnerstruktur in Active Directory importieren
ForEach ($Folder in $SubFolder)
{
    $FolderPath = "$RootFolder\$Folder"
    $FolderName = $Folder.Substring($Folder.LastIndexOf("\")+1)

    $NewOU = New-ADOrganizationalUnit -Name $FolderName -Path $ADBaseDN
    $NewFolder = New-Item -ItemType Directory -Path $FolderPath -Force
    Set-ADObject -Identity $NewOU -Replace @{ Description = $FolderPath }
    $NewFolder | Set-ADObject -Add @{ Description = $NewOU.DistinguishedName }
}

# Active Directory-Verbindung trennen
Remove-Module ActiveDirectory -Session $ADSession
Remove-PSSession $ADSession

In diesem Beispiel-Skript wird eine Verzeichnisstruktur erstellt und dann in Active Directory importiert. Um das Skript an Ihre spezifischen Anforderungen anzupassen, ändern Sie einfach die Werte der Variablen $RootFolder, $SubFolder, $ADServer, $ADUser, $ADPassword und $ADBaseDN entsprechend Ihrer Umgebung.
