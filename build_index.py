#!/usr/bin/env python3
"""
Generate index.html from tutorials.yaml
"""

import yaml

def load_tutorials():
    """Load tutorials from YAML file."""
    with open('tutorials.yaml', 'r') as f:
        data = yaml.safe_load(f)
    return data['tutorials']

def generate_html(tutorials):
    """Generate HTML content from tutorials."""
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bioinformatics Tutorials</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            line-height: 1.6;
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .container {
            background-color: white;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        h1 {
            color: #333;
            border-bottom: 3px solid #0066cc;
            padding-bottom: 10px;
        }
        .intro {
            color: #555;
            margin: 20px 0 40px 0;
            font-size: 1.1em;
        }
        .tutorial {
            margin: 30px 0;
            padding: 20px;
            background-color: #f9f9f9;
            border-left: 4px solid #0066cc;
            border-radius: 4px;
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .tutorial:hover {
            transform: translateX(5px);
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        .tutorial h2 {
            margin-top: 0;
            color: #0066cc;
            font-size: 1.4em;
        }
        .tutorial .date {
            color: #888;
            font-size: 0.9em;
            margin: 10px 0;
            font-style: italic;
        }
        .tutorial .description {
            color: #444;
            margin: 15px 0;
            line-height: 1.7;
        }
        .tutorial a {
            display: inline-block;
            margin-top: 10px;
            padding: 10px 20px;
            background-color: #0066cc;
            color: white;
            text-decoration: none;
            border-radius: 4px;
            transition: background-color 0.3s;
            font-weight: 500;
        }
        .tutorial a:hover {
            background-color: #0052a3;
        }
        footer {
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #ddd;
            text-align: center;
            color: #666;
        }
        footer a {
            color: #0066cc;
            text-decoration: none;
        }
        footer a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Bioinformatics Tutorials</h1>
        <p class="intro">A collection of reproducible workflows and documentation for bioinformatics analyses.</p>
"""

    for tutorial in tutorials:
        html += f"""
        <div class="tutorial">
            <h2>{tutorial['title']}</h2>
            <div class="date">{tutorial['date']}</div>
            <div class="description">{tutorial['description']}</div>
            <a href="{tutorial['filename']}">View Tutorial →</a>
        </div>
"""

    html += """
        <footer>
            <p>Generated from RMarkdown files | <a href="https://github.com/cfmasarweh/Tutorials">View on GitHub</a></p>
        </footer>
    </div>
</body>
</html>
"""

    return html

def main():
    """Main function to build index.html from tutorials.yaml."""
    print("Building index.html from tutorials.yaml...")

    # Load tutorials
    tutorials = load_tutorials()
    print(f"Found {len(tutorials)} tutorials")

    # Generate HTML
    html = generate_html(tutorials)

    # Write to index.html
    with open('index.html', 'w') as f:
        f.write(html)

    print("✓ index.html successfully generated!")

if __name__ == '__main__':
    main()
