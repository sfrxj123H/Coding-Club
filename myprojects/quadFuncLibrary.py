class QuadFuncLibrary:
    def __init__(self):
        self.functionList = {}
        self.complexResults = True

    def isSquaredRootRational(self, num):
        num2 = num
        dem = 1
        while int(num2) != num2:
            num2 *= 10
            dem *= 10
        num2r = int(num2 ** 0.5)
        demr = int(dem ** 0.5)
        return num2r * num2r == num2 and demr * demr == dem

    def displayRounded(self, value):
        if value == 0:
            return 0
        else:
            return "{:.6f}".format(value).rstrip('0').rstrip('.') if '.' in "{:.6f}".format(value) else str(value)

    def tryInt(self, value):
        value = float(value)
        return int(value) if value == int(value) else value

    def formatFunc(self, coef2, coef1, coef0, varName='x', factoredFormat=False, coef4=0, coef3=0):
        output = ""
        if coef4 != 0:
            if coef4 == 1:
                output += f"{varName}⁴"
            elif coef4 == -1:
                output += f"-{varName}⁴"
            else:
                output += f"{self.displayRounded(coef4)}{varName}⁴"
        if coef3 != 0:
            if coef4 != 0:
                if coef3 > 0:
                    output += " + "
                else:
                    output += " - "
            else:
                if coef3 < 0:
                    output += "-"
            if abs(self.tryInt(coef3)) == 1:
                output += f"{varName}³"
            else:
                output += f"{self.displayRounded(abs(self.tryInt(coef3)))}{varName}³"
        if coef2 != 0:
            if coef4 != 0 or coef3 != 0:
                if coef2 > 0:
                    output += " + "
                else:
                    output += " - "
            else:
                if coef2 < 0:
                    output += "-"
            if abs(self.tryInt(coef2)) == 1:
                output += f"{varName}²"
            else:
                output += f"{self.displayRounded(abs(self.tryInt(coef2)))}{varName}²"
        if coef1 != 0:
            if coef4 != 0 or coef3 != 0 or coef2 != 0:
                if coef1 > 0:
                    output += " + "
                else:
                    output += " - "
            else:
                if coef1 < 0:
                    output += "-"
            if abs(self.tryInt(coef1)) == 1:
                output += f"{varName}"
            else:
                output += f"{self.displayRounded(abs(self.tryInt(coef1)))}{varName}"
        if coef2 == 0 and coef1 == 0:
            output += f"{self.displayRounded(coef0)}"
        elif coef0 != 0:
            if coef4!= 0 or coef3!= 0 or coef2 != 0 or coef1 != 0:
                output += " "
            if coef0 > 0:
                output += f"+ {self.displayRounded(coef0)}"
            else:
                output += f"- {self.displayRounded(abs(self.tryInt(coef0)))}"
        if int(coef4 == 0) + int(coef3 == 0) + int(coef2 == 0) + int(coef1 == 0) + int(coef0 == 0) < 4 and factoredFormat:
            output = "(" + output + ")"
        return output

    def functionEvaluation(self, a, b, c):
        print("Specify the range for evaluating the function:")

        minStep = self.tryInt(input("Minimum x value: "))
        maxStep = self.tryInt(input("Maximum x value: "))
        step = self.tryInt(input("Step value: "))

        if minStep <= maxStep:
            print(f"\nFUNCTION VALUES WHEN x EQUALS FROM {minStep} TO {maxStep} (STEP {step})")
            for i in range(0, int((maxStep - minStep) / step) + 1):
                x = self.tryInt(minStep + i * step)
                print(f"f({self.displayRounded(x)}) = {self.displayRounded(a*x**2 + b*x + c)}")

    def rootFinder(self, a, b, c, isIntersect=False, intersect_a=0, intersect_b=0, intersect_c=0):
        if a != 0:
            print("Type: Quadratic function")
            discriminant = self.tryInt(b**2 - 4*a*c)
            print(f"Discriminant: Δ = {discriminant}")
            if discriminant > 0:
                roots = [self.tryInt((-b - discriminant**0.5) / (2*a)), self.tryInt((-b + discriminant**0.5) / (2*a))]
                if abs(roots[0]) > abs(roots[1]):
                    roots = roots[::-1]
                root1 = min(roots)
                root2 = max(roots)
                if self.isSquaredRootRational(discriminant) or not self.complexResults:
                    print(f"Roots: x₁ = {self.displayRounded(root1)}, x₂ = {self.displayRounded(root2)}")
                    print(f"Factored form: {self.formatFunc(0, a, -a*roots[0], 'x', 1)}{self.formatFunc(0, 1, -roots[1], 'x', 1)}")
                else:
                    #Starts searching for more complex results
                    ddenominator = float(self.displayRounded(abs(2*a)))
                    print(ddenominator)
                    multiplier = 1
                    while ddenominator % 1 != 0:
                        ddenominator = float(self.displayRounded(ddenominator*10))
                        multiplier = float(self.displayRounded(multiplier*10))
                    while ddenominator % 2 == 0 and multiplier % 2 == 0:
                        ddenominator /= 2
                        multiplier /= 2
                    while ddenominator % 5 == 0 and multiplier % 5 == 0:
                        ddenominator /= 5
                        multiplier /= 5
                    ddenominator = int(ddenominator)
                    multiplier = int(multiplier)
                    ddiscriminant = self.tryInt(self.displayRounded(discriminant))
                    for i in range(ddenominator, 1, -1):
                        if ddiscriminant % (i*i) == 0 and ddenominator % i == 0:
                            ddiscriminant = self.tryInt(ddiscriminant // (i*i))
                            ddenominator = self.tryInt(ddenominator // i)
                    #Display results
                    droot1 = f"{self.displayRounded(-b / (2*a))} - {multiplier if multiplier != 1 else ''}√{ddiscriminant if ddiscriminant % 1 == 0 else f'({ddiscriminant})'}{' / ' + str(ddenominator) if ddenominator != 1 else ''}"
                    droot2 = f"{self.displayRounded(-b / (2*a))} + {multiplier if multiplier != 1 else ''}√{ddiscriminant if ddiscriminant % 1 == 0 else f'({ddiscriminant})'}{' / ' + str(ddenominator) if ddenominator != 1 else ''}"
                    fd1 = f"- {multiplier if multiplier != 1 else ''}√{ddiscriminant if ddiscriminant % 1 == 0 else f'({ddiscriminant})'}{' /' + str(ddenominator) if ddenominator != 1 else ''}"
                    fd2 = f"+ {multiplier if multiplier != 1 else ''}√{ddiscriminant if ddiscriminant % 1 == 0 else f'({ddiscriminant})'}{' /' + str(ddenominator) if ddenominator != 1 else ''}"
                    print(f"Roots: x₁ = {droot1}, x₂ = {droot2}")
                    print(f"Factored form: {self.formatFunc(0, a, 0, '', 1)}({self.formatFunc(0, 1, -self.tryInt(-b / (2*a)), 'x')} {fd1})({self.formatFunc(0, 1, -self.tryInt(-b / (2*a)), 'x')} {fd2})")
            elif discriminant == 0:
                root = self.tryInt(-b / (2*a))
                roots = [root]
                print(f"Root: x = {root}")
                print(f"Factored form: {self.formatFunc(0, a, 0, '', 1)}{self.formatFunc(0, 1, -self.displayRounded(root), 'x', 1)}²")
            else:
                roots = []
                print("Roots: No real roots.")
        elif b != 0:
            root = self.tryInt(-c / b)
            roots = [root]
            print(f"Root: x = {self.displayRounded(root)}")
        else:
            if c == 0:
                roots = 0
                print("Roots: All real numbers.")
            else:
                roots = []
                print("Roots: No roots.")
        if isIntersect:
            if roots != 0:
                if len(roots) == 0:
                    print("There are no intersections.")
                else:
                    intersect_roots = []
                    for x in roots:
                        intersect_roots.append((x, self.tryInt(intersect_a*x**2 + intersect_b*x + intersect_c)))
                    dprint = ""
                    for x, y in intersect_roots:
                        dprint += f"({self.displayRounded(x)}, {self.displayRounded(y)}), "
                    print(f"Intersection{'s' if len(intersect_roots) > 1 else ''}: {dprint[:-2]}")

    def vertexFinder(self, a, b, c):
        discriminant = b**2 - 4*a*c
        if a != 0:
            vertex_x = self.displayRounded(-b / (2*a))
            vertex_y = self.displayRounded(-discriminant / (4*a))
            print(f"Vertex: ({vertex_x}, {vertex_y})")
            print(f"Axis of symmetry: x = {vertex_x}")
            if a > 0:
                print("Direction: Opens upwards")
                print(f"Monotonicity: f(x) increases on: ({vertex_x}, +∞) and decreases on: (-∞, {vertex_x})")
            else:
                print("Direction: Opens downwards")
                print(f"Monotonicity: f(x) increases on: (-∞, {vertex_x}) and decreases on: ({vertex_x}, +∞)")
        elif b != 0:
            print("Type: Linear function")
            if b > 0:
                print("Direction: Increases")
            else:
                print("Direction: Decreases")
        else:
            print("Type: Constant function")

    def functionInfo(self, a, b, c):
        print(f"\nFUNCTION INFO")
        self.rootFinder(a, b, c)
        self.vertexFinder(a, b, c)

    def polinomialInput(self):
        a, b, c = 0, 0, 0
        maxDegree = input("Enter the maximum degree of the polynomial (0/1/2): ")
        if maxDegree == "2":
            inputMethod = input("""
            Choose your method to calculate coefficients:
            1. Provide 3 coefficients (a ≠ 0)
            2. Provide 1 coefficient and 2 points (a ≠ 0, points must have different x, y values, c ≠ y values of points)
            3. Provide 1 coefficient and vertex (a ≠ 0, c ≠ y value of vertex)
            4. Provide 3 points (points must have different x, y values)
            5. Provide vertex and 1 point (points must have different x, y values)
            6. Provide axis of symmetry and 2 points (points must have different x, y values and not on the axis)
            0. Change maximum degree
            Input method: """)
            if inputMethod == "1":
                print("Enter the coefficients for the quadratic function f(x) = ax² + bx + c")
                a = float(input("a = "))
                b = float(input("b = "))
                c = float(input("c = "))
                if a == 0:
                    print("Error: a cannot be 0.")
                    return 0, 0, 0
            elif inputMethod == "2":
                print("Enter 1 coefficient and 2 points (x1, y1) and (x2, y2) to calculate the coefficients of the quadratic function.")
                x1 = float(input("x1: "))
                y1 = float(input("y1: "))
                x2 = float(input("x2: "))
                y2 = float(input("y2: "))
                if x1 == x2 or y1 == y2:
                    print("Error: x1, x2 and y1, y2 cannot be the same.")
                else:
                    coefChoose = input("Which coefficient will you provide? (a/b/c): ").lower()
                    if coefChoose == "a":
                        a = float(input("a = "))
                        if a == 0:
                            print("Error: a cannot be 0.")
                            return 0, 0, 0
                        b = ((y2 - y1) - a * (x2**2 - x1**2)) / (x2 - x1)
                        c = y1 - a * x1**2 - b * x1
                    elif coefChoose == "b":
                        b = float(input("b = "))
                        a = ((y2 - y1) - b * (x2 - x1)) / (x2**2 - x1**2)
                        c = y1 - a * x1**2 - b * x1
                    elif coefChoose == "c":
                        c = float(input("c = "))
                        if c == y1 or c == y2:
                            print("Error: c cannot be equal to the y value of the points.")
                            return 0, 0, 0
                        a = ((y2 - y1) - (c - c) * (x2 - x1)) / (x2**2 - x1**2)
                        b = (y1 - a * x1**2 - c) / x1
            elif inputMethod == "3":
                print("Enter 1 coefficient and vertex (h, k) to calculate the coefficients of the quadratic function.")
                coefChoose = input("Which coefficient will you provide? (a/b/c): ").lower()
                h = float(input("Vertex x (h): "))
                k = float(input("Vertex y (k): "))
                if c == k:
                    print("Error: c cannot be equal to the y value of the vertex.")
                else:
                    if coefChoose == "a":
                        a = float(input("a = "))
                        if a == 0:
                            print("Error: a cannot be 0.")
                            return 0, 0, 0
                        b = -2 * a * h
                        c = k + a * h**2
                    elif coefChoose == "b":
                        b = float(input("b = "))
                        a = -b / (2 * h)
                        c = k + a * h**2
                    elif coefChoose == "c":
                        c = float(input("c = "))
                        if c == k:
                            print("Error: c cannot be equal to the y value of the vertex.")
                            return 0, 0, 0
                        a = (c - k) / (h**2)
                        b = -2 * a * h
            elif inputMethod == "4":
                print("Enter three points (x1, y1), (x2, y2) and (x3, y3) to calculate the coefficients of the quadratic function.")
                x1 = float(input("x1: "))
                y1 = float(input("y1: "))
                x2 = float(input("x2: "))
                y2 = float(input("y2: "))
                x3 = float(input("x3: "))
                y3 = float(input("y3: "))
                denom = (x1 - x2) * (x1 - x3) * (x2 - x3)
                if y1 == y2 or y1 == y3 or y2 == y3 or denom == 0:
                    print("Error: Points must have different x, y values.")
                    return 0, 0, 0
                a = (x3 * (y2 - y1) + x2 * (y1 - y3) + x1 * (y3 - y2)) / denom
                b = (x3**2 * (y1 - y2) + x2**2 * (y3 - y1) + x1**2 * (y2 - y3)) / denom
                c = (x2 * x3 * (x2 - x3) * y1 + x3 * x1 * (x3 - x1) * y2 + x1 * x2 * (x1 - x2) * y3) / denom
            elif inputMethod == "5":
                print("Enter vertex (h, k) and 1 point (x, y) to calculate the coefficients of the quadratic function.")
                h = float(input("Vertex x (h): "))
                k = float(input("Vertex y (k): "))
                x = float(input("x: "))
                y = float(input("y: "))
                if x == h or y == k:
                    print("Error: The point cannot be on the vertex.")
                    return 0, 0, 0
                a = (y - k) / ((x - h)**2)
                b = -2 * a * h
                c = k + a * h**2
            elif inputMethod == "6":
                print("Enter axis of symmetry x = h and 2 points (x1, y1) and (x2, y2) to calculate the coefficients of the quadratic function.")
                h = float(input("Axis of symmetry x (h): "))
                x1 = float(input("x1: "))
                y1 = float(input("y1: "))
                x2 = float(input("x2: "))
                y2 = float(input("y2: "))
                if x1 == h or x2 == h or y1 == y2:
                    print("Error: Points must have different x, y values and not be on the axis.")
                    return 0, 0, 0
                a = (y2 - y1) / ((x2 - h)**2 - (x1 - h)**2)
                b = -2 * a * h
                c = y1 - a * (x1 - h)**2
            elif inputMethod == "0":
                return self.polinomialInput()
        elif maxDegree == "1":
            inputMethod = input("""
            Choose your method to calculate coefficients:
            1. Provide 2 coefficients (b ≠ 0)
            2. Provide coefficient b and 1 point (b ≠ 0)
            3. Provide 2 points (points must have different x, y values)
            0. Change maximum degree
            Input method: """)
            if inputMethod == "1":
                print("Enter the coefficients for the linear function f(x) = bx + c")
                b = float(input("b = "))
                c = float(input("c = "))
                if b == 0:
                    print("Error: b cannot be 0.")
                    return 0, 0, 0
            elif inputMethod == "2":
                print("Enter coefficient b and 1 point (x, y) to calculate the coefficients of the linear function.")
                b = float(input("b = "))
                if b == 0:
                    print("Error: b cannot be 0.")
                    return 0, 0, 0
                x = float(input("x: "))
                y = float(input("y: "))
                c = y - b * x
            elif inputMethod == "3":
                print("Enter two points (x1, y1) and (x2, y2) to calculate the coefficients of the linear function.")
                x1 = float(input("x1: "))
                y1 = float(input("y1: "))
                x2 = float(input("x2: "))
                y2 = float(input("y2: "))
                if x1 == x2:
                    print("Error: x1 and x2 cannot be the same.")
                    return 0, 0, 0
                b = (y2 - y1) / (x2 - x1)
                c = y1 - b * x1
            elif inputMethod == "0":
                return self.polinomialInput()
        elif maxDegree == "0":
            inputMethod = input("""
            Do you want to:
            1. Continue with constant function (f(x) = c)
            0. Change maximum degree
            Input method: """)
            if inputMethod == "1":
                print("Enter the coefficient for the constant function f(x) = c")
                a, b, c = 0, 0, self.tryInt(input("c = "))
            elif inputMethod == "0":
                return self.polinomialInput()
        else:
            print("Error: Invalid maximum degree.")
        return a, b, c

    def mathOperations(self, a1, b1, c1, a2, b2, c2, fname1, fname2):
        duplicateCondition = a1 == a2 and b1 == b2 and c1 == c2 and fname1 == fname2
        if duplicateCondition:
            inputMethod = input(f"""
                Choose your operation:
                1. a × {fname1}(x) + c
                2. n × [{fname1}(x)]²
                0. Go back
                Operation: """)
        else:
            inputMethod = input(f"""
                Choose your operation:
                1. Addition/Subtraction ( a × {fname1}(x) + b × {fname2}(x) + c)
                2. Multiplication ( n × {fname1}(x) × {fname2}(x) )
                3. Division ( n × {fname1}(x) / {fname2}(x) ) ({fname2}(x) ≠ 0) (not done)
                4. Division ( n × {fname2}(x) / {fname1}(x) ) ({fname1}(x) ≠ 0) (not done)
                0. Go back
                Operation: """)
        if inputMethod == "1":
            a = self.tryInt(input(f"Enter coefficient a for {fname1}(x): "))
            if duplicateCondition:
                b = 0
            else:
                b = self.tryInt(input(f"Enter coefficient b for {fname2}(x): "))
            c = self.tryInt(input(f"Enter free coefficient c: "))
            new_a = a * a1 + b * a2
            new_b = a * b1 + b * b2
            new_c = a * c1 + b * c2 + c
            print(f"Resulting function: {self.formatFunc(new_a, new_b, new_c, 'x')}")
            self.rootFinder(new_a, new_b, new_c, True, a2, b2, c2)
        if inputMethod == "2":
            n = self.tryInt(input("Enter coefficient n: "))
            new_a = n * (a1 * a2)
            new_b = n * (a1 * b2 + b1 * a2)
            new_c = n * (a1 * c2 + b1 * b2 + c1 * a2)
            new_d = n * (b1 * c2 + c1 * b2)
            new_e = n * (c1 * c2)
            print(f"Resulting function: {self.formatFunc(coef4=new_a, coef3=new_b, coef2=new_c, coef1=new_d, coef0=new_e, varName='x')}")
            if a1 != 0:
                discriminant1 = b1**2 - 4*a1*c1
                if discriminant1 >= 0:
                    if discriminant1 > 0:
                        roots1 = [self.tryInt((-b1 - discriminant1**0.5) / (2*a1)), self.tryInt((-b1 + discriminant1**0.5) / (2*a1))]
                    else:
                        roots1 = [self.tryInt(-b1 / (2*a1))]
                else:
                    roots1 = []
            elif b1 != 0:
                roots1 = [self.tryInt(-c1 / b1)]
            elif c1 == 0:
                roots1 = 0
            else:
                roots1 = []
            if a2 != 0:
                discriminant2 = b2**2 - 4*a2*c2
                if discriminant2 >= 0:
                    if discriminant2 > 0:
                        roots2 = [self.tryInt((-b2 - discriminant2**0.5) / (2*a2)), self.tryInt((-b2 + discriminant2**0.5) / (2*a2))]
                    else:
                        roots2 = [self.tryInt(-b2 / (2*a2))]
                else:
                    roots2 = []
            elif b2 != 0:
                roots2 = [self.tryInt(-c2 / b2)]
            elif c2 == 0:
                roots2 = 0
            else:
                roots2 = []
            if n == 0:
                roots1, roots2 = 0, 0
            if roots1 == 0 or roots2 == 0:
                print("Infinite solutions.")
            elif len(roots1) != 0 or len(roots2) != 0:
                solutions = list(set([self.tryInt(self.displayRounded(i)) for i in sorted(roots1 + roots2)]))
                print(f"Solutions:{str(solutions).replace('[', ' ').replace(']', '')}")
            else:
                print("No real solutions.")
        if inputMethod == "3":
            n = self.tryInt(input("Enter coefficient n: "))
            if a2 != 0:
                #c
                a = 0
                b = 0
                c = a1/a2
                rb = b1 - (a1*b2) / a2
                rc = c1 - (a1*c2) / a2
            elif b2 != 0:
                #bx + c
                a = 0
                b = a1/b2
                c = (b1*b2-a1*c2)/(b2*b2)
                rb = 0
                rc = c1 - c2*c
            elif c2 != 0:
                #ax2 + bx + c
                a = a1/c2
                b = b1/c2
                c = c1/c2
                rb = 0
                rc = 0
            else:
                pass
            a, b, c, rb, rc = a*n, b*n, c*n, rb*n, rc*n

    def main(self):
        if len(self.functionList.items()) == 0:
            print("\nLets start with a new function!")
            fname = input("Enter the name of the function (ex: 'f'): ")
            print(f"Defining {fname}(x):")
            a, b, c = self.polinomialInput()
            self.functionList[fname] = (a, b, c)
            print(f"Created function {fname}(x) = {self.formatFunc(a, b, c, 'x')}")
            input("Press Enter to continue...")
            self.main()
        else:
            print(f"\nAvailable functions:")
            for fname, (fa, fb, fc) in self.functionList.items():
                print(f"{fname}(x) = {self.formatFunc(fa, fb, fc, 'x')}")
            inputMethod = input("""
            Choose an operation to perform:
            1. Evaluate function
            2. Get information about function
            3. Redefine existing functions
            4. Define new function
            5. Preform math operations on 2 functions
            6. Delete a function
            0. Exit
            Input method: """)
            if inputMethod == "1":
                if len(self.functionList) > 1:
                    fname = input("Enter the name of the function: ")
                else:
                    fname = list(self.functionList.keys())[0]
                if fname in self.functionList:
                    a, b, c = self.functionList[fname]
                    self.functionEvaluation(a, b, c)
                else:
                    print("Error: Function not found.")
                input("Press Enter to continue...")
                self.main()
            elif inputMethod == "2":
                if len(self.functionList) > 1:
                    fname = input("Enter the name of the function: ")
                else:
                    fname = list(self.functionList.keys())[0]
                if fname in self.functionList:
                    a, b, c = self.functionList[fname]
                    self.functionInfo(a, b, c)
                else:
                    print("Error: Function not found.")
                input("Press Enter to continue...")
                self.main()
            elif inputMethod == "3":
                if len(self.functionList) > 1:
                    fname = input("Enter the name of the function: ")
                else:
                    fname = list(self.functionList.keys())[0]
                if fname in self.functionList:
                    print(f"Redefining {fname}(x):")
                    a, b, c = self.polinomialInput()
                    self.functionList[fname] = (a, b, c)
                    print(f"Redefined function {fname}(x) = {self.formatFunc(a, b, c, 'x')}")
                else:
                    print("Error: Function not found.")
                input("Press Enter to continue...")
                self.main()
            elif inputMethod == "4":
                print("\nDefining a new function!")
                fname = input("Enter the name of the function: ")
                if fname not in self.functionList:
                    print(f"Defining {fname}(x):")
                    a, b, c = self.polinomialInput()
                    self.functionList[fname] = (a, b, c)
                    print(f"Created function {fname}(x) = {self.formatFunc(a, b, c, 'x')}")
                else:
                    print("Error: Function name already exists.")
                input("Press Enter to continue...")
                self.main()
            elif inputMethod == "5":
                print("Function operations are testing.")
                if len(self.functionList) >= 2:
                    fname1 = input("Enter the name of the first function: ")
                    fname2 = input("Enter the name of the second function: ")
                else:
                    print(f"{list(self.functionList.keys())[0]}(x) will be used for both functions")
                    fname1, fname2 = list(self.functionList.keys()) * 2
                if fname1 in self.functionList and fname2 in self.functionList:
                    a1, b1, c1 = self.functionList[fname1]
                    a2, b2, c2 = self.functionList[fname2]
                    self.mathOperations(a1, b1, c1, a2, b2, c2, fname1, fname2)
                else:
                    print("Error: One or both functions not found.")
                input("Press Enter to continue...")
                self.main()
            elif inputMethod == "6":
                fname = input("Enter the name of the function to delete: ")
                if fname in self.functionList:
                    del self.functionList[fname]
                    print(f"Deleted function {fname}(x).")
                else:
                    print("Error: Function not found.")
                input("Press Enter to continue...")
                self.main()
            elif inputMethod == "0":
                print("Exiting the program.")
                exit()
            else:
                print("Error: Invalid input.")
                self.main()