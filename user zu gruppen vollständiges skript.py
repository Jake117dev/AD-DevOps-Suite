function Add-UserToGroup {
    param (
        [Parameter(Mandatory=$true)]
        [string[]]$groups,

        [Parameter(Mandatory=$true)]
        [string[]]$users
    )

    foreach ($user in $users) {
        Write-Output "Processing user: $user"
        $splitName = $user.Split(',')
        $lastname = $splitName[0].Trim()
        $firstname = $splitName[1].Trim()

        $samAccountName = $lastname.Substring(0, 2) + $firstname.Substring(0, 2)
        Write-Output "Initial SAM Account Name: $samAccountName"

        if (!(Get-ADUser -Filter { SamAccountName -eq $samAccountName })) {
            Write-Output "User $samAccountName does not exist, skipping to next user"
            continue
        }

        Write-Output "Final SAM Account Name: $samAccountName"

        foreach ($group in $groups) {
            Write-Output "Attempting to add $samAccountName to $group"
            try {
                Add-ADGroupMember -Identity $group -Members $samAccountName
                Write-Output "Successfully added $samAccountName to $group"
            }
            catch {
                Write-Output "Failed to add $samAccountName to $group"
            }
        }
    }
}

# Usage:
Add-UserToGroup -groups ""

