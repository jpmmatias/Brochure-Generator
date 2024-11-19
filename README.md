# Company Brochure Generator

An automated tool that generates professional company brochures in markdown format by scraping company websites and utilizing AI to create compelling content.

## Features

- Scrapes company websites for relevant information
- Generates professional brochures in markdown format
- Automatically extracts and validates important company links
- Uses OpenAI's GPT models for content generation
- Supports custom company names and URLs

## Prerequisites

- Python 3.x
- OpenAI API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/jpmmatias/Brochure-Generator.git
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Create a `.env` file in the root directory and add your OpenAI API key:
```bash
OPENAI_API_KEY=<your_openai_api_key>
```


## Usage

Run the main script:
```bash
python main.py
```

Follow the prompts to:
1. Enter the company name
2. Provide the company's website URL
3. Choose whether to generate a markdown file

The generated brochure will include:
- Company overview
- Vision and mission
- Company culture
- Products/Services
- Contact information
- Relevant links (About, Careers, etc.)

## Project Structure

- `main.py` - Entry point of the application
- `OpenAi.py` - OpenAI service integration
- `Website.py` - Web scraping and content extraction
- `Brouchure.py` - Brochure generation logic

## Dependencies

- requests - For web scraping
- python-dotenv - Environment variable management
- beautifulsoup4 - HTML parsing
- openai - OpenAI API integration

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.


