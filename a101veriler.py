import scrapy

class A101veriler(scrapy.Spider):

    name = 'a101veriler'
    allowed_domains = ['www.a101.com.tr']
    start_urls = ['https://www.a101.com.tr']

    def parse(self, response):

        category_linkler = []      
        linkler = response.xpath("//div[@class='col-sm-12 submenu-items']/ul/li[1]/a/@href")
        print(linkler)
        for i in linkler[:5]:
            categorylink = i.get()
            category_linkler.append(categorylink)
            print(categorylink)
        for categ in category_linkler:
            for count in range(25):
                full_link = f"https://www.a101.com.tr/{categ}?page={count}"
                yield scrapy.Request(url = full_link, callback=self.parse2)

 
    def parse2(self,response):
        try:
            urunler_isimleri = response.xpath('.//div[@class="product-desc "]/header/hgroup/h3/text()')
            urunler_fiyatlari = response.xpath('.//div[@class="product-desc "]/section[@class="prices"]/span/text()')

            urun_kategori1 = response.xpath('.//ol[@class="breadcrumb"]/li[2]/a/@href')
            urun_kategori2 = response.xpath('.//ol[@class="breadcrumb"]/li[3]/a/@href')

            urun_kategori1 = urun_kategori1.get()
            urun_kategori1 = urun_kategori1.replace("/","")
            urun_kategori2 = urun_kategori2.get()
            urun_kategori2 = urun_kategori2.split("/")[2]

        except:
            pass
        
        if len(urunler_isimleri) > 0:
            for isim,fiyat in zip(urunler_isimleri,urunler_fiyatlari):
                urun_ismi = isim.get()
                urun_ismi = urun_ismi.split("\n")[1][12:]
                urun_fiyati = fiyat.get()
                yield{
                    "name":urun_ismi,
                    "price":urun_fiyati,
                    "category1":urun_kategori1,
                    "category2":urun_kategori2
                }


