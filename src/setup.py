from setuptools import setup
import setup_translate

pkg = 'Extensions.ZDFMediathek'
setup(name='enigma2-plugin-extensions-zdfmediathek',
       version='3.0',
       description='Zugriff auf die ZDF-Mediathek',
       package_dir={pkg: 'ZDFMediathek'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', 'logo.png', 'maintainer.info', 'keymap.xml', 'skin_FHD.xml', 'skin_HD.xml', 'img/*.png']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
