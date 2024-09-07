from manim import *
from random import *
import networkx as nx


class GraphExample(Scene):
    def construct(self):
        # the graph class expects a list of vertices and edges
        vertices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        edges = [(1, 2), (2, 3), (3, 4), (2, 4), (2, 5), (6, 5),
                 (1, 7), (5, 7), (2, 8), (1, 9), (10, 8), (5, 11)]

        # we're using the layout_config's seed parameter to deterministically set the
        # vertex positions (it is otherwise set randomly)
        g = Graph(vertices, edges, layout_config={"seed": 0}).scale(1.6)

        self.play(Write(g))

        # the graph contains updaters that align edges with their vertices
        self.play(g.vertices[6].animate.shift((LEFT + DOWN) * 0.5))

        self.play(g.animate.shift(LEFT * 3))

        # the graphs can also contain labels and be organized into specific layouts
        # (see the Graph class documentation for the list of all possible layouts)
        h = Graph(vertices, edges, labels=True, layout="circular").shift(RIGHT * 3)

        self.play(Write(h))

        # color the vertex 5 and all of its neighbours
        v = 5
        self.play(
            Flash(g.vertices[v], color=RED, flash_radius=0.5),
            g.vertices[v].animate.set_color(RED),
            *[g.edges[e].animate.set_color(RED) for e in g.edges if v in e],
        )

class StarrySky(Scene):
    def construct(self):
        seed(0xDEADBEEF)

        # the graph class expects a list of vertices and edges
        vertices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        edges = [(1, 2), (2, 3), (3, 4), (2, 4), (2, 5), (6, 5),
                 (1, 7), (5, 7), (2, 8), (1, 9), (10, 8), (5, 11)]

        def RandomStar():
            """Create a pretty random star."""
            return Star(
                randint(5, 7),
                fill_opacity=1,
                outer_radius=0.1,
                color=WHITE).rotate(uniform(0, 2 * PI)
            )

        def RandomSkyLine(u, v, z_index=None):
            """Create a pretty random sky line. The z_index is necessary, since it is
            passed by the graph constructor to edges so they're behind vertices."""
            return DashedLine(u, v, dash_length=uniform(0.03, 0.07), z_index=z_index)

        # custom graph with star vertices and dashed line edges
        g = Graph(vertices, edges,
            layout_config={"seed": 0},
            vertex_type=RandomStar,
            edge_type=RandomSkyLine,
        ).scale(2).rotate(-PI / 2)

        self.play(Write(g))

        self.play(FadeOut(g))

class GraphGenerationExample(Scene):
    def construct(self):
        seed(0xDEADBEEF)

        n = 12     # number of vertices
        p = 3 / n  # probability that there is an edge between a pair

        # generate until our graph is not connected (so it looks nicer)
        graph = None
        while graph is None or not nx.is_connected(graph):
            graph = nx.generators.random_graphs.gnp_random_graph(n, p)

        g = Graph.from_networkx(graph, layout_config={"seed": 0}).scale(2.2).rotate(-PI / 2)

        self.play(Write(g))