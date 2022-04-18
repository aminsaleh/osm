from src.parser.osm_reader import Parser
from src.config import SAMPLE_FILE_PATH

parsed_file = Parser(file_name=SAMPLE_FILE_PATH)

def test_parser():
    assert parsed_file.count().nodes == 32
    assert parsed_file.count().ways == 2
    assert parsed_file.count().relations == 1
    assert parsed_file.count().total == 35
