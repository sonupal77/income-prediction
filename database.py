from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from logger import Logger

logging = Logger('logFiles/test.log')

class Connector:
    def __init__(self):
        """
        :DESC: Creates connection with Database when backend thread runs.
        """
        logging.info('INFO', 'Obj created')
        self.Client_id = 'wQGqxyNMCUqAYNXfZZoetGwg'
        self.Client_secret = 'g2TGeNyQY.dZzbFbAuQwhEHt6FEAPwZn-wH4Xl2nbm.SUgg1sUZQq8QvXdZWD.a5P8Ozk75AETpHJt,P+rThrY-qU6+36lf8IjDcfn52e_WSQNkmZtBCeZ6Ih53FqbC+'
        cloud_config = {'secure_connect_bundle': 'secure-connect-test77'}
        auth_provider = PlainTextAuthProvider(self.Client_id, self.Client_secret)
        cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
        self.session = cluster.connect()

    def master(self):
        """
        :DESC: Creates table if not existed into database
        :return:
        """
        self.session.execute("use ineurontest")
        self.session.execute("select release_version from system.local")
        self.session.execute("CREATE TABLE Data(id uuid PRIMARY KEY,Age int,Education text,Capitalgain int,Capitalloss int,Workclass text,MaritalStatus text,Race text, Gender text, HoursperWeek int, Country text);")

    def addData(self, result):
        """
        :param result: Gets data from user and puts it into database
        :return:
        """
        logging.info('INFO', "Inside addData")
        logging.info('INFO', "Inside addData")

        column = "id, Age, Education, Capitalgain, Capitalloss, Workclass, MaritalStatus, Race, Gender, HoursperWeek, Country"
        value = "{0},'{1}','{2}','{3}','{4}',{5},{6},{7},{8},{9},{10}".format('uuid()', 'Age', 'Education', 'Capitalgain',
                                                                        'Capitalloss', 'Workclass', 'MaritalStatus',
                                                                        'Race', 'Gender', 'HoursperWeek', 'Country')
        logging.info('INFO', "String created")
        custom = "INSERT INTO Data({}) VALUES({});".format(column, value)

        logging.info('INFO', "Key created")
        self.session.execute("USE ineurontest")

        output = self.session.execute(custom)

        logging.info('INFO', "Column inserted {}".format(output))


    def getData(self):
        """
        :DESC: Retrieves Data from Database
        :return:
        """
        self.session.execute("use ineurontest")
        row = self.session.execute("SELECT * FROM Data;")
        collection = []
        for i in row:
            collection.append(tuple(i))
        logging.info('INFO', "Retrieved Data from Database : {}".format(i))
        return tuple(collection)
