#save contents of https://management.azure.com/subscriptions/{{subscriptionId}}/resources?api-version=2020-09-01 to data.json

import json,re
  
# Opening JSON file
f = open('data.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)

types = {
	"Microsoft.Compute/disks":"azurerm_managed_disk",
"Microsoft.Compute/images":"azurerm_image",
"Microsoft.Compute/snapshots":"azurerm_snapshot",
"Microsoft.Compute/sshPublicKeys":"azurerm_ssh_public_key",
"Microsoft.Compute/virtualMachines":"azurerm_linux_virtual_machine",
"Microsoft.Network/networkInterfaces":"azurerm_network_interface",
"Microsoft.Network/networkSecurityGroups":"azurerm_network_security_group",
"Microsoft.Network/networkWatchers":"azurerm_network_watcher",
"Microsoft.Network/publicIPAddresses":"azurerm_public_ip",
"Microsoft.Network/virtualNetworks":"azurerm_virtual_network",
"Microsoft.Resources/templateSpecs":"",
"Microsoft.Resources/templateSpecs/versions":"DONT USE ME",
"Microsoft.Storage/storageAccounts":"azurerm_storage_account"

}

# Iterating through the json
# list
for i in data['value']:
	myid=i["id"]
	oname=i["name"]
	myname=re.sub("^5g", "_5g", oname)
	myname=re.sub("^5G", "_5g", myname)
	org=i["id"].split("/")[4]
	myrg=re.sub("^5g", "_5g", org)
	mytype=i["type"].replace(i["type"],types[i["type"]])
	#mystring = 'resource "'+mytype+'" "'+myname+'"{\n name = "'+oname+'"\nresource_group_name = azurerm_resource_group.'+myrg+'\n}\n'
	#print(mystring)
	mystring = "terraform import "+mytype+"."+myname+" "+myid
	print(mystring) 
