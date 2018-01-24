# super famicom wars // translation project

This is the full source for the [Super Famicom Wars] english translation [patch].

For credits and more information on the history of the project, please refer to the [release notes](./docs/release/mb-sfwe.txt)!


## building

The domain specific tools are included as source in the repository, so all that 
is needed to build is make, CMake, a C/C++ toolchain, python 2.7 and a Unix-like command line.

You will also need to source the ROM image of Super Famicom Wars ([NP]) and copy 
it to this path:

```
path: rom/Super Famicom Wars (Japan) (NP).sfc
md5:  d88b4ed9a9d834696357ce4c9ef95359
```

To build, simply run `make` in the project root.


[Super Famicom Wars]: https://www.nintendo.co.jp/n02/shvc/bfwj/index.html
[patch]: https://www.romhacking.net/translations/3354/
[NP]: https://en.wikipedia.org/wiki/Nintendo_Power_(cartridge)
