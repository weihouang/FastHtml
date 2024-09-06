from fasthtml.common import *



custom_css = """
    body {
        font-family: 'Arial', sans-serif;
        background-color: #f0f0f0;
        margin: 0;
        padding: 0;
        height: 100vh;
    }
    header {
        background-color: #333;
        padding: 20px;
        text-align: center;
        border-radius: 10px;

    }
    header nav ul {
        list-style-type: none;
        margin: 0;
        padding: 0;

    }
    header nav ul li {
        display: inline;
        margin-right: 20px;

    }
    header nav ul li a {
        color: white;
        text-decoration: none;
        font-weight: bold;

    }
    header nav ul li a:hover {
        color: #ff6600;


    }
    section {
        margin: 20px auto;
        padding: 20px;
        max-width: 800px;
        background-color: white;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        border-radius: 10px;


    }
    h2, h3 {
        color: #333;

    }
    footer {
        text-align: center;
        padding: 10px;
        background-color: #333;
        color: white;
        position: fixed;
        bottom: 0;
        width: 100%;

    }
"""




app, rt = fast_app(hdrs=(Style(custom_css),))

def header():
    return Header(
        Nav(Ul(
            Li(A(href="/")("Home")),
            Li(A(href="/about")("About")),
            Li(A(href="/portfolio")("Portfolio")),
            Li(A(href="/contact")("Contact"))
        ))
    )

def footer():
    return 

@rt("/")
def home():
    return Titled("Welcome to My Website",
                  Div(
                      header(),
                      Section(H2("Hi, I'm Weiho"), P("A software developer!")),
                      Section(H3("Latest Projects"), 
                              P("Check out my portfolio to see what I've been working on.")),
                      footer()
                  ))

@rt("/about")
def about():
    return Titled("About Me",
                  Div(
                      header(),
                      Section(H2("About Me"),
                              P("I have a background in software engineering, with a focus on web and game development. My favorite languages are Python and Java. "
                                "I enjoy creating apps and learning new technologies.")),
                      footer()
                  ))

@rt("/portfolio")
def portfolio():
    return Titled("My Projects",
                  Div(
                      header(),
                      Section(H2("Portfolio"),
                              P("Here are some of the projects I've worked on:"),
                              Ul(
                                  Li(A(href="https://github.com/weihouang")("GitHub Profile")),
                                  Li(A(href="https://github.com/weihouang/FastHtml")("Project 1 - FastHtml")),
                                  Li(A(href="https://weihouang.com")("Project 2 - Personal Website"))
                              )),
                      footer()
                  ))

@rt("/contact")
def contact():
    return Titled("Contact Me",
                  Div(
                      header(),
                      Section(H2("Get in Touch"),
                              P("Email: willy200335@gmail.com")),
                      footer()
                  ))

@rt("/project/{title}/{description}/{tech}")
def project(title: str, description: str, tech: str):
    return Titled(f"Project: {title}",
                  Div(
                      header(),
                      Section(H2(f"Project: {title}"),
                              P(f"Description: {description}"),
                              P(f"Technologies used: {tech}")),
                      footer()
                  ))

# Running the server

serve()

