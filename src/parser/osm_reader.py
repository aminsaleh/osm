import xml.etree.cElementTree as ET
from pathlib import Path
from types import SimpleNamespace
from loguru import logger

from src.config import DATA_PATH


class Parser:
    def __init__(self, file_name='map.osm'):
        self.file_name = file_name
        if isinstance(file_name, Path):
            self.file_path = file_name
        else:
            self.file_path = Path.joinpath(DATA_PATH, file_name)
        self._root = self._reader()

    def _reader(self):
        try:
            tree = ET.parse(self.file_path)
            logger.info(f'{self.file_name} parsed succesfully!')
            return tree.getroot()
        
        except FileNotFoundError:
            logger.exception(f'{self.file_name} not found!')

    def nodes(self):
        tag = 'node'
        for node in self._root.iter(tag):
            yield node.attrib

    def ways(self):
        tag = 'way'
        for way in self._root.iter(tag):
            yield way.attrib

    def relations(self):
        tag = 'relation'
        for relation in self._root.iter(tag):
            yield relation.attrib
    
    def count(self):
        nodes_cnt = sum(1 for _ in self.nodes())
        ways_cnt = sum(1 for _ in self.ways())
        relations_cnt = sum(1 for _ in self.relations())
        cnt = SimpleNamespace(
            nodes=nodes_cnt,
            ways=ways_cnt,
            relations=relations_cnt,
            total=nodes_cnt+ways_cnt+relations_cnt,
        )
        return cnt
        

    def __repr__(self) -> str:
        return f"Object of {self.file_name} file"
