from neo4j import GraphDatabase

URI = "neo4j+s://9a34ec7d.databases.neo4j.io"
USERNAME = "neo4j"
PASSWORD = "mjQ8nWuZSlptcDZ003VLSG6Rq6neePCsf_g3-DFlCgs"

driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))

def get_session():
    return driver.session()

def test_connection():
    with driver.session() as session:
        result = session.run("RETURN 'Connected to Neo4j Aura' AS message")
        return result.single()["message"]