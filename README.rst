========================================
Prakuli
========================================

a practice to write something like `Sikuli <http://www.sikulix.com/>`_

Dependency
========================================

+------------------------------------------------------------+----------------------+----------------------------+
| Library                                                    | Usage                | Note                       |
+============================================================+======================+============================+
| `SimpleCV <https://github.com/sightmachine/SimpleCV>`_     | Computer Vision      |                            |
+------------------------------------------------------------+----------------------+----------------------------+
| `PyUserInput <https://github.com/SavinaRoja/PyUserInput>`_ | Mouse/Keyboard Input |                            |
+------------------------------------------------------------+----------------------+----------------------------+
| `pyscreenshot <https://github.com/ponty/pyscreenshot>`_    | Screenshot           | by SimpleCV's ScreenCamera |
+------------------------------------------------------------+----------------------+----------------------------+

Todo
========================================

- [x] `Click <http://doc.sikuli.org/region.html?highlight=click#Region.click>`_
- [ ] `Type <http://doc.sikuli.org/region.html?highlight=click#Region.type>`_
- [ ] setup script
- [ ] GUI for image display

Run
========================================

there is no GUI for image display and select now, so just import this program and write the code

.. code-block:: python

    # test.py
    from prakuli import *

    # it will find the image in `images/` folder
    # or give a absolutely path
    doubleClick('test.png')

now run it by ``python2 test.py``, it will start to find ``test.png`` on the screen and double click it
