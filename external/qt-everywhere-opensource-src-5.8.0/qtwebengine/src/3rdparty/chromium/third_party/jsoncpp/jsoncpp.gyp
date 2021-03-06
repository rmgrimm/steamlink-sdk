# Copyright (c) 2012 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'variables': {
    'use_system_jsoncpp%': 0,
  },
  'conditions' : [
    ['use_system_jsoncpp == 0', {
  'includes': [
    'jsoncpp.gypi',
  ],
  'targets': [
    {
      'target_name': 'jsoncpp',
      'type': 'static_library',
    },
  ],
  }, #  'use_system_jsoncpp == 0'
  {
  'targets': [
    {
      'target_name': 'jsoncpp',
      'type': 'none',
      'variables': {
        'headers_root_path': 'source/include',
        'header_filenames': [
          'json/assertions.h',
          'json/autolink.h',
          'json/config.h',
          'json/features.h',
          'json/forwards.h',
          'json/json.h',
          'json/reader.h',
          'json/value.h',
          'json/writer.h',
        ],
      },
      'includes': [
        '../../build/shim_headers.gypi',
      ],
      'direct_dependent_settings': {
        'cflags': [
          '<!@(<(pkg-config) --cflags jsoncpp)',
        ],
      },
      'link_settings': {
        'ldflags': [
          '<!@(<(pkg-config) --libs-only-L --libs-only-other jsoncpp)',
        ],
        'libraries': [
          '<!@(<(pkg-config) --libs-only-l jsoncpp)',
        ],
      },
    }
  ],
  }
  ]]
}

# Local Variables:
# tab-width:2
# indent-tabs-mode:nil
# End:
# vim: set expandtab tabstop=2 shiftwidth=2:
