from promptly import render

result = render("examples/prompts/hello.j2", time="HELLO")
print(result)
