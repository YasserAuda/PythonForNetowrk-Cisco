
import sys

def main():

    print('Python version {}.{}.{}'.format(*sys.version_info))
    print(sys.platform)
    
    import datetime
    now = datetime.datetime.now()
    print(now)
    print(now.year, now.year, now.month, now.minute, now.second, now.microsecond)

if __name__ == "__main__": main()

