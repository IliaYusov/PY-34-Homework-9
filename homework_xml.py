import xml.etree.ElementTree as ET
from homework_top_ten import top_ten_longer_than_six

parser = ET.XMLParser(encoding='utf-8')
tree = ET.parse('newsafr.xml', parser)
root = tree.getroot()
xml_items = root.findall('channel/item')
words_list = ' '.join(item.find('description').text for item in xml_items).split()

print(*top_ten_longer_than_six(words_list), sep='\n')



