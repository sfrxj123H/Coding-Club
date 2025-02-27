def inputList(text, task=2):
    try:
        eval(text)
    except:
        while text[0] == " ":
            text = text[1:]
        text = '"' + text
        while text[-1] == " ":
            text = text[:-1]
        text = text + '"'
        while text.find(",") > -1:
            while text[text.find(",")-1] == " ":
                text1 = text[:text.find(",") - 1]
                text2 = text[text.find(","):]
                text = text1 + text2
            while text[text.find(",")+1] == " ":
                text1 = text[:text.find(",") + 1]
                text2 = text[text.find(",") + 2:]
                text = text1 + text2
            text = text[:text.find(",")] + '"' + "*_*" + '"' + text[text.find(",") + 1:]
        for i in range(len(text) - 3):
            if text[i:i+3] == "*_*":
                text = text[:i] + "," + text[i+3:]
    try:
        data = list(eval(text + ", 1"))[:-1]
        if task == 1:
            print(sum(data))    # Sum of all numbers in list
            sum_data = 0
            for i in data:
                sum_data += i
            # print(sum_data)   # Another method
        elif task == 2:
            print(data)   # Show list
        elif task == 3:
            print(max(data))    # Show max number in list
        elif task == 4:
            print(len(data))    # Show length of list
        else:
            print("Error! Task not found!")
    except:
        print("Error! List error!")


inputList(input("List: "), int(input("Task: ")))
