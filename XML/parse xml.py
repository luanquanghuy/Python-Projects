# -*- coding: latin-1 -*-
import xml.etree.ElementTree as ElementTree

note = '''
<item>
<description>
<![CDATA[
<a href="http://gamek.vn/2018-roi-hay-cung-diem-lai-5-bi-kip-co-the-giup-ban-lam-chu-cuoc-choi-trong-pubg-nhe-20180111120431918.chn" title="2018 r?i, h�y c�ng ?i?m l?i 5 b� k�p c� th? gi�p b?n L�M CH? CU?C CH?I trong PUBG nh�!"><img src="http://genknews.genkcdn.vn/zoom/100_62/2018/photo-2-1515646870712.jpg" width="100" border="0" alt="2018 r?i, h�y c�ng ?i?m l?i 5 b� k�p c� th? gi�p b?n L�M CH? CU?C CH?I trong PUBG nh�!" /></a><span>?? c� th? tr? n�n pro trong PUBG, ng??i ch?i ph?i s? h?u kh� nhi?u y?u t?, kh�ng ??n thu?n ch? l� k? n?ng b?n s�ng th�ng th??ng, m� c�n c?n ph?i c� ??u �c nh?y b�n v� linh ho?t n?a. M?t s? m?o sau ?�y c� th? gi�p b?n th?ng tr? c�c tr?n ??u PUBG d? d�ng h?n ??y.</span>
]]>
</description>
</item>
'''
root = ElementTree.fromstring(note)
for log in root.iter('description'):
    print(log.text)
