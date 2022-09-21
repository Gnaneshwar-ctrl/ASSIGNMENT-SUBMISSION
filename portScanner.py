import subprocess
import sys 

class Ping:
    def __init__(self):
        self.address = '127.0.0.'

    def main(self):
        for c in range(1,255):
            m = subprocess.Popen(
                "ping -c 1 {0}{1}".format(self.address,c),
                shell = True,stderr=subprocess.PIPE
            )

            while True:
                out = m.stderr.read(1)
                if out :
                    sys.stdout.write(out)
                    sys.stdout.flush()
		

if __name__ == "__main__":
    scan = Ping()
    scan.main()
