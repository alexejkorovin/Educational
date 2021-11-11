import stddraw


if i % 1000 == 0:
 stddraw.clear()
 for k in range(n):
  stddraw.filledRectangle(k - 0.25, 0.0, 0.5, hits[k])
 stddraw.show(10)
