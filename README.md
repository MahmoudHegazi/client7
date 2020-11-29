https://eshop.tesco.com.my/groceries/en-GB/shop/fresh-food/all (30)
https://eshop.tesco.com.my/groceries/en-GB/shop/grocery/all (128)
https://eshop.tesco.com.my/groceries/en-GB/shop/baby/all (26)
https://eshop.tesco.com.my/groceries/en-GB/shop/chilled-and-frozen/all (23)
https://eshop.tesco.com.my/groceries/en-GB/shop/drinks/all (32)
https://eshop.tesco.com.my/groceries/en-GB/shop/health-and-beauty/all (95)
https://eshop.tesco.com.my/groceries/en-GB/shop/household/all (48)
https://eshop.tesco.com.my/groceries/en-GB/shop/pets/all (6)
https://eshop.tesco.com.my/groceries/en-GB/shop/non-food-and-gifting/all (72)


## my new IDEA create search engine can search for all domains in world and add them to it better than google without complex code
1. first step found how website like goDady knows is the domain exist or not get the list then search in it

## how to create search engine:
https://support.google.com/programmable-search/answer/4513882?hl=en

###### scrapy good tool but can not used inside my restful API + you can not run using python keword should be scrapy and thats problem

becuase it's mother fucker site use this code
https://stackoverflow.com/questions/38215148/python-requests-get-takes-a-long-time-to-respond-to-some-requests

override_images:
https://stackoverflow.com/questions/60280208/python-beautifulsoup-scraper-not-scraping-images

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


```sheel
>>> response.xpath('//a[contains(@data-auto, "product-tile--title")]/@href').getall()
['/groceries/en-GB/products/7004064879', '/groceries/en-GB/products/7003939332', '/groceries/en-GB/products/7004261216', '/groceries/en-GB/products/7072786078', '/groceries/en-GB/products/7072786086', '/groceries/en-GB/products/7072537124', '/groceries/en-GB/products/7073929697', '/groceries/en-GB/products/7072537590', '/groceries/en-GB/products/7070941122', '/groceries/en-GB/products/7004291433', '/groceries/en-GB/products/7070941130', '/groceries/en-GB/products/7003387925', '/groceries/en-GB/products/7001278541', '/groceries/en-GB/products/7073916536', '/groceries/en-GB/products/7003387933', '/groceries/en-GB/products/7073880264', '/groceries/en-GB/products/7073910910', '/groceries/en-GB/products/7073880973', '/groceries/en-GB/products/7000309168', '/groceries/en-GB/products/7072269472', '/groceries/en-GB/products/7072352388', '/groceries/en-GB/products/7073916587', '/groceries/en-GB/products/7072700521', '/groceries/en-GB/products/7004693248']
>>> response.xpath("//img[@class='product-image']/@src").getall()
['https://secure.ap-tescoassets.com/assets/MY/208/9555067700208/ShotType1_225x225.jpg', 'https://secure.ap-tescoassets.com/assets/MY/073/8851347136073/ShotType1_225x225.jpg', 'https://secure.ap-tescoassets.com/assets/MY/215/9555067700215/ShotType1_225x225.jpg', 'https://secure.ap-tescoassets.com/assets/MY/453/8887549669453/ShotType1_225x225.jpg', 'https://secure.ap-tescoassets.com/assets/MY/460/8887549669460/ShotType1_225x225.jpg', 'https://secure.ap-tescoassets.com/assets/MY/256/8888021200256/ShotType1_225x225.jpg', 'https://secure.ap-tescoassets.com/assets/MY/617/9555018610617/ShotType1_225x225.jpg', 'https://secure.ap-tescoassets.com/assets/MY/720/8888021200720/ShotType1_225x225.jpg', 'https://secure.ap-tescoassets.com/assets/MY/760/9555630101760/ShotType1_225x225.jpg', 'https://secure.ap-tescoassets.com/assets/MY/228/5052525877228/ShotType1_225x225.jpg', 'https://secure.ap-tescoassets.com/assets/MY/777/9555630101777/ShotType1_225x225.jpg', 'https://secure.ap-tescoassets.com/assets/MY/267/9557054011267/ShotType1_225x225.jpg', 'https://secure.ap-tescoassets.com/assets/MY/749/9556500901749/ShotType1_225x225.jpg', 'https://secure.ap-tescoassets.com/assets/MY/535/9557225022535/ShotType1_225x225.jpg', 'https://secure.ap-tescoassets.com/assets/MY/099/9557187020099/ShotType1_225x225.jpg', 'https://secure.ap-tescoassets.com/assets/MY/592/9555630108592/ShotType1_225x225.jpg', 'https://secure.ap-tescoassets.com/assets/MY/414/9557992502414/ShotType1_225x225.jpg', 'https://secure.ap-tescoassets.com/assets/MY/728/9557992502728/ShotType1_225x225.jpg', 'https://secure.ap-tescoassets.com/assets/MY/105/9556091511105/ShotType1_225x225.jpg', 'https://secure.ap-tescoassets.com/assets/MY/194/5054548599194/ShotType1_225x225.jpg', 'https://secure.ap-tescoassets.com/assets/MY/208/9555546621208/ShotType1_225x225.jpg', 'https://secure.ap-tescoassets.com/assets/MY/603/9557225022603/ShotType1_225x225.jpg', 'https://secure.ap-tescoassets.com/assets/MY/484/9557368157484/ShotType1_225x225.jpg', 'https://secure.ap-tescoassets.com/assets/MY/081/9557368156081/ShotType1_225x225.jpg']
>>> response.xpath('//a[contains(@data-auto, "product-tile--title")]/text()').getall()
['IK Yellow A4 Multifunction Business Paper 70gsm 450 Sheets', 'Staedtler Luna 24 Coloured Pencils + Free Sharpener', 'IK Yellow Multifunction Business Paper A4 80gsm 450 Sheets', 'Panasonic AA 1.5V Alkaline Battery 8pcs', 'Panasonic AAA 1.5V Alkaline Battery 8pcs', 'Energizer Max AA 1.5V Alkaline Batteries 8 Pack', 'Tesco A4 Copier Paper 80gsm 450 Sheets', 'Energizer Max AAA 1.5V Alkaline Batteries 8 Pack', 'VS Star Fire Plastic Spoon 170mm x 50pcs', 'Tesco Extra Long Life AAA 1.5V Alkaline Batteries 4 Pack', 'VS Star Fire Plastic Fork 170mm x 50pcs', 'Panasonic Extra Heavy Duty AA 1.5V 4 Batteries', 'Eveready Super Heavy Duty AA 1.5V Battery 12pcs', 'Tesco 3 Inches Arch File 2pcs', 'Panasonic Extra Heavy Duty AAA 1.5V Zinc Carbon Battery 4pcs', "StarFire 6oz Printed Paper Cup 50's", 'StarFire Disposable Party Wares 5" Plastic Stirrer 50pcs', 'StarFire 7" White Paper Plate 50pcs', 'Stabilo Legacy 1183 Eraser 6pcs', 'Tesco Basics Zinc Chloride AA 1.5V Batteries 4 Pack', 'Mag Butane Fuel Cartridge 4 x 230g', 'Tesco 2D Insert Binder White 25mm', 'Unicorn B-8800 2B Blacklead Pencil 12pcs', 'Unicorn Max No. 10 2 x 1000 Staples']


```
