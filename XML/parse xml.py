# -*- coding: latin-1 -*-
import xml.etree.ElementTree as ElementTree

note = '''
<item>
<description>
<![CDATA[
<a href="http://gamek.vn/2018-roi-hay-cung-diem-lai-5-bi-kip-co-the-giup-ban-lam-chu-cuoc-choi-trong-pubg-nhe-20180111120431918.chn" title="2018 r?i, hãy cùng ?i?m l?i 5 bí kíp có th? giúp b?n LÀM CH? CU?C CH?I trong PUBG nhé!"><img src="http://genknews.genkcdn.vn/zoom/100_62/2018/photo-2-1515646870712.jpg" width="100" border="0" alt="2018 r?i, hãy cùng ?i?m l?i 5 bí kíp có th? giúp b?n LÀM CH? CU?C CH?I trong PUBG nhé!" /></a><span>?? có th? tr? nên pro trong PUBG, ng??i ch?i ph?i s? h?u khá nhi?u y?u t?, không ??n thu?n ch? là k? n?ng b?n súng thông th??ng, mà còn c?n ph?i có ??u óc nh?y bén và linh ho?t n?a. M?t s? m?o sau ?ây có th? giúp b?n th?ng tr? các tr?n ??u PUBG d? dàng h?n ??y.</span>
]]>
</description>
</item>
'''
root = ElementTree.fromstring(note)
for log in root.iter('description'):
    print(log.text)
