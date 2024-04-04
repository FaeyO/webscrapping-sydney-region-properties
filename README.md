# Domain.com.au Commercial Real Estate Web Scraping

This project involves web scraping commercial real estate listings from the Domain.com.au website using the Scrapy framework. The scraped data includes the name of the apartment, location, description, agent contact, and website.

## Project Overview

The goal of this project is to extract commercial real estate listings data from Domain.com.au for further analysis or integration into other applications.

## Installation

1. Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/domain-commercial-real-estate-scraper.git
```

2. Install Scrapy if you haven't already:

```bash
pip install scrapy
```

## Usage

1. Navigate to the project directory:

```bash
cd domain-commercial-real-estate-scraper
```

2. Run the Scrapy spider:

```bash
scrapy crawl domain_commercial -o output.json
```

This command will execute the Scrapy spider named `domain_commercial` and save the scraped data to a JSON file named `output.json`.

## Project Structure

The project structure is organized as follows:

```
domain-commercial-real-estate-scraper/
│
├── domain_commercial/
│   ├── __init__.py
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── settings.py
│   └── spiders/
│       ├── __init__.py
│       └── domain_commercial_spider.py
│
├── README.md
└── scrapy.cfg
```

- `domain_commercial/`: Contains the Scrapy project files.
- `domain_commercial/items.py`: Defines the data items to be scraped.
- `domain_commercial/middlewares.py`: Contains custom middleware settings.
- `domain_commercial/pipelines.py`: Defines the pipeline for processing scraped data.
- `domain_commercial/settings.py`: Contains project settings such as user agents and pipeline settings.
- `domain_commercial/spiders/`: Directory containing Scrapy spiders.
- `domain_commercial/spiders/domain_commercial_spider.py`: Scrapy spider for scraping commercial real estate listings from Domain.com.au.
- `scrapy.cfg`: Scrapy configuration file.
- `README.md`: This file, providing an overview of the project and instructions for usage.

## Data Fields

The following fields are extracted for each commercial real estate listing:

- `name`: Name or title of the apartment.
- `location`: Location or address of the apartment.
- `description`: Description of the apartment.
- `agent_contact`: Contact information of the agent.
- `website`: Website URL of the commercial real estate listing.

## Data Output

The scraped data is saved to a JSON file named `output.json` in the project directory.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## Contact

For questions or inquiries, please contact [FaeyO](mailto:foyinbo250@gmail.com).

---

Replace `yourusername` in the clone command with your GitHub username.

### website view

![image](https://github.com/FaeyO/webscrapping-sydney-region-properties/assets/118575325/4ab78e0f-b1df-4b76-9818-5568e08e2d7f)
