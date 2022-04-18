from src.parser.osm_reader import Parser

if __name__=='__main__':
    parsed_file = Parser('map.osm')
    print(parsed_file.nodes())
    print(next(parsed_file.nodes()))
