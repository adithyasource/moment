; Setting metadata
VIAddVersionKey "ProductName" "moment"
VIAddVersionKey "FileDescription" "moment - micro blogging"
VIProductVersion "1.0.0.0"
VIAddVersionKey "FileVersion" "1.0.0"
VIAddVersionKey "ProductVersion" "1.0.0"
VIAddVersionKey "LegalCopyright" "Unlicense"


;--------------------------------


; The name of the installer
Name "moment"

; The setup filename
OutFile "moment v1.0.0 setup.exe"

; The setup icon
Icon "${NSISDIR}\Contrib\Graphics\Icons\nsis1-install.ico"

; The uninstaller icon
UninstallIcon "${NSISDIR}\Contrib\Graphics\Icons\nsis1-uninstall.ico"

; The default installation directory
InstallDir $PROGRAMFILES\moment

; Registry key to check for directory (for writing over the old install)
InstallDirRegKey HKLM "Software\moment" "Install_Dir"


;--------------------------------


; Pages

Page directory
Page components
Page instfiles

UninstPage uninstConfirm
UninstPage instfiles


;--------------------------------


Section "moment - video game library"

  ; Removes option to uncheck the app from installing
  SectionIn RO

  ; Set output path to the installation directory.
  SetOutPath $INSTDIR
  
  ; Put file there (you can add more File lines too)
  File "dist\moment.exe"
  
  ; Write the installation path into the registry
  WriteRegStr HKLM SOFTWARE\moment "Install_Dir" "$INSTDIR"
  
  ; Write the uninstall keys for Windows
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\moment" "DisplayName" "moment"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\moment" "UninstallString" '"$INSTDIR\uninstall.exe"'
  WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\moment" "NoModify" 1
  WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\moment" "NoRepair" 1
  WriteUninstaller "$INSTDIR\uninstall.exe"
  
SectionEnd


;--------------------------------


; Following three sections are shown as checkboxes in the components page
; And their contents are executed if they are checked

Section "desktop shortcut"

    ; Creates a shortcut on the desktop
    CreateShortCut "$DESKTOP\moment.lnk" "$INSTDIR\moment.exe" "" "$INSTDIR\moment.exe" 0

SectionEnd

Section "start menu shortcut"

    ; Creates start menu shortcut
    CreateDirectory "$SMPROGRAMS\moment"
    CreateShortcut "$SMPROGRAMS\moment\Uninstall.lnk" "$INSTDIR\uninstall.exe" "" "$INSTDIR\uninstall.exe" 0
    CreateShortcut "$SMPROGRAMS\moment\moment.lnk" "$INSTDIR\moment.exe" "" "$INSTDIR\moment.exe" 0

SectionEnd


;--------------------------------


; Displays a dialogbox after installation

Function .onInstSuccess
   MessageBox MB_YESNO "launch moment now?" IDYES OpenApp IDNO NoOpen
  OpenApp:
    ExecShell "" '"$INSTDIR\moment.exe"'
    Goto EndDialog
  NoOpen:
  EndDialog:
FunctionEnd


;--------------------------------


; Uninstaller

Section "Uninstall"
  
  ; Remove registry keys
  DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\moment"
  DeleteRegKey HKLM SOFTWARE\moment

  ; Remove files and uninstaller
  Delete $INSTDIR\moment.exe
  Delete $INSTDIR\uninstall.exe

  ; Remove directories used (only deletes empty dirs)
  RMDir "$SMPROGRAMS\moment"
  RMDir "$INSTDIR"

SectionEnd