'''
尽可能多的匹配

注意：贪婪模式与非贪婪模式
贪婪模式：在整个表达式匹配成功的前提下，尽可能多的匹配 ( * )；
非贪婪模式：在整个表达式匹配成功的前提下，尽可能少的匹配 ( ? )；
Python里数量词默认是贪婪的。
示例一 ： 源字符串：abbbc
使用贪婪的数量词的正则表达式 ab* ，匹配结果： abbb。
* 决定了尽可能多匹配 b，所以a后面所有的 b 都出现了。
使用非贪婪的数量词的正则表达式ab*?，匹配结果： a。
即使前面有 *，但是 ? 决定了尽可能少匹配 b，所以没有 b。
示例二 ： 源字符串：aa<div>test1</div>bb<div>test2</div>cc
使用贪婪的数量词的正则表达式：<div>.*</div>
匹配结果：<div>test1</div>bb<div>test2</div>
这里采用的是贪婪模式。在匹配到第一个“</div>”时已经可以使整个表达
式匹配成功，但是由于采用的是贪婪模式，所以仍然要向右尝试匹配，
查看是否还有更长的可以成功匹配的子串。匹配到第二个“</div>”后，
向右再没有可以成功匹配的子串，匹配结束，匹配结果为
“<div>test1</div>bb<div>test2</div>”

使用非贪婪的数量词的正则表达式：<div>.*?</div>
匹配结果：<div>test1</div>
正则表达式二采用的是非贪婪模式，在匹配到第一个“</div>”
时使整个表达式匹配成功，由于采用的是非贪婪模式，
所以结束匹配，不再向右尝试，匹配结果为“<div>test1</div>”。
'''
import re

content = '''
    <div class="thumb">
        <a href="/article/120980088" target="_blank">
            <img src="//pic.qiushibaike.com/system/pictures/12098/120980088/medium/AUX058FU13B3S72D.jpg" alt="糗事#120980088" class="illustration" width="100%" height="auto">
        </a>
    </div>
    <div class="thumb">
        <a href="/article/118484461" target="_blank">
            <img src="//pic.qiushibaike.com/system/pictures/11848/118484461/medium/app118484461.jpg" alt="糗事#118484461" class="illustration" width="100%" height="auto">
        </a>
    </div>
    <div class="thumb">
        <a href="/article/118484011" target="_blank">
            <img src="//pic.qiushibaike.com/system/pictures/11848/118484011/medium/app118484011.jpg" alt="糗事#118484011" class="illustration" width="100%" height="auto">
        </a>
    </div>
'''

p = re.compile(r'<div.*?<img src="(.*?)" alt=".*?"',re.S)

#p = re.compile(r'<div class="thumb">.*?<img src="(.*?)" alt=".*?"',re.S)

src_list = p.findall(content)

for i in range(len(src_list)):
    src = src_list[i]
    print(src)

