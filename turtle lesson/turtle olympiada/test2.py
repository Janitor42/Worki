import turtle as t

t.speed(0)
t.pensize(2)

def oval_spiral():
    # Increasing radii for the spiraling effect
    radii = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    t.pendown()
    for r in radii:
        # Draw a circle (which is a special case of oval with equal radii)
        t.circle(r)
    t.penup()

# Create the spiral pattern by rotating
for i in range(12):
    oval_spiral()
    t.goto(0, 0)
    t.left(30)

t.mainloop()