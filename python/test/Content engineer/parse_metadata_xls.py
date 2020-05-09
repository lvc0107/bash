import xlrd
from lxml import etree
from datetime import datetime
import logging
import sys
import re

logger = logging.getLogger(__name__)
my_stream_handler = logging.StreamHandler(stream=sys.stdout)
my_stream_handler.setLevel(logging.INFO)

logger.setLevel(logging.DEBUG)
logger.addHandler(my_stream_handler)

# columns names
PATH = 'path'
TITLE = 'track title'
ISRC = 'isrc'
ARTIST = 'main artist'
LABEL = 'label'


def is_ISRC_valid(isrc):
    # Expected format : "CC-XXX-YY-NNNNN".
    return re.match(r"^[a-zA-Z]{2}-[0-9a-zA-Z]{3}-[0-9]{2}-[0-9]{5}$", isrc)


def check_file_exist(file_path):
    file_location = "./filenames.txt"
    with open(file_location, 'rb') as file:
        if file_path in file.read():
            return True

    return False


def is_data_valid(row, xls_idx, row_index):
    try:
        list_missing = []

        if not row[row_index[TITLE]]:
            list_missing.append(TITLE)
            logger.error("Missing required data: '{0}' in row {1} - {2}".format(TITLE, xls_idx, row))

        if not row[row_index[ARTIST]]:
            list_missing.append(ARTIST)
            logger.error("Missing required data: '{0}' in row {1} - {2}".format(ARTIST, xls_idx, row))

        file_exist = False
        if not row[row_index[PATH]]:
            list_missing.append(PATH)
            logger.error("Missing required data: '{0}' in row {1} - {2}".format(PATH, xls_idx, row))
        else:
            file_exist = check_file_exist(row[row_index[PATH]])
            if not file_exist:
                list_missing.append(PATH)
                logger.error("Missing required data. The file is missing '{0}' in row {1} - {2}".format(PATH, xls_idx, row))

        isrc_valid = False
        if not row[row_index[ISRC]]:
            list_missing.append(ISRC)
            logger.error("Missing required data: '{0}' in row {1} - {1}".format(ISRC, xls_idx, row))
        else:
            isrc_valid = is_ISRC_valid(row[row_index[ISRC]])
            if not isrc_valid:
                logger.error("Missing required data: ISRC has invalid format: '{0}' in row {1} - {1}".format(
                    row[row_index[ISRC]], xls_idx, row))

        return not list_missing and isrc_valid and file_exist
    except Exception as e:
        logger.error(e)
        return False


def write_xml(data, row_index):
    columns = data[0]
    list_of_expected_labels = [PATH, TITLE, ARTIST, LABEL, ISRC]
    extra_fields = set(columns) - set(list_of_expected_labels)

    customer_name = "customer name"
    date_created = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
    ingestion = etree.Element("ingestion", name=customer_name, dateCreated=date_created)
    etree.tostring(ingestion, xml_declaration=True, encoding="utf-8")
    tracks = etree.SubElement(ingestion, "tracks")
    for xls_idx, row in enumerate(data[1:]):
        offset = 2  # The real data start in row number 2
        if is_data_valid(row, xls_idx + offset, row_index):
            track = etree.SubElement(tracks, "track", id='track_id')
            title = etree.SubElement(track, "title")
            fingerprint_uri = etree.SubElement(track, "fingerprint_uri")
            audio_uri = etree.SubElement(track, "audio_uri")
            video_uri = etree.SubElement(track, "video_uri")
            year = etree.SubElement(track, "year")
            label = etree.SubElement(track, "label")
            duration = etree.SubElement(track, "duration")
            number = etree.SubElement(track, "number")
            isrc = etree.SubElement(track, "ISRC")

            artists = etree.SubElement(track, "artists")
            artist = etree.SubElement(artists, "artist")

            releases = etree.SubElement(track, "releases")
            release = etree.SubElement(releases, "release")

            genres = etree.SubElement(track, "genres")
            genre = etree.SubElement(genres, "genre")

            extras = etree.SubElement(track, "extras")
            for colum_name in extra_fields:
                extra = etree.SubElement(extras, "extra", name=colum_name)
                extra.text = row[row_index[colum_name]]

            title.text = row[row_index[TITLE]]
            audio_uri.text = row[row_index[PATH]]
            artist.text = row[row_index[ARTIST]]
            label.text = row[row_index[LABEL]]
            isrc.text = row[row_index[ISRC]]

    tree = etree.ElementTree(ingestion)
    tree.write('./ingestion.xml', xml_declaration=True, encoding="UTF-8")


def process_xls():
    file_location = "./metadata.xls"
    with xlrd.open_workbook(file_location) as workbook:
        sheet = workbook.sheet_by_index(0)
        data = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]
        columns = data[0]

        """
        I built an association  between the column name in a data row and
        its position in the data list, in order to use the column name for indexing.

           Index in dict    index in la data list                             
        index['path']        = 0
        index['track title'] = 1
        index['main artist'] = 2
        index['album title'] = 3
        index['label']       = 4
        index['isrc']        = 5
        """
        index = {}
        for i in range(len(columns)):
            index[columns[i]] = i

        write_xml(data, index)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        logger.error(sys.argv)
        logger.error("Error: Execute $python parse_metadata_xls.py metadata.xls ingestion.xml")
        sys.exit(1)

    metadata = sys.argv[1]
    output_file = sys.argv[2]
    process_xls()
