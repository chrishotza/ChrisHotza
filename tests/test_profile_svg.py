"""Synthetic SVG safety tests; original profile illustrations remain untouched."""
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from scripts.check_profile import inspect_svg


class SvgProfileGuardTests(unittest.TestCase):
    def inspect(self, fragment: str) -> list[str]:
        with TemporaryDirectory() as tmp:
            file = Path(tmp) / "test.svg"
            file.write_text(
                '<svg xmlns="http://www.w3.org/2000/svg">' +
                fragment + '</svg>',
                encoding="utf-8",
            )
            return inspect_svg(file)

    def test_valid_internal_gradient_reference_remains_accepted(self):
        self.assertEqual(self.inspect(
            '<defs><linearGradient id="g"><stop offset="1"/></linearGradient></defs>'
            '<rect width="10" height="10" fill="url(#g)"/>'
        ), [])

    def test_event_handlers_are_rejected_without_script_elements(self):
        for attr in ('onload="alert(1)"', 'onclick="alert(1)"',
                     'onmouseover="alert(1)"'):
            with self.subTest(attr=attr):
                self.assertTrue(any("attribute" in msg for msg in
                                    self.inspect('<rect ' + attr + '/>')))

    def test_external_resource_urls_are_rejected_in_paint_attributes(self):
        for value in (
            "url(https://example.invalid/image.svg)",
            "url(data:image/svg+xml;base64,QQ==)",
            "url(../outside.svg#shape)",
            "url(javascript:alert)",
        ):
            with self.subTest(value=value):
                self.assertTrue(any("External SVG URL" in msg for msg in
                                    self.inspect('<rect fill="' + value + '"/>')))

    def test_css_imports_and_animations_are_rejected(self):
        self.assertTrue(self.inspect('<rect style="@import url(https://example.invalid/x)"/>'))
        for tag in ('animate', 'set', 'animateTransform', 'style', 'a'):
            with self.subTest(tag=tag):
                self.assertTrue(any("unsafe SVG element" in msg for msg in
                                    self.inspect('<' + tag + '/>')))

    def test_xlink_reference_is_rejected(self):
        fragment = (
            '<use xmlns:xlink="http://www.w3.org/1999/xlink" '
            'xlink:href="https://example.invalid/external.svg#id"/>'
        )
        self.assertTrue(any("href attribute" in msg for msg in self.inspect(fragment)))

    def test_invalid_xml_fails(self):
        with TemporaryDirectory() as tmp:
            file = Path(tmp) / "bad.svg"
            file.write_text("<svg><rect></svg>", encoding="utf-8")
            self.assertTrue(any("Invalid XML" in msg for msg in inspect_svg(file)))


if __name__ == "__main__":
    unittest.main()
