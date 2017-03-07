import sys, getopt

from keystone.getAuth import *
import glanceclient.v2.client as glclient

def createImage(argv):
    infile =''
    outfile=''
    pub = 'public'

    try:
        opts, args = getopt.getopt(argv, "hi:o:p", ["infile=","outfile="])
    except getopt.GetoptError:
        print '%s -i <inputfile> -o <outputfile>' % sys.argv[0]
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print '%s -i <inputfile> -o <outputfile>' % sys.argv[0]
            sys.exit()
        elif opt in ('-i', '--ifile'):
            infile = arg
        elif opt in ('-o', '--ofile'):
            outfile = arg
        elif opt in ('-p', '--public'):
            pub = arg

    print ' Input file is', infile
    print 'Output file is', outfile

    sess = GetSession()
    glance = glclient.Client(session=sess)
    with open(infile) as fimage:
        image = glance.images.create(name=outfile, visibility=pub, disk_format='qcow2',
                                    container_format='bare', data=unicode(fimage)
                                    )


if __name__ == '__main__':
    createImage(sys.argv[1:])
