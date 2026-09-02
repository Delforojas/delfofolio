from django.shortcuts import render, HttpResponse


TECHNOLOGY_CATEGORIES = (
    {
        "slug": "lenguajes-frameworks",
        "name": "Lenguajes y Frameworks",
        "technologies": (
            {"name": "Python", "icon": "python", "color": "#3776ab"},
            {"name": "Django", "icon": "django", "color": "#44b78b"},
            {"name": "JavaScript", "icon": "javascript", "color": "#f7df1e"},
            {"name": "TypeScript", "icon": "typescript", "color": "#3178C6"},
            {"name": "PHP", "icon": "php", "color": "#777BB4"},
            {"name": "Symfony", "icon": "symfony", "color": "#000000"},
            {"name": "Angular", "icon": "angular", "color": "#E10606"},

        ),
    },
    {
        "slug": "frontend-diseno",
        "name": "Frontend y Diseño",
        "technologies": (
            {"name": "HTML5", "icon": "html5", "color": "#e34f26"},
            {"name": "CSS3", "icon": "css", "color": "#663399"},
            {"name": "Bootstrap", "icon": "bootstrap","color":"#7952b3"},
        ),
    },
    {

    "slug": "databases",

    "name": "Databases",

    "technologies": (

        {"name": "SQL", "icon": "sql", "color": "#ff9d4d"},

        {"name": "PostgreSQL", "icon": "postgresql", "color": "#4169E1"},

        {"name": "MySQL", "icon": "mysql", "color": "#4479A1"},

    ),

},

{

    "slug": "analytics-bi",

    "name": "Analytics & BI",

    "technologies": (

        {"name": "Power BI", "icon": "power-bi", "color": "#f2c811"},

        {"name": "Power Query", "icon": "power-query", "color": "#1e8bcd"},

        {"name": "DAX", "icon": "dax", "color": "#f2c811"},

    ),

},

{

    "slug": "python-data-stack",

    "name": "Python Data Stack",

    "technologies": (

        {"name": "Pandas", "icon": "pandas", "color": "#e70488"},

        {"name": "NumPy", "icon": "numpy", "color": "#4dabcf"},

        {"name": "Matplotlib", "icon": "matplotlib", "color": "#73d2de"},

        {"name": "Scikit-learn", "icon": "scikitlearn", "color": "#F7931E"},

    ),

},
    {
        "slug": "herramientas-entornos",
        "name": "Herramientas y Entornos",
        "technologies": (
            {"name": "Git", "icon": "git", "color": "#f05032"},
            {"name": "GitHub", "icon": "github", "color": "#ffffff"},
            {"name": "Docker", "icon": "docker", "color": "#2496ed"},
            {"name": "Anaconda", "icon": "anaconda", "color": "#44A833"},
            {"name": "Visual Studio Code", "icon": "visual-studio-code", "color": "#007acc"},
            {"name": "Postman", "icon": "postman", "color": "#ff6c37"},
            {"name": "phpMyAdmin", "icon": "phpmyadmin", "color": "#6C78AF"},
        ),
    },

{

    "slug": "ai-agentic-development",

    "name": "AI & Agentic Development",

    "technologies": (

        {"name": "OpenCode", "icon": "opencode", "color": "#FFFFFF"},

        {"name": "OpenAI", "icon": "openai", "color": "#FFFFFF"},

        {"name": "MCP", "icon": "modelcontextprotocol", "color": "#FFFFFF"},

        {"name": "Agent Skills", "icon": "agentskills", "color": "#FFFFFF"},

    ),

},
)


html_base= """
<h1>Mi Web Personal</h1>
    <ul>    
        <li><a href="/">Portada</a></li>
        <li><a href="/about-me/">Acerca de</a></li>
        <li><a href="/portfolio/">Portafolio</a></li>
        <li><a href="/contact/">Contacto</a></li>
    </ul>
"""

# Create your views here.
def home(request):
    return render(request, "core/home.html")
        
def about(request):
    return render(request, "core/about.html")


def tecnologias(request):
    return render(
        request,
        "core/tecnologias.html",
        {"technology_categories": TECHNOLOGY_CATEGORIES},
    )


def contact(request):
    return render(request, "core/contact.html")
