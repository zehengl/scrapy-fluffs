# scrapy-fluffs

Scraping images from [Fluff Images](http://majorclanger.co.uk/fluffimagesf.htm)

## Usage

    git clone git@github.com:zehengl/scrapy-fluffs.git
    cd scrapy-fluffs
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    cd fluffs
    scrapy crawl images

Crawled images are available at `scrapy-fluffs/images/full`
