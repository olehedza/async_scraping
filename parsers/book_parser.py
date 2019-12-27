import re
import logging

from locators.book_locators import BookLocators

logger = logging.getLogger('scraping.book_parser')


class BookParser:
    """
    Given one of the quote divs,
    find out the data about the quote
    """

    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self, parent):
        logger.debug(f'New book parser created from `{parent}`.')
        self.parent = parent

    @property
    def name(self):
        logger.debug('Find book name...')
        locator = BookLocators.NAME
        item_link = self.parent.select_one(locator)
        item_name = item_link.attrs['title']
        logger.debug(f'Found book name, `{item_name}`.')
        return item_name

    @property
    def link(self):
        logger.debug('Finding book link...')
        locator = BookLocators.LINK
        item_link = self.parent.select_one(locator).attrs['href']
        logger.debug('Found book link, `{item_link}`.')
        return item_link

    @property
    def price(self):
        logger.debug('Finding book name...')
        locator = BookLocators.PRICE
        item_price = self.parent.select_one(locator).string

        pattern = '£([0-9]+\.[0-9]+)'
        matcher = re.search(pattern, item_price)
        float_price = float(matcher.group(1))
        logger.debug(f'Found book price, `{float_price}`.')
        return float_price

    @property
    def rating(self):
        logger.debug('Finding book rating...')
        locator = BookLocators.RATING
        star_rating_tag = self.parent.select_one(locator)
        classes = star_rating_tag.attrs['class']
        rating_classes = [r for r in classes if r != 'star-rating']
        rating_number = BookParser.RATINGS.get(rating_classes[0])
        logger.info('Found book rating, `{rating_number}`.')
        return rating_number

    def __repr__(self):
        return f'<Book {self.name}, £{self.price} ({self.rating} stars)>'
