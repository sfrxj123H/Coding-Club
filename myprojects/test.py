#6.25 and 56
def tryInt(value):
    return int(value) if value == int(value) else value

def d(value):
    return round(value, 6)
    
def formatFunc(coef2, coef1, coef0, varName, factoredFormat=False, coef4=0, coef3=0):
    output = ""
    if coef4 != 0:
        if coef4 == 1:
            output += f"{varName}⁴"
        elif coef4 == -1:
            output += f"-{varName}⁴"
        else:
            output += f"{tryInt(coef4)}{varName}⁴"
    if coef3 != 0:
        if coef4 != 0:
            if coef3 > 0:
                output += " + "
            else:
                output += " - "
        else:
            if coef3 < 0:
                output += "-"
        if abs(tryInt(coef3)) == 1:
            output += f"{varName}³"
        else:
            output += f"{abs(tryInt(coef3))}{varName}³"
    if coef2 != 0:
        if coef4 != 0 or coef3 != 0:
            if coef2 > 0:
                output += " + "
            else:
                output += " - "
        else:
            if coef2 < 0:
                output += "-"
        if abs(tryInt(coef2)) == 1:
            output += f"{varName}²"
        else:
            output += f"{abs(tryInt(coef2))}{varName}²"
    if coef1 != 0:
        if coef4 != 0 or coef3 != 0 or coef2 != 0:
            if coef1 > 0:
                output += " + "
            else:
                output += " - "
        else:
            if coef1 < 0:
                output += "-"
        if abs(tryInt(coef1)) == 1:
            output += f"{varName}"
        else:
            output += f"{abs(tryInt(coef1))}{varName}"
    if coef2 == 0 and coef1 == 0:
        output += f"{tryInt(coef0)}"
    elif coef0 != 0:
        if coef4!= 0 or coef3!= 0 or coef2 != 0 or coef1 != 0:
            output += " "
        if coef0 > 0:
            output += f"+ {tryInt(coef0)}"
        else:
            output += f"- {abs(tryInt(coef0))}"
    if int(coef4 == 0) + int(coef3 == 0) + int(coef2 == 0) + int(coef1 == 0) + int(coef0 == 0) < 4 and factoredFormat:
        output = "(" + output + ")"
    return output

def isSquaredRootRational(num):
    num2 = num
    dem = 1
    while int(num2) != num2:
        num2 *= 10
        dem *= 10
    num2r = int(num2 ** 0.5)
    demr = int(dem ** 0.5)
    return num2r * num2r == num2 and demr * demr == dem

def rootFinder(a, b, c, isIntersect=False, intersect_a=0, intersect_b=0, intersect_c=0):
    if a != 0:
        print("Type: Quadratic function")
        discriminant = tryInt(b**2 - 4*a*c)
        print(f"Discriminant: Δ = {discriminant}")
        if discriminant > 0:
            roots = [tryInt((-b - discriminant**0.5) / (2*a)), tryInt((-b + discriminant**0.5) / (2*a))]
            if abs(roots[0]) > abs(roots[1]):
                roots = roots[::-1]
            root1 = min(roots)
            root2 = max(roots)
            if isSquaredRootRational(discriminant):
                print(f"Roots: x₁ = {d(root1)}, x₂ = {d(root2)}")
                print(f"Factored form: {formatFunc(0, a, -a*roots[0], 'x', 1)}{formatFunc(0, 1, -roots[1], 'x', 1)}")
            else:
                ddiscriminant = discriminant
                ddenominator = tryInt(abs(2*a))
                for i in range(tryInt(abs(2*a)), 1, -1):
                    if ddiscriminant % (i*i) == 0 and ddenominator % i == 0:
                        ddiscriminant = tryInt(ddiscriminant // (i*i))
                        ddenominator = tryInt(ddenominator // i)
                droot1 = f"{d(tryInt(-b / (2*a)))} - √{ddiscriminant}{' /' + str(ddenominator) if ddenominator != 1 else ''}"
                droot2 = f"{d(tryInt(-b / (2*a)))} + √{ddiscriminant}{' /' + str(ddenominator) if ddenominator != 1 else ''}"
                fd1 = f"- √{ddiscriminant}{' /' + str(ddenominator) if ddenominator != 1 else ''}"
                fd2 = f"+ √{ddiscriminant}{' /' + str(ddenominator) if ddenominator != 1 else ''}"
                print(f"Roots: x₁ = {droot1}, x₂ = {droot2}")
                print(f"Factored form: {formatFunc(0, a, 0, '', 1)}({formatFunc(0, 1, -tryInt(-b / (2*a)), 'x')} {fd1})({formatFunc(0, 1, -tryInt(-b / (2*a)), 'x')} {fd2})")
        elif discriminant == 0:
            root = tryInt(-b / (2*a))
            roots = [root]
            print(f"Root: x = {root}")
            print(f"Factored form: {formatFunc(0, a, 0, '', 1)}{formatFunc(0, 1, -root, 'x', 1)}²")
        else:
            roots = []
            print("Roots: No real roots.")
    elif b != 0:
        root = tryInt(-c / b)
        roots = [root]
        print(f"Root: x = {root}")
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
                    intersect_roots.append((x, tryInt(intersect_a*x**2 + intersect_b*x + intersect_c)))
                dprint = ""
                for x, y in intersect_roots:
                    dprint += f"({d(x)}, {d(y)}), "
                print(f"Intersection{'s' if len(intersect_roots) > 1 else ''}: {dprint[:-2]}")

def mathOperations(a1, b1, c1, a2, b2, c2, fname1, fname2):
    inputMethod = input(f"""
        Choose your operation:
        1. Addition/Subtraction ( a × {fname1}(x) + b × {fname2}(x) )
        2. Multiplication ( n × {fname1}(x) × {fname2}(x) )
        3. Division ( n × {fname1}(x) / {fname2}(x) ) ({fname2}(x) ≠ 0) (not done)
        4. Division ( n × {fname2}(x) / {fname1}(x) ) ({fname1}(x) ≠ 0) (not done)
        0. Go back
        Input method: """)
    if inputMethod == "1":
        a = tryInt(float(input(f"Enter coefficient a for {fname1}(x): ")))
        b = tryInt(float(input(f"Enter coefficient b for {fname2}(x): ")))
        new_a = a * a1 + b * a2
        new_b = a * b1 + b * b2
        new_c = a * c1 + b * c2
        print(f"Resulting function: {formatFunc(new_a, new_b, new_c, 'x')}")
        rootFinder(new_a, new_b, new_c, True, a2, b2, c2)
    if inputMethod == "2":
        n = tryInt(float(input("Enter coefficient n: ")))
        new_a = n * (a1 * a2)
        new_b = n * (a1 * b2 + b1 * a2)
        new_c = n * (a1 * c2 + b1 * b2 + c1 * a2)
        new_d = n * (b1 * c2 + c1 * b2)
        new_e = n * (c1 * c2)
        print(f"Resulting function: {formatFunc(coef4=new_a, coef3=new_b, coef2=new_c, coef1=new_d, coef0=new_e, varName='x')}")
        if a1 != 0:
            discriminant1 = b1**2 - 4*a1*c1
            if discriminant1 >= 0 >= 0:
                roots1 = []
                if discriminant1 > 0:
                    roots1 = [d(tryInt((-b1 - discriminant1**0.5) / (2*a1))), d(tryInt((-b1 + discriminant1**0.5) / (2*a1)))]
                elif discriminant1 == 0:
                    roots1 = [d(tryInt(-b1 / (2*a1)))]
        elif b1 != 0:
            roots1 = [d(tryInt(-c1 / b1))]
        elif c1 == 0:
            roots1 = 0
        else:
            roots1 = []
        if a2 != 0:
            discriminant2 = b2**2 - 4*a2*c2
            if discriminant2 >= 0:
                roots2 = []
                if discriminant2 > 0:
                    roots2 = [d(tryInt((-b2 - discriminant2**0.5) / (2*a2))), d(tryInt((-b2 + discriminant2**0.5) / (2*a2)))]
                elif discriminant2 == 0:
                    roots2 = [d(tryInt(-b2 / (2*a2)))]
        elif b2 != 0:
            roots2 = [d(tryInt(-c2 / b2))]
        elif c2 == 0:
            roots2 = 0
        else:
            roots2 = []
        print(roots1, roots2)
        if roots1 == 0 or roots2 == 0:
            print("Infinite solutions.")
        elif len(roots1) != 0 or len(roots2) != 0:
            solutions = sorted(list(set(roots1 + roots2)))
            print(f"Solutions:{str(solutions).replace('[', ' ').replace(']', '')}")
        else:
            print("No real solutions.")

a, b, c, d, e = 0, 0, 0, 1, 0
print(int(a == 0) + int(b == 0) + int(c == 0) + int(d == 0) + int(e == 0))
# print(formatFunc(a = a, b = b, c = c, d = d, e = e, varName = "x", factoredFormat=False))
mathOperations(1, 2, 1, 1, -3, 2, "f", "g")