from DrissionPage import Chromium

from get_lasturl import get_part1
page = Chromium(9223)
page = page.new_tab('https://www.xiaohongshu.com/explore/66d6fb740000000012013b38?xsec_token=ABbFzuWKVd594YK7auJ8PZecfvCCWEBLAnq3LX0M1qJfk=&xsec_source=pc_search')
get_part1(page, 1, 'https://www.xiaohongshu.com/explore/66d6fb740000000012013b38?xsec_token=ABbFzuWKVd594YK7auJ8PZecfvCCWEBLAnq3LX0M1qJfk=&xsec_source=pc_search', 1)

