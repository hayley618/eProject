"""
Basic skeleton of a mitmproxy addon.

Run as follows: mitmproxy -s anatomy.py
"""
from mitmproxy import ctx


class Counter:
    def __init__(self):
        self.num = 0

    def request(self, flow):
        self.num = self.num + 1
        ctx.log.info("We've seen %d flows" % self.num)

#1、插件   2、[obj]  列表中包含实例对象
addons = [
    Counter()
]

if __name__ == '__main__':
    from mitmproxy.tools.main import mitmdump
    mitmdump(['-p', '8889', '-s', __file__])