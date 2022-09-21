# ASSIGNMENT-SUBMISSION

Due to the short time for submission I have choose to work on the following simple python tools which can be used in managing/working with servers: 

Project1: (registryData, winTree)
	These 2 scripts are written for windows platform. 
	As many people might have been familiar with "tree" cmd in linux based operating systems, I have written this script which can do the same in windows.
	And another script to read a specific registry value.

Project2: (revShell)
	I have written this simple python script using which penetration testers/hackers can get a reverse shell in certain conditions.

Project3: (portScanner)
	I have written this simple script which can check for IP's which are accessible in our network. 





Ussage:

1) python winTree.py {location} 
	({location} can be "." for current directory or "/" for root directory and soon...)

2) python registryData.py -e/-q {key}
	({key} can be used as mentioned in this link "https://learn.microsoft.com/en-us/windows-hardware/drivers/install/hklm-system-currentcontrolset-enum-registry-tree")
	
3) python portScanner.py 
	{scans all the ip's}

4) python revShell.py 
	{to get reverse shell my modifying the port and IP accordingly in the script)
