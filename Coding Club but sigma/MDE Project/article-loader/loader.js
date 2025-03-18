export function loader(key, toQuerySelector) {
    if (key == "math-k&g1") {
        let docAdd = ""
        docAdd += "<a href='../math/k-and-G1/numbers'><h3>Numbers</h3></a>"
        docAdd += "<a href='../math/k-and-G1/addition-and-subtraction'><h3>Addition and Subtraction</h3></a>"
        docAdd += "<a href='../math/k-and-G1/before-solving-quizzes'><h3>Before solving quizzes</h3></a>"
        docAdd += "<a href='../math/k-and-G1/quiz/addition-and-subtraction'><h3>Quiz: Solving basic additions and subtractions" + 
        (localStorage.getItem("quiz-addition-and-subtraction") == "true" ? " (Completed)" : "") +
        "</h3></a>"
        document.querySelector(toQuerySelector).innerHTML = docAdd
    }
    else if (key == "dev-tools") {
        let docAdd = ""
        docAdd += "<a href='../dev-tools/sources.html'><h3>Sources</h3></a>"
        docAdd += "<a href='../dev-tools/changelog.html'><h3>Change Log</h3></a>"
        document.querySelector(toQuerySelector).innerHTML = docAdd
    }
    else {
        document.querySelector(toQuerySelector).innerHTML = ""
    }

}