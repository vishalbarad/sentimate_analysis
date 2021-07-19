import scrapy


class ExtractReviewsSpider(scrapy.Spider):
    name = 'extract_reviews'
    allowed_domains = ['www.amazon.in']
    start_urls = ['https://www.amazon.in/OnePlus-Nord-Blue-128GB-Storage/product-reviews/B095PYTSV8/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews']

    # def parse(self, response):
    #     reviews_list = list()
    #     ratings_list = list()
    #     reviews = response.xpath("//div[@class='a-row a-spacing-small review-data']//span[@class='a-size-base review-text review-text-content']//span//text()").getall()
    #     ratings = response.xpath("//i[@class='a-icon a-icon-star a-star-5 review-rating']//span[@class='a-icon-alt']//text()").getall()
    #
    #     for review in reviews:
    #         reviews_list.append(review)
    #
    #     for rating in ratings:
    #         ratings_list.append(rating)
    #
    #     yield {"Reviews":reviews_list,
    #            "Ratings":ratings_list}
    #
    #     next_page = response.css("ul.a-pagination li.a-last a::attr(href)").get()
    #
    #     if next_page:
    #         yield response.follow(url=next_page,callback=self.parse)

    def parse(self, response):

        for review in response.xpath("//div[@class='a-section celwidget']"):

            user_rating = review.xpath(".//div[@class='a-row']//span[@class='a-icon-alt']/text()").get()

            user_review = review.xpath(".//div[@class='a-row a-spacing-small review-data']//span[@class='a-size-base review-text review-text-content']//span/text()").get()

            yield {'Reviews':user_review,
                   'Ratings':user_rating}

        next_page = response.css("ul.a-pagination li.a-last a::attr(href)").get()

        if next_page:
            yield response.follow(url=next_page,callback=self.parse)

