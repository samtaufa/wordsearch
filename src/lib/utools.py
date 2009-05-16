#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

    :copyright: (c) 2009, Samiuela Loni Vea Taufa
    :license: ISCL, see LICENSE.txt for more details
"""
# code below derived in part or whole from:
# http://ginstrom.com/scribbles/2008/03/08/using-chardet-to-convert-arbitrary-byte-strings-to-unicode/
#
# chardet available from http://chardet.feedparser.org

import chardet 

class unicodetools:
    """ Unicode Tools
    """
    def __init__(self):
        pass
    def bytes2unicode(self, bytes, errors='replace'):
        """Convert a byte string into Unicode.
        First checks for a BOM, and if one is found returns
        the Unicode text minus the BOM. If there is no BOM,
        falls back to chardet."""
       
        encoding_map = (('\xef\xbb\xbf', 'utf-8'),
                        ('\xff\xfe\0\0', 'utf-32'),
                        ('\0\0\xfe\xff', 'UTF-32BE'),
                        ('\xff\xfe', 'utf-16'),
                        ('\xfe\xff', 'UTF-16BE'))

        for bom, encoding in encoding_map:
            if bytes.startswith(bom):
                return unicode(bytes[len(bom):],
                               encoding,
                               errors=errors)
       
        # No BOM found, so use chardet
        detection = chardet.detect(bytes)
        encoding = detection.get('encoding') or 'utf-16'
        return unicode(bytes, encoding, errors=errors)

    def convNotSoSmartQuotesToHtmlEntity(x):
        """ [ref: http://myzope.kedai.com.my/blogs/kedai/128]
        """
        d = {
            "\xc2\x82":"&sbquo;",
            "\xc2\x83":"&fnof;",
            "\xc2\x84":"&bdquo;",
            "\xc2\x85":"&hellip;",
            "\xc2\x86":"&dagger;",
            "\xc2\x87":"&Dagger;",
            "\xc2\x88":"&circ;",
            "\xc2\x89":"&permil;",
            "\xc2\x8A":"&Scaron;",
            "\xc2\x8B":"&lsaquo;",
            "\xc2\x8C":"&OElig;",
            "\xc2\x91":"&lsquo;",
            "\xc2\x92":"&rsquo;",
            "\xc2\x93":"&ldquo;",
            "\xc2\x94":"&rdquo;",
            "\xc2\x95":"&bull;",
            "\xc2\x96":"&ndash;",
            "\xc2\x97":"&mdash;",
            "\xc2\x98":"&tilde;",
            "\xc2\x99":"&trade;",
            "\xc2\x9A":"&scaron;",
            "\xc2\x9B":"&rsaquo;",
            "\xc2\x9C":"&oelig;"
            }
        for i in d.keys():
            x=x.replace(i,d[i])
        return x
        