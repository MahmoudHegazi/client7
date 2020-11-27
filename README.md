https://eshop.tesco.com.my/groceries/en-GB/shop/fresh-food/all (30)
https://eshop.tesco.com.my/groceries/en-GB/shop/grocery/all (128)
https://eshop.tesco.com.my/groceries/en-GB/shop/baby/all (26)
https://eshop.tesco.com.my/groceries/en-GB/shop/chilled-and-frozen/all (23)
https://eshop.tesco.com.my/groceries/en-GB/shop/drinks/all (32)
https://eshop.tesco.com.my/groceries/en-GB/shop/health-and-beauty/all (95)
https://eshop.tesco.com.my/groceries/en-GB/shop/household/all (48)
https://eshop.tesco.com.my/groceries/en-GB/shop/pets/all (6)
https://eshop.tesco.com.my/groceries/en-GB/shop/non-food-and-gifting/all (72)


(image) 
```python
response.xpath("//img[@class='product-image']/@src").extract()

response.xpath("//a[@class='pagination--button']/@href").extract()

response.xpath("//*[@class="pagination--button"]/a/@href").extract()

scrapy shell "https://eshop.tesco.com.my/groceries/en-GB/shop/non-food-and-gifting/all"
//*[@id="product-list"]/div[2]/div[5]/nav/ul/li[7]/a

response.xpath("//*[@id="product-list"]/div[2]/div[5]/nav/ul/li[7]/a/@href").extract()

response.xpath("//*[@class="pagination--button"]/a/@href").extract()

pagination--button
//*[@id="product-list"]/div[2]/div[5]/nav/ul/li[7]/a

<img src="https://secure.ap-tescoassets.com/assets/MY/208/9555067700208/ShotType1_225x225.jpg" alt="IK Yellow A4 Multifunction Business
 Paper 70gsm 450 Sheets" class="product-image" srcset="https://secure.ap-tescoassets.com/assets/MY/208/9555067700208/ShotType1_90x90.jpg 768w,https://secure.ap-tescoassets.com/assets/MY/208/9555067700208/ShotType1_225x225.jpg 4000w">


a.pagination--button.prev-next


product-tile--title
response.xpath('//title/text()').get()

response.xpath('//a[contains(@data-auto, "product-tile--title")]/@href').getall()



// proudct URL
response.xpath('//a[contains(@data-auto, "product-tile--title")]/@href').getall()


response.xpath('//a[contains(@data-auto, "product-tile--title")]/text()').getall()
```
