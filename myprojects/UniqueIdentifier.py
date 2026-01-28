import os, subprocess, json
destination = input("File or folder path: ")
if os.path.exists(destination):
    acl = "(Get-Acl -LiteralPath '{}').Access | Select-Object IdentityReference, FileSystemRights, AccessControlType | ConvertTo-Json".format(destination)
    print("\n--- Security Permissions ---\n")
    print(json.load(subprocess.run(["powershell", "-Command", acl]).stdout))
else:
    print("File not found.")