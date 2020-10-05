
import xml.etree.ElementTree as ET
from homework_top_words import top_long_words

parser = ET.XMLParser(encoding='utf-8')
tree = ET.parse('newsafr.xml', parser)
root = tree.getroot()
xml_items = root.findall('channel/item')
words_list = ' '.join(item.find('description').text for item in xml_items).split()

print(*top_long_words(words_list, 6, 10), sep='\n')



