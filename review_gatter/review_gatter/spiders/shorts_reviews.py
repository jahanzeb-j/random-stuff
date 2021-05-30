import scrapy
import itertools


class ShortsReviewsSpider(scrapy.Spider):
    name = 'shorts_reviews'
    #allowed_domains = ['www.shortsground.com'
     #                  ]  #www.shopclues.com/mens-shirts.html'
    #]  #www.shortsground.com/']
    start_urls = ['file:///C:/Users/jjabbar/Desktop/reviews.html'] #['https://www.shortsground.com/wp-admin/admin-ajax.php?action=woocommerce_photo_reviews_shortcode_ajax_get_reviews/']

    #location of csv file
    custom_settings = {'FEED_URI': 'reviews5.csv', 'FEED_FORMAT': 'csv'}

    def parse(self, response):
        #Extract product information
        review = response.xpath(
            '//div[@class="shortcode-wcpr-content"]/div[@class="shortcode-review-content-container"]/div[@class="shortcode-wcpr-review-content"]/text()'
        ).extract()  #response.css('img::attr(title)').extract()
        print(review)
        #images = response.css('img::attr(data-src)').extract()
        images = response.xpath(
            '//div[@class="shortcode-wcpr-content"]/div[@class="shortcode-reviews-images-container"]/div[@class="shortcode-reviews-images-wrap-right"]/img/@data-original_src'
        ).extract()
        print(images)
        reviewerName = response.xpath(
            '//div[@class="shortcode-wcpr-content"]/div[@class="shortcode-review-content-container"]/div[@class="shortcode-review-content-container-top"]/div[@class="shortcode-review-content-container-top-right"]/div[@class="shortcode-wcpr-comment-author"]/text()'
        ).extract()
        print(reviewerName)
        reviewDate = response.xpath(
            '//div[@class="shortcode-wcpr-content"]/div[@class="shortcode-review-content-container"]/div[@class="shortcode-review-content-container-top"]/div[@class="shortcode-review-content-container-top-right"]/div[@class="wcpr-review-rating"]/div[@class="wcpr-review-date"]/text()'
        ).extract()
        print(reviewDate)

        zipped = itertools.zip_longest(review, images,reviewerName,reviewDate, fillvalue='https://shortsground.com/wp-content/uploads/2021/01/d8550898951b06af316d28958bc5631b.jpg')

        for item in zipped:
            scraped_info = {
                'review': item[0],
                'image_urls': [item[1]],
                'name': item[2],
                'date': item[3],
            }
            yield scraped_info
        # NEXT_PAGE_SELECTOR = '.wcpr-current + a::attr(href)'
        # next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        # if next_page:
        #     yield scrapy.Request(
        #     response.urljoin(next_page),
        #     callback=self.parse)
