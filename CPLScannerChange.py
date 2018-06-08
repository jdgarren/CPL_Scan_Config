configXP = 'C:\Documents and Settings\All Users\Application Data\FCPA\SFTPUpload\SFTP.ini'
config7 = 'C:\ProgramData\FCPA\SFTPUpload\SFTP.ini'
print('Preparing to update SFTP config')
print('If there are any Access Denied errors, run this as an administrator.')

try:
    open(configXP)
except FileNotFoundError:
    pass
else:
    f = open(configXP, 'w')
    f.write('scflzzsftp.dcf.state.fl.us\n')
    f.write('adi-prod\n')
    f.write('Ve7XC6AlZxZqnsofnr4vXdPT1kb2YKA+vksOhaWvYho=\n')
    f.write('adi_cps_prod\n')
    f.close()
    print('Updated Windows XP Config file!')


try:
    open(config7)
except FileNotFoundError:
    print('Config file not found.')
else:
    f = open(config7, 'w')
    f.write('scflzzsftp.dcf.state.fl.us\n')
    f.write('adi-prod\n')
    f.write('Ve7XC6AlZxZqnsofnr4vXdPT1kb2YKA+vksOhaWvYho=\n')
    f.write('adi_cps_prod\n')
    f.close()
    print('Updated Windows 7+ Config file!')


input("Press enter to close program")

