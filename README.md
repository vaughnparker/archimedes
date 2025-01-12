# archimedes
A description + derivation of the Platonic and Archimedean solids

In this repo I want to play around with and discuss the class of polyhedra called the [Archimedean solids](https://en.wikipedia.org/wiki/Archimedean_solid). They are a super cool group of shapes and in this Github repo I will show you how you can discover all oft them from the ground up.

But before we get into what they are and how they are defined, there are a few prerequisite pieces of knowledge. If you are already comfortable with the basics what polyhedra are, you can skip this part.

## What is a polygon?

A [polygon](https://en.wikipedia.org/wiki/Polygon) is usually what we think of when we think of a 2-dimensional (2D) shape. There are many definitions of what a polygon is, but my favorite comes from jan Misali's [video on regular polyhedra.](https://www.youtube.com/watch?v=_hjRvZYkAgA). From the video:

> A *polygon* is a shape made out of line segments where the defining endpoints are each shared by exactly two line segments.

The "line segments" that form up a polygon are called "edges" and the "defining endpoints" are called "vertices" (singular = "vertex").

> A *regular polygon* is a polygon whose edges are the same length and whose vertices are the same angle.

I'm also going to put a few more constraints on what we're talking about here. I'm talking about things that could feasibly exist in the real world, so I'm not going to allow for shapes that intersect themselves. Think of a star or pentagram. Technically, a star has five "edges", it's just that these "edges" happen to pass through each other. I am going to discuss shapes that have clearly defined "insides" and "outsides". This type of polygons is sometimes referred to as [simple polygons](https://en.wikipedia.org/wiki/Simple_polygon). From Wikipedia:

> In geometry, a simple polygon is a polygon that does not intersect itself and has no holes.

All polygons that are simple and regular are also "convex" (as opposed to "concave"). From Wikipedia:

> * Convex: any line drawn through the polygon (and not tangent to an edge or corner) meets its boundary exactly twice. As a consequence, all its interior angles are less than 180°. Equivalently, any line segment with endpoints on the boundary passes through only interior points between its endpoints.
> * Simple: the boundary of the polygon does not cross itself. All convex polygons are simple.

This distinction between convex and concave polygons is best seen visually:

[See image here](https://img.sparknotes.com/figures/B/b333d91dce2882b2db48b8ad670cd15a/convexconcave.gif)

### How many (convex) regular polygons are there?

https://mathworld.wolfram.com/images/eps-svg/RegularPolygons_800.svg

Most people have a general sense of what a regular polygon might look like. A regular 3-gon (aka an equilateral triangle) is formed of 3 sides with equally long sides and equally measured angles. A regular 4-gon is a square. Above that are pentagons (5 sides), hexagons (6 sides), octagons (8 sides), decagons (10 sides), and many more.

It is not hard to see that there are infinitely many regular polygons.

## Outline for rest of readme

* What is a polyhedron?
  * What are regular polyhedra?
* The platonic solids
  * How do we know these are the only 5? / Constructing all the platonic solids
    * Formal definition of face, edge, vertex transitivity? maybe
* Archimedean solids
* Tilings
* Johnson solids?
