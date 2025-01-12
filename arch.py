# TODO: rewrite this into a neat jupyter notebook

# let's list all archimedian solids...
# Archimedian solids are polyhedra with regular polygons as faces that are vertex-transitive.
# According to wikipedia:
# In geometry, an Archimedean solid is one of 13 convex polyhedra whose faces
# are regular polygons and whose vertices are all symmetric to each other

# How could we possibly find all of them? Well, it's actually not so hard!
# We can do this almost entirely in 2 dimensions. Since these polyhedra are
# vertex transitive, we can just construct one vertex and it will define the
# whole polyhedra. We know that "doing a loop" is 360°. We also know that
# traversing the boundary of an n-gon brings us facing back in the same
# direction we started in. These "turns" we make are really just the exterior
# angles of an n-gon. Therefore, the sum of the exterior angles of a polygon
# must be 360°

# From Google: "The sum of the exterior angles of any convex polygon is 360°.
# An exterior angle is the angle formed outside a polygon when one of its sides
# is extended.

# A specific exterior angle can therefore be found by 360° / n.
# A specific interior angle can be found by 180 - (360° / n)

def get_interior_angle(n):
	return 180 - (360 / n)

for n in range(3, 21):
	print(f"A polygon with {n} sides has interior angles of {get_interior_angle(n)}°")

def get_vertex_sum(vertex):
	vertex_sum = 0
	for shape in vertex:
		vertex_sum += get_interior_angle(shape)
	return vertex_sum


# Each vertex of a polyhedra must conform to the following rules:
# - The vertex must be made up of at least 3 "faces" (polygons)"
# - The angles of the sides in the vertex must sum to at most 360°
# - Each polygon must have at least 3 sides

# Because the smallest regular polygon (the equilateral triangle) has angles of
# 60°, we can add another rule:
# - The vertex must be made up of at most 6 faces

# Now let's list them all out:

# all_three_meets = []
# all_four_meets = []
# all_five_meets = []
# #all_six_meets = []

def get_three_meets():
	to_return = []
	for a in range(3, 100):
		for b in range(3, 100):
			for c in range(3, 100):
				possible_config = (a, b, c)
				vertex_sum = get_vertex_sum(possible_config)
				
				if vertex_sum <= 360:
					to_return.append(possible_config)

	return to_return

all_three_meets = get_three_meets()
print(len(all_three_meets))


# First of all - I made a huge error in the above code. Running it we get 2,872
# solids, but there's a ton of duplicates! For example, we have (99, 4, 3) and
# (99, 3, 4). Let's run it again with the constraint that a <= b <= c :

def get_three_meets_v2():
	to_return = []
	for c in range(3, 100):
		for b in range(3, c+1):
			for a in range(3, b+1):
				possible_config = (a, b, c)
				vertex_sum = get_vertex_sum(possible_config)
				
				if vertex_sum <= 360:
					to_return.append(possible_config)

	return to_return

all_three_meets_v2 = get_three_meets_v2()
print(len(all_three_meets_v2))


# This gives us 587 vertex configurations already! But wait...
# do all of these correspond to possible solids?

# Here is where the first big insight comes in: if a is odd, then b = c.
# How do we know this? A great proof can be found at the following link:
# https://math.harvard.edu/media/AllenLiuTheStarsAboveUsThesis.pdf

# I will explain this reasoning: "Lemma: If a uniform polyhedron has an
# odd-sided face, that face must be surrounded at each vertex by two faces that
# are identical to each other."

# We know this because if a is odd, then one of the shapes ("A") that meets at
# the vertex is an odd-sided polygon. Since all of its vertices have the form
# (a, b, c), each of its sides must border a polygon with b or c sides. These
# sides must alternate, such that the polygons bordering A must have sides of
# length bcbcbc...
# However, since there is an odd number of sides, this means that there will
# eventually come a vertex that is of form (a, b, b) or (a, b, c). Therefore,
# this would not be an Archimedian solid, and so: if a is odd, then b = c.

# We can re-state this by saying that, for each vertex (a, b, c) one of
# the following statements must be true:
# a is odd, and b = c
# b is odd, and a = c
# c id odd, and a = b
# or a, b, and c are all even


# Let's filter the existing list down further:

def is_contradiction(a, b, c):
	a_is_odd = a % 2 == 1
	b_is_odd = b % 2 == 1
	c_is_odd = c % 2 == 1

	if a_is_odd and (b != c):
		return True

	if b_is_odd and (a != c):
		return True

	if c_is_odd and (a != b):
		return True

	return False

def filter_out_contradictions(list_of_solids):
	to_return = []
	for a, b, c in list_of_solids:
		if is_contradiction(a, b, c):
			pass
		else:
			to_return.append((a, b, c))

	return to_return


all_three_meets_v3 = filter_out_contradictions(all_three_meets_v2)
print(len(all_three_meets_v3))
# for possible_config in all_three_meets_v3:
# 	print(possible_config)

# Looking at these 164 configurations, we notice that many of them belong to
# one of two families: (4, 4, x) and (3, 3, x). These families are infinite and
# they have special names, the prisms and antiprisms respectively. However,
# there are two exceptions. These are the tetrahedron (3, 3, 3) and cube
# (4, 4, 4). These are both Platonic Solids. For now, let's filter out the
# infinite families.

# THIS IS NOT TRUE!!! ANTIPRISMS ARE (3, 3, 3, n), and NOT (3, 3, n)

def is_prism(a, b, c):
    return [a, b, c].count(4) == 2

#def filter_out_infinite_families(list_of_solids):
def filter_out_prisms(list_of_solids):
	to_return = []
	for a, b, c in list_of_solids:
		if is_prism(a, b, c):
			pass
		else:
			to_return.append((a, b, c))

	return to_return


all_three_meets_v4 = filter_out_prisms(all_three_meets_v3)
print(len(all_three_meets_v4))

# for possible_config in all_three_meets_v4:
# 	print(possible_config)

print("All 3-face vertices found!")

# We have finally arrived at all possible vertex configurations of 3 polygons. Let's go through them one-by-one

# blah blah

# To review:

# (3, 3, 3)		Platonic Solid (#1)
# (4, 4, 4)		Platonic Solid (#2)
# (5, 5, 5)		Platonic Solid (#3)
# (3, 6, 6)		Archimedian Solid (#1)
# (4, 6, 6)		Archimedian Solid (#2)
# (5, 6, 6)		Archimedian Solid (#3)
# (6, 6, 6)		Regular Tiling (#1)
# (4, 6, 8)		Archimedian Solid (#4)
# (3, 8, 8)		Archimedian Solid (#5)
# (4, 8, 8)		Semiregular Tiling (#1)
# (4, 6, 10)	Archimedian Solid (#6)
# (3, 10, 10)	Archimedian Solid (#7)
# (4, 6, 12)	Semiregular Tiling (#2)
# (3, 12, 12)	Semiregular Tiling (#3)

# 3 platonic solids
# 7 archimedian solids
# 1 regular tiling
# 3 semi-regular tilings

# Let's move on to the next part, 4-face vertices:


# the logic here needs to be different.
# not every vertex can be re-written in a format where it's decreasing


# We have a weird issue. It has to do with symmetries of regular polygons.
# A triangle has 6 symmetries https://en.wikipedia.org/wiki/Dihedral_group
# A square has 8. However, for 3 numbers, there are only 6 orders to write them
# in. But for 4 numbers, there are 4! = 24 ways. Therefore, we have an issue.
# We can't just allow all duplicates, as for any tuple (a, b, c, d), there are
# 8 valid ways to write it. But if we add the requirement that
# a <= b <= c <= d, then we will discount completely valid configurations, such
# as (3, 5, 3, 5) / the icosidodecahedron

# The actual solution to this is to write up an explanation before we add the
# a <= b <= c rule in the 3-meets logic. Anyways.

def generate_unique_four_meets():
	to_return = []
	for d in range(3, 100):
		for c in range(3, d+1):
			for b in range(3, d+1):
				for a in range(3, d+1):
					possible_config = (a, b, c, d)
					vertex_sum = get_vertex_sum(possible_config)
				
					if vertex_sum > 360:
						continue

					if (a, b, c, d) in to_return or \
					(b, c, d, a) in to_return or \
					(c, d, a, b) in to_return or \
					(d, a, b, c) in to_return or \
					(d, c, b, a) in to_return or \
					(c, b, a, d) in to_return or \
					(b, a, d, c) in to_return or \
					(a, d, c, b) in to_return:
						continue

					to_return.append(possible_config)

	return to_return




all_four_meets_v1 = generate_unique_four_meets()
print(len(all_four_meets_v1))
# for possible_config in all_four_meets_v1:
# 	print(possible_config)




# antiprisms exist. Let's get rid of them.

def is_antiprism(vertex):
    return vertex.count(3) == 3

def filter_out_antiprisms(list_of_solids):
	to_return = []
	for config in list_of_solids:
		if is_antiprism(config):
			pass
		else:
			to_return.append(config)

	return to_return


all_four_meets_v2 = filter_out_antiprisms(all_four_meets_v1)
print(len(all_four_meets_v2))
# for possible_config in all_four_meets_v2:
# 	print(possible_config, get_vertex_sum(possible_config))

# Now it's time for epic Kepler insight number 2:
# "[There cannot be a] solid angle surrounded by four faces with at least one
# 3-gon and a b-gon opposite of it where a ≠ c.”


def is_lemma2_contradiction(vertex):
    # First, we find the 3-gon
    triangle_indices = []
    for i in range(len(vertex)):
    	if vertex[i] == 3:
    		triangle_indices.append(i)

    for i in triangle_indices:
    	a_index = (i + 1) % 4
    	c_index = (i + 3) % 4
    	if vertex[a_index] != vertex[c_index]:
    		return True

    return False

def filter_out_lemma2_cases(list_of_solids):
	to_return = []
	for config in list_of_solids:
		if is_lemma2_contradiction(config):
			pass
		else:
			to_return.append(config)

	return to_return


all_four_meets_v3 = filter_out_lemma2_cases(all_four_meets_v2)
print(len(all_four_meets_v3))
for possible_config in all_four_meets_v3:
	print(possible_config, get_vertex_sum(possible_config))


# We have finally arrived at all possible vertex configurations of 4 polygons. Let's go through them one-by-one

# blah blah

# To review:

# {3, 3, 3, 3) 240.0 Platonic Solid (#4)
# (3, 4, 3, 4) 300.0 Archimedian Solid (#6)
# (4, 4, 3, 4) 330.0 Archimedian Solid (#9)
# (4, 4, 4, 4) 360.0 Regular Tiling (#2)
# (3, 5, 3, 5) 336.0 Archimedian Solid (#10)
# (4, 3, 4, 5) 348.0 Archimedian Solid (#11)
# (3, 6, 3, 6) 360.0 Semiregular Tiling (#4)
# (4, 3, 4, 6) 360.0 Semiregular Tiling (#5)


# 1 platonic solid
# 4 archimedian solids
# 1 regular tiling
# 2 semi-regular tilings


# We've found 11 of the 13 archimedian solids now. We're in the home stretch!
# Let's repeat this with the case of 5-face vertices.

print("All 4-face vertices found!")

# For this one, let's go about this in a clever way. Recall that:

# A polygon with 3 sides has interior angles of 60.0°
# A polygon with 4 sides has interior angles of 90.0°
# A polygon with 5 sides has interior angles of 108.0°
# A polygon with 6 sides has interior angles of 120.0°
# A polygon with 7 sides has interior angles of 128.57142857142856°
# A polygon with 8 sides has interior angles of 135.0°
# A polygon with 9 sides has interior angles of 140.0°
# A polygon with 10 sides has interior angles of 144.0°
# A polygon with 11 sides has interior angles of 147.27272727272728°
# A polygon with 12 sides has interior angles of 150.0°
# A polygon with 13 sides has interior angles of 152.30769230769232°
# A polygon with 14 sides has interior angles of 154.28571428571428°
# A polygon with 15 sides has interior angles of 156.0°
# A polygon with 16 sides has interior angles of 157.5°
# A polygon with 17 sides has interior angles of 158.8235294117647°
# A polygon with 18 sides has interior angles of 160.0°
# A polygon with 19 sides has interior angles of 161.05263157894737°
# A polygon with 20 sides has interior angles of 162.0°

# The first 4 polygons are going to each contribute at least 60°. This means
# that the 5th and final polygon must contribute at most 360° - (4 * 60°) =
# 360° - 240° = 120°. Therefore, it is clear that even the largest polygon in
# the largest case has at most 120, which is a hexagon. Let's not waste time
# searching for polygons with more than 6 sides then!

def generate_unique_five_meets():
	to_return = []
	for e in range(3,7):
		for d in range(3, e+1):
			for c in range(3, e+1):
				for b in range(3, e+1):
					for a in range(3, e+1):
						possible_config = (a, b, c, d, e)
						vertex_sum = get_vertex_sum(possible_config)
					
						if vertex_sum > 360:
							continue

						if (a, b, c, d, e) in to_return or \
						(b, c, d, e, a) in to_return or \
						(c, d, e, a, b) in to_return or \
						(d, e, a, b, c) in to_return or \
						(e, a, b, c, d) in to_return or \
						(e, d, c, b, a) in to_return or \
						(d, c, b, a, e) in to_return or \
						(c, b, a, e, d) in to_return or \
						(b, a, e, d, c) in to_return or \
						(a, e, d, c, b) in to_return:
							continue

						to_return.append(possible_config)

	return to_return

all_five_meets_v1 = generate_unique_five_meets()
print(len(all_five_meets_v1))
for possible_config in all_five_meets_v1:
	print(possible_config, get_vertex_sum(possible_config))


# This generates 6 vertex configurations of 5 faces, all of which are valid:

# Let's go through them one-by-one

# blah blah

# To review:

# (3, 3, 3, 3, 3) 300.0 Platonic Solid (#5)
# (3, 3, 3, 3, 4) 330.0 Archimedian Solid (#12)
# (4, 3, 3, 3, 4) 360.0 Semiregular Tiling (#6)
# (3, 4, 3, 3, 4) 360.0 Semiregular Tiling (#7)
# (3, 3, 3, 3, 5) 348.0 Archimedian Solid (#13)
# (3, 3, 3, 3, 6) 360.0 Semiregular Tiling (#8)

# Finally, we can consider the only way that 6 regular polygons can meet at a
# single vertex:

# (3, 3, 3, 3, 3, 3) 360.0 Regular Tiling (#3)





# Now, we consider Kepler’s second lemma.
# Lemma 2: A polyhedron that has the same pattern of polygon faces at every vertex
# cannot have these types of solid angles:
# i) A solid angle surrounded by three faces—a-gon, b-gon, and c-gon—where a is
# odd and b ≠ c. See Figure 2.1. 
# 6
# ii) A solid angle surrounded by four faces with at least one 3-gon and a b-gon
# opposite of it where a ≠ c.” (Cromwell 159). See Figure 2.2
