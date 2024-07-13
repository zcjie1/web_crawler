class UrlManager:
    #初始化函数
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    #添加新url
    def add_url(self, url):
        if url is None or len(url) == 0:
            return
        if url in self.old_urls or url in self.new_urls:
            return
        self.new_urls.add(url)

    #批量添加url
    def add_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_url(url)

    #取出一个url
    def get_url(self):
        if self.have_new_url():
            url = self.new_urls.pop()
            self.old_urls.add(url)
            return url
        else:
            return None

    #判断是否存在新url
    def have_new_url(self):
        return len(self.new_urls) > 0