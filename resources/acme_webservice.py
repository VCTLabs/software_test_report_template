"""
This example was taken from the upstream documented examples.

https://diagrams.mingrammer.com/
"""

from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.aggregator import Fluentd
from diagrams.onprem.analytics import Spark
from diagrams.onprem.compute import Server
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.monitoring import Grafana, Prometheus
from diagrams.onprem.network import Nginx
from diagrams.onprem.queue import Kafka

# can use graphviz dot attributes:
# graph_attr, node_attr and edge_attr are supported

node_attr = {
    "fontsize": "14",
}

graph_attr = {
    "fontsize": "24",
    "labelloc": "t",
    "bgcolor": "transparent",
}

edge_attr = {"penwidth": "5", "bgcolor": "transparent"}

with Diagram(
    "Advanced ACME Web Service",
    show=False,
    graph_attr=graph_attr,
    edge_attr=edge_attr,
    node_attr=node_attr,
):
    ingress = Nginx("ingress")

    metrics = Prometheus("metric")
    metrics << Edge(color="firebrick", style="dashed") << Grafana("monitoring")

    with Cluster("Service Cluster"):
        grpcsvc = [Server("grpc1"), Server("grpc2"), Server("grpc3")]

    with Cluster("Sessions HA"):
        primary = Redis("session")
        (
            primary - Edge(color="brown", style="dashed") - Redis("replica")
            << Edge(label="collect")
            << metrics
        )
        grpcsvc >> Edge(color="brown") >> primary

    with Cluster("Database HA"):
        primary = PostgreSQL("users")
        (
            primary - Edge(color="brown", style="dotted") - PostgreSQL("replica")
            << Edge(label="collect")
            << metrics
        )
        grpcsvc >> Edge(color="black") >> primary

    aggregator = Fluentd("logging")
    (
        aggregator
        >> Edge(label="parse")
        >> Kafka("stream")
        >> Edge(color="black", style="bold")
        >> Spark("analytics")
    )

    (
        ingress
        >> Edge(color="darkgreen")
        << grpcsvc
        >> Edge(color="darkorange")
        >> aggregator
    )
