# Postcat

import argparse
import subprocess

SPOOL_DIR = '/var/spool/postfix'
POSTCAT_EXEC = '/usr/local/bin/postcat'
QUEUE_DEFERRED = 'deferred'
QUEUE_ACTIVE = 'active'

queue_names = [QUEUE_ACTIVE, QUEUE_DEFERRED]


def main(argv):
    queue = QUEUE_DEFERRED
    if argv.queue:
        if argv.queue not in queue_names:
            print "{} is not a valid queue name.".format(argv.queue)
            exit(1)
        else:
            queue = argv.queue

    # build the file's full path
    queue_id = argv.queue_id
    first = queue_id[0]
    f = '/'.join([SPOOL_DIR, queue, first, queue_id])
    # build the cmd
    cmd = "{} {}".format(POSTCAT_EXEC, f)

    print subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.read()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Queue data browser', version='1.0')

    parser.add_argument('queue_id', action='store', help='Name of the queue file')
    parser.add_argument('--queue', action='store', help='Queue to browse. Valid names: deferred, active')

    args = parser.parse_args()

    main(args)
