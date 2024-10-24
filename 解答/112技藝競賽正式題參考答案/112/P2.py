s = input()

s_prime = '#' + '#'.join(s) + '#'
n_prime = len(s_prime)
radii = []
center, radius = 0, 0

while center < len(s_prime):
    while 0 <= center - radius - 1 and center + radius + 1 < n_prime and\
            s_prime[center - radius - 1] == s_prime[center + radius + 1]:
        radius += 1

    radii.append(radius)
    old_center, old_radius = center, radius
    center, radius = center + 1, radius - 1

    while center <= old_center + old_radius:
        mirrored_center = old_center - (center - old_center)
        mirrored_radius = radii[mirrored_center]
        max_radius = old_center + old_radius - center

        if mirrored_radius < max_radius:
            radii.append(mirrored_radius)
        elif mirrored_radius > max_radius:
            radii.append(max_radius)
        else:
            radius = mirrored_radius
            break

        center += 1

print(max(radii))
