from gremlin_python import statics
from gremlin_python.structure.graph import Graph
from gremlin_python.process.graph_traversal import __
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from gremlin_python.process.anonymous_traversal import traversal

def seed(g):
    g.addV('animal').property('name', 'Am Bulldog').as_('breed_1').iterate()
    g.addV('animal').property('name', 'Blue Tick').as_('breed_2').iterate()
    g.addV('animal').property('name', 'Labrador').as_('breed_3').iterate()
    g.addV('animal').property('name', 'Gr Shepard').as_('breed_4').iterate()
    g.addV('animal').property('name', 'Poodle').as_('breed_5').iterate()
    
    g.addV('animal').property('name', 'White').property('transperency', 'x234567').as_('color_1').iterate()
    g.addV('animal').property('name', 'Grey').as_('color_2').iterate()
    g.addV('animal').property('name', 'Black').as_('color_3').iterate()
    g.addV('animal').property('name', 'Brown').as_('color_4').iterate()

    g.addE('White Am Bulldog').from_('breed_1').to('color_1')
    g.addE('Black Am Bulldog').from_('breed_1').to('color_3')

    # list of list
    # results = g.V().outE().inV().path().by('name')

    results = g.V()

    print(results)

    # for result in results:
    #     print(result)

def main():
    connection = DriverRemoteConnection('ws://middle-ware:8182/gremlin', 'g')
    # The connection should be closed on shut down to close open connections with connection.close()
    g = traversal().withRemote(connection)
    seed(g)
    connection.close()

if __name__ == "__main__":
    main()