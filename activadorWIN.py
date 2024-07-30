import platform,os,time


def comando(codigo,version,windows):
    print(f'windows:{windows}, version:{version}')
    os.system(f'slmgr /ipk {codigo}')
    time.sleep(10)
    os.system('slmgr /skms kms.digiboy.ir')
    time.sleep(10)
    os.system('slmgr /ato')
    

if platform.system() == 'Windows':
    try:
        version= platform.win32_edition()
        if version == 'Professional':
            codigo=  'W269N-WFGWX-YVC9B-4J6C9-T83GX'
            
        elif version == 'Home':

            codigo = 'TX9XD-98N7V-6WMQ6-BX7FG-H8Q99'
        elif version == 'Home N':

            codigo = 'TX9XD-98N7V-6WMQ6-BX7FG-H8Q99'
            
        elif version == 'Professional N':
            codigo = '3KHY7-WNT83-DGQKR-F7HPR-844BM'
        elif version == 'Enterprise':

            codigo = 'NPPR9-FWDCX-D2C8J-H872K-2YT43'

        elif version == 'Enterprise N':

            codigo = 'DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4'

        elif version == 'Education':

            codigo = 'NW6C2-QMPVW-D7KKK-3GKT6-VCFB2'
        elif version == 'Education  N':

            codigo = '2WH4N-8QGBV-H22JP-CT43Q-MDWWJ'
        elif version == 'Enterprise 2015 LTSB':

            codigo = 'WNMTR-4C88C-JK8YV-HQ7T2-76DF9'

        elif version == 'Enterprise 2015 LTSB N':

            codigo = '2F77B-TNFGY-69QQF-B8YKP-D69TJ'

        elif version == 'Home Single Language':

            codigo = '7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH'
        elif version == 'Home Country Specific':
            codigo = 'PVMJN-6DFY6-9CCP6-7BKTT-D3WVR'
        else:
            print('no se pudo activar')

        comando(codigo,version,platform.system())
    except:
        print('error')