from fastapi import FastAPI, Request, Form
import uvicorn
from fastapi.responses import HTMLResponse
from calc_func import result

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def get_answer():
    return """
    <html lang="en">
  <head>
  </head>
  <body>
    <form action="/submit" method="post">
      <label for="">Input:</label>
      <input type="text" name="expression" placeholder="enter the expression" />
      <input type="submit" value="Send" >
    </form>
  </body>
</html>

"""


@app.post("/submit", response_class=HTMLResponse)
async def submit_form(expression: str = Form(...)):

    number = []
    operator = []
    num = ""

    for char in expression:
        if char.isdigit():
            num += char
        else:
            if num != "":
                number.append(num)
                num = ""
            if char in "+-*/":
                operator.append(char)

    if num != "":
        number.append(num)

    output = result(number, operator)

    return f"""
    <html>
    <body>
        <h2>Result: {output}</h2>   
        <a href="/">Go Back</a>
    </body>
    </html>
    """
