{
  'targets': [
    {
      'target_name': 'libtess2',
      'type': '<(library)',
      'direct_dependent_settings': {
        'include_dirs': [
          'Include',
          # 'Contrib',
        ],
      },
      'include_dirs': [
        'Include',
      ],
      'sources': [
        # 'Contrib/nanosvg.h',
        # 'Contrib/nanosvg.c',
        'Include/tesselator.h',
        'Source/bucketalloc.h',
        'Source/bucketalloc.c',
        'Source/dict.h',
        'Source/dict.c',
        'Source/geom.h',
        'Source/geom.c',
        'Source/mesh.h',
        'Source/mesh.c',
        'Source/priorityq.h',
        'Source/priorityq.c',
        'Source/sweep.h',
        'Source/sweep.c',
        'Source/tess.h',
        'Source/tess.c',
      ]
    }
  ]
}