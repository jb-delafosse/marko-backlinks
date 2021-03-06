from pathlib import Path
from unittest import mock

from linky_note.usecases.parse import parse
from marko.block import Document


@mock.patch(
    "glob.glob",
    return_value=["Marketing.md", "DigitalMarketing.md", "BusinessUnit.md"],
)
def test_parse_nominal(mock_glob, note_parser):
    # Given
    directory = Path()
    note_parser.return_value = object.__new__(Document)

    # When
    parsed_files = parse(directory)

    # Then
    assert "Marketing.md" in parsed_files
    assert "DigitalMarketing.md" in parsed_files
    assert "BusinessUnit.md" in parsed_files
