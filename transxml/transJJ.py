try:
  import xml.etree.cElementTree as ET
except ImportError:
  import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ElementTree,Element

tree = ET.parse("1raw.xml")
root = tree.getroot()

def create_node(tag, property_map, content):
    '''新造一个节点
       tag:节点标签
       property_map:属性及属性值map
       content: 节点闭合标签里的文本内容
       return 新节点'''
    element = Element(tag, property_map)
    element.text = content
    return element
for gift in root.findall('gift'):
  root.remove(gift)

for child in root:
  if(child.tag == 'd'):
    del child.attrib['raw']
    child.text += '('
    child.text += child.attrib['user']
    child.text += ')'
    del child.attrib['user']

  if(child.tag == 'sc'):
    child.text += '(((('
    child.text += child.attrib['user']
    child.text += '的￥'
    child.text += child.attrib['price']
    child.text += '醒目留言))))'
    del child.attrib['raw']
    del child.attrib['user']
    del child.attrib['time']
    del child.attrib['price']

for sc in root.findall('sc'):
  sc.set('p', sc.attrib['ts'])
  del sc.attrib['ts']
  sc.tag = 'd'

tree.write("./refresh.xml", encoding="utf-8", xml_declaration=True)