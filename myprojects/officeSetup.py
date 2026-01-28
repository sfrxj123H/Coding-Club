import subprocess, os, time, shlex, sys

# Default configuration XML content (Office 2019 Standard, Visio, Project)
office_2019_standard = '''
<Configuration ID="d10b7777-56a1-4a39-bc63-1d2e8f1a93b0">
  <Add OfficeClientEdition="64" Channel="PerpetualVL2019">
    <Product ID="Standard2019Volume" PIDKEY="6NWWJ-YQWMR-QKGCB-6TMB3-9D9HK">
      <Language ID="en-us" />
    </Product>
    <Product ID="VisioStd2019Volume" PIDKEY="7TQNQ-K3YQQ-3PFH7-CCPPM-X4VQ2">
      <Language ID="en-us" />
    </Product>
    <Product ID="ProjectStd2019Volume" PIDKEY="C4F7P-NCP8C-6CQPT-MQHV9-JXD2M">
      <Language ID="en-us" />
    </Product>
  </Add>
  <Property Name="SharedComputerLicensing" Value="0" />
  <Property Name="FORCEAPPSHUTDOWN" Value="FALSE" />
  <Property Name="DeviceBasedLicensing" Value="0" />
  <Property Name="SCLCacheOverride" Value="0" />
  <Property Name="AUTOACTIVATE" Value="1" />
  <Updates Enabled="TRUE" />
  <RemoveMSI />
  <AppSettings>
    <User Key="software\microsoft\office\16.0\excel\options" Name="defaultformat" Value="51" Type="REG_DWORD" App="excel16" Id="L_SaveExcelfilesas" />
    <User Key="software\microsoft\office\16.0\powerpoint\options" Name="defaultformat" Value="27" Type="REG_DWORD" App="ppt16" Id="L_SavePowerPointfilesas" />
    <User Key="software\microsoft\office\16.0\word\options" Name="defaultformat" Value="" Type="REG_SZ" App="word16" Id="L_SaveWordfilesas" />
  </AppSettings>
</Configuration>
'''
# Default configuration XML content (Office 2024 LTSC Professional Plus, Visio, Project, Proofing Tools)
office_2024_LTSC_ProfessionalPlus = '''
<Configuration ID="fb504758-de61-4796-869d-24990044ce27">
  <Add OfficeClientEdition="64" Channel="PerpetualVL2024">
    <Product ID="ProPlus2024Volume" PIDKEY="XJ2XN-FW8RK-P4HMP-DKDBV-GCVGB">
      <Language ID="en-us" />
      <Language ID="MatchOS" />
    </Product>
    <Product ID="VisioPro2024Volume" PIDKEY="B7TN8-FJ8V3-7QYCP-HQPMV-YY89G">
      <Language ID="en-us" />
      <Language ID="MatchOS" />
    </Product>
    <Product ID="ProjectPro2024Volume" PIDKEY="FQQ23-N4YCY-73HQ3-FM9WC-76HF4">
      <Language ID="en-us" />
      <Language ID="MatchOS" />
    </Product>
    <Product ID="ProofingTools">
      <Language ID="vi-vn" />
    </Product>
  </Add>
  <Property Name="SharedComputerLicensing" Value="0" />
  <Property Name="FORCEAPPSHUTDOWN" Value="FALSE" />
  <Property Name="DeviceBasedLicensing" Value="0" />
  <Property Name="SCLCacheOverride" Value="0" />
  <Property Name="AUTOACTIVATE" Value="1" />
  <Updates Enabled="TRUE" />
  <AppSettings>
    <User Key="software\microsoft\office\16.0\excel\options" Name="defaultformat" Value="51" Type="REG_DWORD" App="excel16" Id="L_SaveExcelfilesas" />
    <User Key="software\microsoft\office\16.0\powerpoint\options" Name="defaultformat" Value="27" Type="REG_DWORD" App="ppt16" Id="L_SavePowerPointfilesas" />
    <User Key="software\microsoft\office\16.0\word\options" Name="defaultformat" Value="" Type="REG_SZ" App="word16" Id="L_SaveWordfilesas" />
  </AppSettings>
</Configuration>
'''

#Define function to get full path
def fullPath(path):
    if os.path.isabs(path) and os.path.exists(path):
        return path
    
    if getattr(sys, 'frozen', False):  # Running in PyInstaller exe
        base_path = os.path.dirname(sys.executable)
    else:  # Running as plain Python
        base_path = os.path.dirname(os.path.abspath(__file__))
    
    return os.path.join(base_path, path)

# Loopers
complete = False
retry = False

print("--- Office SETUP ---\n")
print("This script will help you install Microsoft Office using the Office Deployment Tool.")
print("You can download the deployment tool from: https://www.microsoft.com/en-us/download/details.aspx?id=49117")
print("If you don't provide a configuration file, a default one for Office 2019 Standard will be created.")
print("You can customize the configuration XML file with Office Customization Tool: https://config.office.com/deploymentsettings")
print("More info: https://learn.microsoft.com/en-us/microsoft-365-apps/deploy/deployment-guide-microsoft-365-apps")
print("Note: This script will not activate Office. You need a valid license key for activation.\n")

while not complete: #Let the user retry if they made a mistake
  #Check for setup.exe in current directory
  if os.path.exists(fullPath("setup.exe")) and retry == False:
      setupDestination = fullPath("setup.exe")
      print("\nFound setup.exe in current directory.")
  else:
      print("\nSelecting deployment tool (Download deployment tool: https://www.microsoft.com/en-us/download/details.aspx?id=49117)")
      setupDestination = fullPath(input("Deployment tool application path (default as 'setup.exe'): "))
      if setupDestination == fullPath(""):
        print("No path provided, choosing 'setup.exe' as deployment tool file.")
        setupDestination = fullPath("setup.exe")
      if not os.path.exists(setupDestination):
        if os.path.exists(setupDestination + ".exe"): #Check if user forgot to add .exe
            setupDestination += ".exe"
            print(f"Found {os.path.basename(setupDestination)} in specified path.")
        else:
          print("File not found, please try again.")
          retry = True
          continue
      else:
        print(f"Found {os.path.basename(setupDestination)} in specified path.")

  #Check for configuration.xml in current directory
  if os.path.exists(fullPath("configuration.xml")) and retry == False:
      configDestination = fullPath("configuration.xml")
      print("\nFound configuration.xml in current directory.")
  elif os.path.exists(fullPath("Configuration.xml")) and retry == False:
      configDestination = fullPath("Configuration.xml")
      print("\nFound Configuration.xml in current directory.")
  else:
      print("\nSelecting configuration (Press ENTER to use default configuration for Office 2019 Standard)")
      configDestination = fullPath(input("Configuration file path (default as 'configuration.xml'): "))
      if configDestination == fullPath("2024") or configDestination == fullPath("Office 2024") or configDestination == fullPath("office 2024"):
          configDestination = fullPath("Office 2024 LTSC Professional Plus.xml")
          avoidOverwrite = 0
          while os.path.exists(configDestination): #Avoid overwriting existing files
              configDestination = fullPath(f"Office 2024 LTSC Professional Plus {avoidOverwrite}.xml")
              avoidOverwrite += 1
          with open(configDestination, "w") as f:
              f.write(office_2024_LTSC_ProfessionalPlus)
              f.close()
              print(f"Created Office 2024 LTSC Professional Plus configuration file at => {os.path.basename(configDestination)}")
      elif configDestination == fullPath("") or not os.path.exists(configDestination):
          if configDestination != fullPath("") and os.path.exists(configDestination + ".xml"): #Check if user forgot to add .xml
              configDestination += ".xml"
              print(f"Found {os.path.basename(configDestination)} in specified path.")
          else:
            print("No path provided or file not found, creating default configuration file for Office 2019 Standard.")
            configDestination = fullPath("Office 2019 Standard.xml")
            avoidOverwrite = 0
            while os.path.exists(configDestination): #Avoid overwriting existing files
                configDestination = fullPath(f"Office 2019 Standard {avoidOverwrite}.xml")
                avoidOverwrite += 1
            with open(configDestination, "w") as f:
                f.write(office_2019_standard)
                f.close()
                print(f"Created Office 2019 Standard configuration file at => {os.path.basename(configDestination)}")
      else:
        print(f"Found {os.path.basename(configDestination)} in specified path.")

  #Run setup command
  cmd = [setupDestination, "/configure", configDestination]
  confirm = input("\nDo you want to run command: " + " ".join(shlex.quote(arg) for arg in cmd) + "\n[Y/N]: ")
  if confirm.lower() == 'y' or confirm == '':
    complete = True
    try:
      subprocess.run([setupDestination, "/configure", configDestination], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running setup: {e}, exiting in 3 seconds.")
        time.sleep(3)
        exit(1)
    finally:
      complete = True
  elif confirm.lower() == 'n':
    print("\n--- RETRYING ---\n")
    retry = True
  else:
    print("Invalid input, exiting in 3 seconds.")
    time.sleep(3)
    exit(2)