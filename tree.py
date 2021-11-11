import turtle
tina = turtle.Turtle()
# tina.shape('turtle')
# tina.color("green")
hr = turtle.Turtle()
hr.left(90)
hr.speed(150)

def tree(i):
    if i<10:
        return
    else:
        hr.forward(i)
        hr.left(40)
        tree(3*i/4)
        hr.right(80)
        tree(3 * i / 5)
        hr.left(40)
        hr.backward(i)

tree(100)




def main():
    n = int(sys.argv[1])
    tree(n, 0.5, 0.0,0.5 ,0.5)

    stddraw.show()


if __name__ == '__main__':
    main()
