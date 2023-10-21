from neo4j import GraphDatabase

class Interface:
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password), encrypted=False)
        self._driver.verify_connectivity()

    def close(self):
        self._driver.close()

    def bfs(self, start_node, last_node):
        # TODO: Implement this method
        with self._driver.session() as session:
            result = session.run("""
                MATCH (a:Location{name: $First})
                MATCH (d:Location{name: $last})
                CALL gds.bfs.stream('mygraph', {
                  sourceNode: id(a),targetNodes: [id(d)]
                })
                YIELD path
                RETURN path
            """, First=start_node, last=last_node)
            # Extract the first path from the result set
            output = result.data()
            return output

    def pagerank(self, max_iterations, weight_property):
        # TODO: Implement this method
        try:
            with self._driver.session() as session:

                # Create a graph
                session.run(""" 
                CALL gds.graph.project.cypher(
                    'mygraph',
                    'MATCH (pickup:Location) RETURN id(pickup) AS id',
                    'MATCH (pickup:Location)-[trip:TRIP]->(dropoff:Location) RETURN id(pickup) AS source, id(dropoff) AS target, trip.distance AS distance')""")

                # Running PageRank to find the highest ranked node
                result = session.run("""
                CALL gds.pageRank.stream('mygraph', {
                maxIterations: $max_iter,
                dampingFactor: 0.85,
                relationshipWeightProperty: $prop})
                YIELD nodeId, score RETURN gds.util.asNode(nodeId).name AS name, score ORDER BY score DESC, name ASC LIMIT 1 """, max_iter = max_iterations, prop = weight_property)
                highest = result.data()[0] 

                # Running PageRank to find the lowest ranked node
                result =session.run("""
                CALL gds.pageRank.stream('mygraph', {
                maxIterations: $max_iter,
                dampingFactor: 0.85,
                relationshipWeightProperty: $prop})
                YIELD nodeId, score
                RETURN gds.util.asNode(nodeId).name AS name, score
                ORDER BY score ASC, name ASC
                LIMIT 1 """, max_iter = max_iterations, prop = weight_property)
                lowest = result.data()[0]
                output = [highest, lowest]
                return output
        except:
            with self._driver.session() as session:
                # Running PageRank to find the highest ranked node
                result = session.run("""
                CALL gds.pageRank.stream('mygraph', {
                maxIterations: $max_iter,
                dampingFactor: 0.85,
                relationshipWeightProperty: $prop})
                YIELD nodeId, score RETURN gds.util.asNode(nodeId).name AS name, score ORDER BY score DESC, name ASC LIMIT 1 """, max_iter = max_iterations, prop = weight_property)
                highest = result.data()[0]
                # Running PageRank to find the lowest ranked node
                result =session.run("""
                CALL gds.pageRank.stream('mygraph', {
                maxIterations: $max_iter,
                dampingFactor: 0.85,
                relationshipWeightProperty: $prop})
                YIELD nodeId, score
                RETURN gds.util.asNode(nodeId).name AS name, score
                ORDER BY score ASC, name ASC
                LIMIT 1 """, max_iter = max_iterations, prop = weight_property)
                lowest = result.data()[0]
                output = [highest, lowest]

                return output
            #raise NotImplementedError