# teslabs KiCAD Library

This repository contains Teslabs collection of KiCAD symbols, footprints and
related files.

## Plugins

Commonly used plugins can be installed by running `install-plugins` script. This
is the current list of installed plugins:

- [InteractiveHtmlBom](https://github.com/openscopeproject/InteractiveHtmlBom)
- [ViaStitching](https://github.com/jsreynaud/kicad-action-scripts)

## 3D models

Custom 3D models are provided for some footprints. In order to make them work
the corresponding footprints have in their search path
`${KIPRJMOD}/teslabs-kicad/...` so that 3D models are found when this repository
is used as a submodule.

## Other useful resources

- [@adamgreig's KiCAD Library](https://github.com/adamgreig/agg-kicad)
- [KiCad Third-Party Tools](https://github.com/xesscorp/kicad-3rd-party-tools)
- [Smisioto KiCAD Libraries](http://smisioto.no-ip.org/elettronica/kicad/kicad-en.htm)
