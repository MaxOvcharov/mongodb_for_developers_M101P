"""
This script will check that a replica set with three nodes 
  is running on a host command line arg parsing to make folks 
  happy who want to run at mongolabs or mongohq this functions 
  uses global vars to communicate. forgive me.
"""


import pymongo
import sys
import getopt
import pprint

connection = None
db = None
mongostr = 'mongodb://localhost:27017'
db_name = 'admin'
rs_name = 'm101'


def arg_parsing(argv):

    global webhost
    global mongostr
    global db_name

    try:
        opts, args = getopt.getopt(argv, '-p:-m:-d:')
    except getopt.GetoptError:
        print('usage validate.py -m mongoConnectString')
        print(f'\tmongoConnectionString default to {mongostr}')
        print(f'\tdatabaseName defaults to {db_name}')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('usage validate.py -m mongoConnectString -d databaseName')
            sys.exit(2)
        elif opt == '-m':
            mongostr = arg
            print(f'Overriding MongoDB connection string to be {mongostr}')
        elif opt == '-d':
            db_name = arg
            print(f'Overriding MongoDB database to be {db_name}')


def get_rs_status():
    """ Gets the replica set status """
    db = connection.admin
    rs = db.command('replSetGetStatus')
    return rs


def get_rs_configuration():
    """ Gets the replica state config """
    db = connection.local
    coll = db.system.replset
    return coll.find_one()


def repl_set_running(num_nodes):

    try:
        rs = get_rs_status()
        conf = get_rs_configuration()
        hosts  = connection.hosts
    except:
        print('can\'t query MongoDB..is it running?')
        raise

    if rs['ok'] != 1:
        print('Sorry, ok is not 1 for rs.status()')
        print('Here is what I get:')
        pp = pprint.PrettyPrinter(depth=6)
        pp.pprint(rs)
        return False

    if len(rs['members']) != num_nodes:
        print('Sorry, there need to be three members of the replica set.')
        print('Here is the menbers array I see')

        pp = pprint.PrettyPrinter(depth=6)
        pp.pprint(rs['members'])
        return False
    
    print('Looks good. Replica set with three nodes running')
    return True


def graceful_exit(i):
    connection.close()
    sys.exit(i)


def main(argv):
    """ Main section of the code """
    arg_parsing(argv)
    global connection
    global db

    print('Welcome to the HW 6.x replica Checker. My job is to '
          'make sure you started a replica set with three nodes')

    # connect to the db (mongostr was set in arg_parsing)
    try:
        connection = pymongo.MongoClient(mongostr, replicaSet=rs_name)
        db = connection[db_name]
    except:
        print(f'can\'t connect to MongoDB replica {rs_name} set using {mongostr}. Is it running?')
        exit(2)     # no graceful exit if it is not connected
        
    if not repl_set_running(3):
        print('Sorry, the replica set does not seem to be running')
        graceful_exit(1)
    
    # if you are reading this in cleartext, you are
    # violating the honor code.
    # You can still redeem yourself. Get it working and
    # don't submit the validation code until you do.
    # All a man has at the end of the day is his word.
    print('Tests Passed for HW 6.5. Your HW 6.5 validation code is kjvjkl3290mf0m20f2kjjv')
    graceful_exit(0)


if __name__ == '__main__':
    main(sys.argv[1:])








