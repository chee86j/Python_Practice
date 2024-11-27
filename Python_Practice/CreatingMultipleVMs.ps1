# One of the introductory Projects for PowerShell on Microsoft Learn
# PowerShell Script for Creating Multiple Virtual Machines
param (
    [string[]]$Name = @('web', 'app', 'sql'), # Names of the VMs to be created
    [string]$ResourceGroupName,
    [string]$Location = 'eastus'
)

# Get admin credentials
$adminCredential = Get-Credential

# Loop over the array and create VMs
foreach ($vm in $Name) {

    # Output the current VM being created
    Write-Output "Creating VM: $vm"

    $azVmParams = @{
        ResourceGroupName   = $ResourceGroupName
        Name                = $vm
        Credential          = $adminCredential
        Location            = $Location
        Image               = 'Canonical:0001-com-ubuntu-server-jammy:22_04-lts:latest'
        OpenPorts           = 22
        PublicIpAddressName = $vm
    }
    # Create the VM using the parameters defined above
    New-  AzVM @azVmParams
}

# To remove a specific VM, you can use the Remove-AzVM cmdlet with the -Name parameter.
# Remove-AzVM -ResourceGroupName "learn-396623f6-bd3a-4328-b3b9-23475b2e9294" -Name "app" -Force


# # JavaScript Equivalent
# function createVMs({ Name = ['web', 'app', 'sql'], ResourceGroupName, Location = 'eastus' }) {
#     # Simulate getting admin credentials (in real scenarios, this might involve prompts or an external system)
#     let adminCredential = getCredential(); # Placeholder function for credential retrieval

#     # Loop over the array and create VMs
#     Name.forEach(function(vm) {
#         let azVmParams = {
#             ResourceGroupName: ResourceGroupName,
#             Name: vm,
#             Credential: adminCredential,
#             Location: Location,
#             Image: 'Canonical:0001-com-ubuntu-server-jammy:22_04-lts:latest',
#             OpenPorts: 22,
#             PublicIpAddressName: vm
#         };

#         # Assuming a function to create the VM
#         createAzVm(azVmParams); # Placeholder for VM creation function
#     });
# }

# # Example of calling the function
# createVMs({
#     Name: ['web', 'app', 'sql'], # Names of the VMs to be created
#     ResourceGroupName: 'MyResourceGroup',
#     Location: 'eastus'
# });



    
    


